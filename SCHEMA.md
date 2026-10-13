# Contributor guide / schema (v2)
Canonical data: `entries.json`. `data.js` is generated from it (lets index.html work via file://):
`python3 -c "import json;d=json.load(open('entries.json'));open('data.js','w').write('window.TIMELINE_DATA='+json.dumps(d,ensure_ascii=False)+';')"`
Filter choices persist in the browser (localStorage key `tl-filters`). Bump `?v=N` on the script tags in index.html after changes (phone cache-busting).

Entry fields:
- `id` (unique), `title`, `lane`: `"history"` | `"myth"` (marker shape: circle / diamond)
- `status`: `confirmed` | `disputed` | `hypothesis` | `debunked` | `myth-legend` (marker colour + badge)
- `priority`: 1 (always labelled) | 2 (mid zoom) | 3 (close zoom only)
- `start`, `end` (year; negative = BCE; `end` may be null), optional `dateNote`
- `categories` (REQUIRED, ≥1): any of `history`, `science-cosmos`, `archaeology`, `myth-legend`, `religion`, `aliens-ufo`, `anomalies`, `lost-civilisations`, `catastrophes`, `hoaxes` (drives the filter panel; add new keys to `CATS` in app.js)
- `threads` (optional, may be empty): narrative threads linking entries, e.g. `flood-myths`, `lost-civilisations`, `sky-beings`, `cosmic-impacts`, `changed-understanding`, `dragons-and-fossils`. Selecting a thread highlights its entries and dims others; new thread names appear automatically.
- `evidenceTypes`: e.g. archaeological, geological/ice core, radiocarbon, genetic, textual, oral tradition, speculative
- `mainstream` (string), `alternatives`: [{`label`,`text`}] - neutral wording; mark untested claims "speculative"
- optional `changed`: how understanding shifted over time, with dates
- `sources`: [{`title`,`authors`?,`year`?,`doi` or `url`,`type`}]
- `media`: [{`type`:"image",`url` (upload.wikimedia.org ~400px thumb),`page` (Commons file page),`author`,`license`,`title`}
           | {`type`:"video",`url` (YouTube),`title`,`channel`} (title/channel from YouTube oEmbed)]

Rules: only real, verifiable sources (prefer DOIs, museum/university pages, encyclopedias); never invent a citation.
Images: freely licensed Wikimedia Commons files only, with credit. Videos: reputable channels only, verified via oEmbed.
Daily batches: every new entry MUST have `categories`; add `threads` where an obvious link exists. Tags live in `tools/tags.py` (`C` = categories, `T` = threads) and are applied by `tools/build.py`.
`tools/build.py` regenerates entries from `tools/entries_src.py`, verifying DOIs (Crossref), Wikipedia pages and Commons licences;
`tools/yt.py` finds and oEmbed-verifies videos (merge `videos.json` into media afterwards, reviewing relevance by hand).
