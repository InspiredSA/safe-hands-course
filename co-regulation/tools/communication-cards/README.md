# ELS printable communication cards

Three A4, three-page PDF packs: English (`en`), French (`fr`) and Mauritian Creole (`mfe`). Each pack contains one adult guidance page, eight original word-and-symbol cards, and an optional separate Nappy card plus seven customization blanks. These are optional starter examples, not a complete AAC system or an individual clinical prescription.

## Print

- A4, portrait, single-sided, **100% / Actual size**
- Cut on each card's solid outer outline; the dashed inset on a blank is a photo guide
- Each card is approximately 88.4 × 54.3 mm at 100%
- Print pages 2 and 3 for cards; keep page 1 for adult preparation
- Follow the adult guidance for mounting, safe edges and familiar communication
- Dark navy illustrations and labels remain distinguishable in grayscale; color is not used to convey the message

## Edit and rebuild

`cards_text.json` contains the complete wording for all three languages, the card order, labels and source links. `generate_cards.py` contains every original vector drawing, page layout and text placement. The source is portable and uses paths relative to the script by default.

Requires Python 3 and `reportlab`. Rebuild the bundled layout:

```sh
python3 generate_cards.py
```

From the repository root, rebuild the hosted downloads with:

```sh
python3 co-regulation/tools/communication-cards/generate_cards.py \
  --output-dir co-regulation/downloads \
  --report-path /tmp/communication-card-layout.json
```

You can also pass `--brand-dir`, `--font-dir` and `--text-json` when using a different layout.

The brand directory must contain `inspired-logo-colour.png`. The font directory must contain the supplied `OpenSans-Regular.ttf`, `OpenSans-Semibold.ttf` and `OpenSans-Bold.ttf`. Keep `OpenSans-OFL.txt` with redistributed fonts. The PDFs embed the used font subsets. A layout overflow causes generation to fail rather than silently losing content.

After edits, regenerate and inspect all pages using Poppler:

```sh
pdftoppm -r 150 -png output/pdf/communication-cards-en.pdf tmp/pdfs/en
```

Repeat for French and Mauritian Creole. Confirm that card labels match the child's actual communication; do not simply substitute this pack for an established AAC system. French and Mauritian Creole adult pages explicitly mark the translations as drafts for checking by a fluent local speaker and the child's team before use.

## Artwork and brand

The line illustrations and card templates were made for this pack. Schools may print, copy and adapt this original artwork and these templates for educational use. This permission **does not cover the Inspired logo**. The existing logo is reproduced unmodified from the supplied course branding. No ASHA, NCPMI or commercial AAC programme graphics are reproduced.

The source references on page 1 link to:

- [ASHA: Augmentative and Alternative Communication](https://www.asha.org/Practice-Portal/Professional-Issues/Augmentative-and-Alternative-Communication/)
- [NCPMI: Tips and Ideas for Making Visuals](https://challengingbehavior.org/docs/tips_for_visuals.pdf)

Both were checked on 7 October 2026. They support multimodal communication, access to established AAC, and matching visual representations to an individual child's understanding. They do not validate these original example symbols or their translations.
