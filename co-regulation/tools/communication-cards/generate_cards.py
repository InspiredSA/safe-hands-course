#!/usr/bin/env python3
"""Build the three ELS A4 communication-card packs.

Edit cards_text.json to adapt words and adult guidance. The vector symbols below
are original drawings, not copied from a commercial AAC symbol programme.
Requires: reportlab. Run: python3 generate_cards.py
"""
from pathlib import Path
import argparse
import json
import math
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, Color, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--brand-dir", type=Path, default=ROOT / "assets", help="Directory containing inspired-logo-colour.png")
parser.add_argument("--font-dir", type=Path, default=ROOT / "assets", help="Directory containing OpenSans-Regular.ttf, OpenSans-Semibold.ttf and OpenSans-Bold.ttf")
parser.add_argument("--text-json", type=Path, default=ROOT / "cards_text.json", help="Editable UTF-8 wording file")
parser.add_argument("--output-dir", type=Path, default=ROOT / "output" / "pdf", help="Directory for the three PDFs")
parser.add_argument("--report-path", type=Path, default=ROOT / "layout_report.json", help="Optional layout report location")
ARGS = parser.parse_args()
ASSETS = ARGS.brand_dir.resolve()
FONTS = ARGS.font_dir.resolve()
OUT = ARGS.output_dir.resolve()
DATA = json.loads(ARGS.text_json.read_text(encoding="utf-8"))
OUT.mkdir(parents=True, exist_ok=True)
W, H = A4
M = 40
NAVY = HexColor("#122147")
BLUE = HexColor("#1B75BB")
TEXT = HexColor("#2F2F32")
MUTED = HexColor("#415165")
RULE = HexColor("#7C899A")
LIGHT = HexColor("#F1F5F8")
for name, filename in (("Body", "OpenSans-Regular.ttf"), ("Semi", "OpenSans-Semibold.ttf"), ("Bold", "OpenSans-Bold.ttf")):
    pdfmetrics.registerFont(TTFont(name, str(FONTS / filename)))


def paragraph(c, text, x, top, width, size=10.2, leading=14.0, font="Body", color=TEXT):
    style = ParagraphStyle("P", fontName=font, fontSize=size, leading=leading,
                           textColor=color, alignment=TA_LEFT, spaceBefore=0,
                           spaceAfter=0, allowWidows=0, allowOrphans=0)
    p = Paragraph(escape(text), style)
    _, ht = p.wrap(width, H)
    p.drawOn(c, x, top - ht)
    return top - ht


def centered(c, text, x, y, max_width, size=24, font="Semi", color=NAVY):
    while pdfmetrics.stringWidth(text, font, size) > max_width:
        size -= .25
    c.setFillColor(color)
    c.setFont(font, size)
    c.drawCentredString(x, y, text)


def header(c, d, title, subtitle, compact=False):
    c.setFillColor(NAVY)
    c.rect(0, H-8, W, 8, fill=1, stroke=0)
    c.drawImage(str(ASSETS / "inspired-logo-colour.png"), W-M-88, H-60,
                width=88, height=88*71/193, mask="auto", preserveAspectRatio=True)
    c.setFillColor(MUTED)
    c.setFont("Semi", 8.6)
    c.drawString(M, H-39, d["eyebrow"])
    title_size = 24 if compact else 25
    while pdfmetrics.stringWidth(title, "Semi", title_size) > W-2*M:
        title_size -= .25
    c.setFillColor(NAVY)
    c.setFont("Semi", title_size)
    c.drawString(M, H-88, title)
    bottom = paragraph(c, subtitle, M, H-102, W-2*M, size=9.2, leading=12.4, color=MUTED)
    return bottom


def footer(c, d, page):
    c.setStrokeColor(RULE)
    c.setLineWidth(.55)
    c.line(M, 39, W-M, 39)
    c.setFillColor(MUTED)
    c.setFont("Body", 7.4)
    c.drawString(M, 26, d["footer"])
    c.setFont("Semi", 7.4)
    c.drawRightString(W-M, 26, f"{d['language']}  |  {page} / 3")


def line(c, *points):
    p=c.beginPath(); p.moveTo(*points[0])
    for q in points[1:]: p.lineTo(*q)
    c.drawPath(p)


def path(c, commands, fill=False):
    p=c.beginPath()
    for cmd,args in commands:
        getattr(p,cmd)(*args)
    c.drawPath(p, stroke=1, fill=int(fill))


def star(c, x, y, r1=13, r2=7, n=8):
    pts=[]
    for i in range(n*2):
        ang=math.pi/2 + i*math.pi/n
        r=r1 if i%2==0 else r2
        pts.append((x+math.cos(ang)*r,y+math.sin(ang)*r))
    line(c, *(pts+[pts[0]]))


def icon_help(c):
    # Adult and child reaching toward one another; a relational help symbol.
    c.circle(71,79,10,stroke=1,fill=0)
    c.circle(24,58,8,stroke=1,fill=0)
    path(c,[("moveTo",(64,66)),("curveTo",(54,61,51,49,46,44)),
            ("lineTo",(38,43)),("lineTo",(30,47))])
    line(c,(77,66),(86,48),(92,48))
    path(c,[("moveTo",(64,66)),("lineTo",(61,37)),("lineTo",(80,37)),("lineTo",(77,66))])
    line(c,(65,37),(59,16),(52,16))
    line(c,(75,37),(81,16),(88,16))
    line(c,(20,48),(14,32),(9,31))
    line(c,(28,48),(32,27),(17,27),(20,48))
    line(c,(21,27),(18,13),(12,13))
    line(c,(28,27),(32,13),(38,13))


def icon_break(c):
    # Person seated on a chair with a small pause mark.
    c.circle(40,81,10,stroke=1,fill=0)
    path(c,[("moveTo",(38,69)),("curveTo",(32,61,32,50,38,45)),
            ("lineTo",(59,45)),("lineTo",(69,24)),("lineTo",(80,24))])
    line(c,(45,66),(49,55),(63,53))
    line(c,(24,58),(24,37),(60,37))
    line(c,(27,37),(22,16))
    line(c,(57,37),(62,16))
    c.roundRect(72,64,5,20,1.5,stroke=0,fill=1)
    c.roundRect(84,64,5,20,1.5,stroke=0,fill=1)


def icon_drink(c):
    # Open cup, visible water line and straw.
    path(c,[("moveTo",(26,70)),("lineTo",(34,17)),("lineTo",(68,17)),
            ("lineTo",(76,70)),("close",())])
    c.ellipse(26,65,76,75,stroke=1,fill=0)
    line(c,(31,47),(71,47))
    line(c,(53,39),(58,84),(75,89))


def icon_toilet(c):
    # Side-view toilet, tank, seat and pedestal.
    c.roundRect(61,52,23,34,3,stroke=1,fill=0)
    c.line(68,77,76,77)
    c.ellipse(19,47,77,57,stroke=1,fill=0)
    path(c,[("moveTo",(22,48)),("curveTo",(23,34,34,27,47,28)),
            ("lineTo",(43,14)),("lineTo",(72,14)),("lineTo",(68,48))])
    c.line(78,52,83,52)


def icon_hurt(c):
    # Neutral person with a hand near the torso and a pain burst.
    c.circle(47,82,10,stroke=1,fill=0)
    path(c,[("moveTo",(39,69)),("lineTo",(31,64)),("lineTo",(21,43)),
            ("curveTo",(18,34,24,30,31,33)),("lineTo",(45,43))])
    line(c,(55,69),(64,63),(72,57))
    line(c,(33,57),(34,32),(59,32),(59,57))
    line(c,(37,32),(33,13),(25,13))
    line(c,(56,32),(62,13),(70,13))
    star(c,74,39,14,7)


def icon_stop(c):
    # Palm facing out; open fingers are drawn as one continuous outline.
    path(c,[("moveTo",(36,13)),("lineTo",(34,29)),("lineTo",(18,50)),
            ("curveTo",(12,58,19,65,25,60)),("lineTo",(35,48)),
            ("lineTo",(35,81)),("curveTo",(35,90,46,90,46,81)),
            ("lineTo",(46,60)),("lineTo",(46,89)),
            ("curveTo",(46,97,57,97,57,89)),("lineTo",(57,61)),
            ("lineTo",(57,85)),("curveTo",(57,94,68,94,68,85)),
            ("lineTo",(68,60)),("lineTo",(68,74)),
            ("curveTo",(68,82,79,82,79,74)),("lineTo",(79,45)),
            ("curveTo",(79,31,70,25,69,13)),("close",())])
    path(c,[("moveTo",(44,40)),("curveTo",(50,45,59,45,65,40))])


def cube(c,x,y,s):
    # Square toy block; no letters that would bias the language.
    c.roundRect(x,y,s,s,2.3,stroke=1,fill=0)
    c.line(x+4,y+s-5,x+s-4,y+s-5)


def icon_more(c):
    cube(c,12,22,25)
    cube(c,41,22,25)
    cube(c,26,51,25)
    c.line(80,49,80,74)
    c.line(67.5,61.5,92.5,61.5)


def icon_finished(c):
    # Two blocks put away in a basket, with an open, clear check mark.
    cube(c,20,41,22)
    cube(c,45,41,22)
    path(c,[("moveTo",(13,43)),("lineTo",(21,15)),("lineTo",(76,15)),
            ("lineTo",(84,43)),("close",())])
    c.line(29,22,32,35); c.line(47,22,47,35); c.line(65,22,62,35)
    line(c,(62,79),(70,70),(88,91))


def icon_nappy(c):
    # Simple clean nappy, with front panel and fastening tabs.
    path(c,[("moveTo",(18,74)),("lineTo",(82,74)),("lineTo",(77,51)),
            ("curveTo",(65,49,63,23,51,20)),("curveTo",(38,23,36,49,23,51)),
            ("close",())])
    path(c,[("moveTo",(33,65)),("lineTo",(67,65)),("curveTo",(63,46,60,31,51,27)),
            ("curveTo",(41,31,37,46,33,65))])
    c.roundRect(14,60,20,12,2,stroke=1,fill=0)
    c.roundRect(66,60,20,12,2,stroke=1,fill=0)


ICONS = {"help":icon_help,"break":icon_break,"drink":icon_drink,
         "toilet":icon_toilet,"hurt":icon_hurt,"stop":icon_stop,
         "more":icon_more,"finished":icon_finished,"nappy":icon_nappy}


def draw_icon(c, name, x, y, size=96):
    c.saveState(); c.translate(x,y); c.scale(size/100,size/100)
    c.setStrokeColor(NAVY); c.setFillColor(NAVY)
    c.setLineWidth(3.15); c.setLineJoin(1); c.setLineCap(1)
    ICONS[name](c)
    c.restoreState()


def instruction_page(c, d):
    c.bookmarkPage("guidance"); c.addOutlineEntry(d["title"], "guidance", 0)
    top=header(c,d,d["title"],d["subtitle"])
    top-=17
    body_width=W-2*M
    box_top=top
    aac_title_h=14
    _, h=Paragraph(escape(d["aac_text"]),ParagraphStyle("AA",fontName="Body",fontSize=11,leading=15.4)).wrap(body_width-26,H)
    box_height=13+aac_title_h+7+h+13
    c.setFillColor(LIGHT); c.roundRect(M,box_top-box_height,body_width,box_height,5,fill=1,stroke=0)
    paragraph(c,d["aac_heading"],M+13,box_top-12,body_width-26,size=11.2,leading=14,font="Semi",color=NAVY)
    paragraph(c,d["aac_text"],M+13,box_top-33,body_width-26,size=11,leading=15.4)
    top=box_top-box_height-18
    for i,section in enumerate(d["sections"],1):
        c.setFillColor(BLUE); c.circle(M+9,top-8,9,stroke=0,fill=1)
        c.setFillColor(white); c.setFont("Semi",9.5); c.drawCentredString(M+9,top-11.4,str(i))
        top=paragraph(c,section["title"],M+27,top,body_width-27,size=11.8,leading=15.5,font="Semi",color=NAVY)
        top-=5
        top=paragraph(c,section["text"],M+27,top,body_width-27,size=11,leading=15.4)
        top-=14
    if d["translation_note"]:
        top=paragraph(c,d["translation_note"],M,top,body_width,size=8.8,leading=11.7,font="Semi",color=MUTED)-10
    top=paragraph(c,d["sources_heading"],M,top,body_width,size=8.2,leading=10.8,font="Semi",color=NAVY)-3
    for source in DATA["sources"]:
        text=source["label"]
        c.setFillColor(MUTED); c.setFont("Body",7.5); c.drawString(M,top-8,text)
        c.linkURL(source["url"],(M,top-10,M+pdfmetrics.stringWidth(text,"Body",7.5),top+1),relative=0,thickness=0)
        top-=11
    top-=5
    bottom=paragraph(c,d["art_note"],M,top,body_width,size=7.5,leading=10.3,color=MUTED)
    if bottom < 51:
        raise RuntimeError(f"Instruction page overflow for {d['language']}: bottom {bottom:.1f}")
    footer(c,d,1); c.showPage()
    return round(bottom,1)


def card(c, d, key, x, y, w, h):
    c.setStrokeColor(RULE); c.setLineWidth(.8)
    c.roundRect(x,y,w,h,7,stroke=1,fill=0)
    if key:
        draw_icon(c,key,x+w/2-48,y+45,96)
        centered(c,d["labels"][key],x+w/2,y+15,w-28,size=23)
    else:
        # This inset is a photo guide; keep the filled card's outer cut size.
        c.setStrokeColor(HexColor("#A7AFB8")); c.setLineWidth(.7); c.setDash(3,3)
        c.roundRect(x+35,y+51,w-70,h-65,4,stroke=1,fill=0)
        c.setDash()
        centered(c,d["photo_placeholder"],x+w/2,y+93,w-80,size=10,font="Body",color=MUTED)
        c.setStrokeColor(RULE); c.line(x+24,y+16,x+w-24,y+16)
        centered(c,d["word_placeholder"],x+w/2,y+26,w-40,size=9,font="Body",color=MUTED)


def grid_page(c,d,custom=False):
    page=3 if custom else 2
    title=d["custom_title"] if custom else d["cards_title"]
    subtitle=d["custom_instruction"] if custom else d["cards_instruction"]
    anchor="custom" if custom else "cards"
    c.bookmarkPage(anchor);c.addOutlineEntry(title,anchor,0)
    header(c,d,title,subtitle,compact=True)
    gap_x=14;gap_y=11
    card_w=(W-2*M-gap_x)/2
    card_h=154
    grid_top=H-144
    order=["nappy",None,None,None,None,None,None,None] if custom else DATA["card_order"]
    for i,key in enumerate(order):
        col=i%2;row=i//2
        x=M+col*(card_w+gap_x)
        y=grid_top-(row+1)*card_h-row*gap_y
        card(c,d,key,x,y,card_w,card_h)
    footer(c,d,page);c.showPage()


def main():
    report={}
    for language in ("en","fr","mfe"):
        d=DATA[language]
        dest=OUT/d["filename"]
        c=canvas.Canvas(str(dest),pagesize=A4,pageCompression=1)
        c.setTitle(f"{d['title']} | ELS | {d['language']}")
        c.setAuthor("ELS staff learning resource")
        c.setSubject("Optional communication-card examples for children aged 12 months and over")
        c.setKeywords("AAC, communication, co-regulation, print, A4, school")
        c.setViewerPreference("PrintScaling","None")
        report[language]={"guidance_content_bottom_pt":instruction_page(c,d)}
        grid_page(c,d);grid_page(c,d,custom=True);c.save()
        report[language]["pdf"]=str(dest)
    ARGS.report_path.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
