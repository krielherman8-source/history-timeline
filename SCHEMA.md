# Contributor guide / schema
Canonical data: `entries.json`. After editing, regenerate `data.js` (lets index.html work via file://):
`python3 -c "import json;d=json.load(open('entries.json'));open('data.js','w').write('window.TIMELINE_DATA='+json.dumps(d,ensure_ascii=False)+';')"`

Entry fields:
- `id` (string, unique), `title`, `lane`: `"history"` | `"myth"`
- `start`, `end` (number, astronomical-ish year; negative = BCE/years before 1 CE; `end` may be null), optional `dateNote`
- `evidenceTypes`: e.g. archaeological, geological/ice core, radiocarbon, textual, oral tradition, speculative
- `mainstream` (string), `alternatives`: [{`label`,`text`}] — neutral wording, mark untested claims "speculative"
- `sources`: [{`title`,`authors`?,`year`?,`doi` or `url`,`type`}]

Rules: only real, verifiable sources (prefer DOIs, museum/university pages, encyclopedias). If unsure, omit. Never invent a citation.
