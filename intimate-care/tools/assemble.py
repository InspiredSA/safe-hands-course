"""Rebuild static language bundles after editing their JSON source dictionaries."""
from pathlib import Path
import json
root = Path(__file__).resolve().parents[1]
languages = ("en", "fr", "mfe")
ui = {language: json.loads((root / f"ui-{language}.json").read_text()) for language in languages}
extras = {language: json.loads((root / f"course-extras-{language}.json").read_text()) for language in languages}
for language in languages:
    if set(ui[language]) != set(ui["en"]):
        raise ValueError(f"UI key mismatch: {language}")
    if len(extras[language]["meta"]) != 6 or len(extras[language]["practice"]) != 6:
        raise ValueError(f"Expected six modules and quick checks: {language}")
for filename, global_name, value in (("i18n.js", "COURSE_UI", ui), ("course-extras.js", "COURSE_EXTRAS", extras)):
    (root / filename).write_text(f"window.{global_name}=" + json.dumps(value, ensure_ascii=False, indent=2) + ";\n")
print("Rebuilt English, French and Kreol Morisien static dictionaries")
