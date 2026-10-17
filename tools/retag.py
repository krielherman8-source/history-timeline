# Re-apply tags.py (categories + threads) to ALL entries in entries.json and regenerate data.js.
# Needed because add.py only tags the entries it appends, so threads grown in later batches
# (addt calls naming older ids) would otherwise never reach the older entries.
import json,sys
sys.path.insert(0,'.');import tags
p='../entries.json';d=json.load(open(p))
missing=[e['id'] for e in d['entries'] if e['id'] not in tags.C]
if missing: sys.exit('no categories for: '+' '.join(missing))
ids={e['id'] for e in d['entries']}
dangling=sorted({i for v in tags.T.values() for i in v.split() if i not in ids})
before={e['id']:(e['categories'],e['threads']) for e in d['entries']}
tags.apply(d['entries'])
ch=[e['id'] for e in d['entries'] if before[e['id']]!=(e['categories'],e['threads'])]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
open('../data.js','w').write('// generated from entries.json - do not edit\nwindow.TIMELINE_DATA='+json.dumps(d,ensure_ascii=False)+';\n')
print('retagged',len(ch),'entries:',' '.join(ch));print('thread ids not (yet) in entries:',' '.join(dangling));print('total',len(d['entries']))
