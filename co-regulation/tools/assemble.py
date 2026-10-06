"""Build offline JavaScript bundles from the three reviewed source dictionaries.
Use --english-only only for interim development, never for the published course.
"""
from pathlib import Path
import json,sys
p=Path(__file__).resolve().parents[1]
langs=('en',) if '--english-only' in sys.argv else ('en','fr','mfe')
ui={l:json.loads((p/f'ui-{l}.json').read_text()) for l in langs}
extras={l:json.loads((p/f'course-extras-{l}.json').read_text()) for l in langs}
courses={l:json.loads((p/f'course-{l}.json').read_text()) for l in langs}
for l in langs:
 assert set(ui[l])==set(ui['en']),f'UI keys differ: {l}'
 assert len(extras[l]['meta'])==6 and len(extras[l]['practice'])==6,f'Module extras incomplete: {l}'
 assert len(courses[l]['modules'])==6 and len(courses[l]['questions'])==20,f'Course incomplete: {l}'
 assert [(q['answer'],q['critical']) for q in courses[l]['questions']]==[(q['answer'],q['critical']) for q in courses['en']['questions']],f'Question keys differ: {l}'
 assert sum(m['time'] for m in extras[l]['meta'])==48
 for i,m in enumerate(courses[l]['modules']):
  assert [len(page['blocks']) for page in m['pages']]==[len(page['blocks']) for page in courses['en']['modules'][i]['pages']],f'Block topology differs: {l}, module {i}'
 for field in ['visualGuides','videos','sources']:
  assert len(extras[l][field])==len(extras['en'][field]),f'Extras missing {field}: {l}'
for fn,global_name,data in [('i18n.js','COURSE_UI',ui),('course-extras.js','COURSE_EXTRAS',extras)]:
 (p/fn).write_text(f'window.{global_name}='+json.dumps(data,ensure_ascii=False,indent=2)+';\n')
for l in langs:
 fn='course-data.js' if l=='en' else f'course-data-{l}.js'
 name='COURSE' if l=='en' else f'COURSE_{l.upper()}'
 (p/fn).write_text(f'window.{name}='+json.dumps(courses[l],ensure_ascii=False,indent=2)+';\n')
print('Built: '+', '.join(langs))
