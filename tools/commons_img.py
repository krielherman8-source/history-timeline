# Attach a specific Wikimedia Commons file to an entry (verifies the file exists and is freely licensed via the Commons API).
# usage: python3 commons_img.py <entry-id> "File:Name.jpg"
import json,re,sys,urllib.request,urllib.parse,html
UA={'User-Agent':'history-timeline-builder/1.0 (https://github.com/krielherman8-source/history-timeline)'}
eid,fn=sys.argv[1],sys.argv[2]
q=json.load(urllib.request.urlopen(urllib.request.Request('https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=url|extmetadata&iiurlwidth=400&titles='+urllib.parse.quote(fn),headers=UA),timeout=30))
ii=list(q['query']['pages'].values())[0].get('imageinfo')
if not ii: sys.exit('not on Commons')
ii=ii[0];md=ii['extmetadata'];lic=md.get('LicenseShortName',{}).get('value','')
if not re.search(r'(CC|Public domain|PD|GFDL|CC0)',lic,re.I) or re.search('fair use|non-free',lic,re.I): sys.exit('licence not free: '+lic)
strip=lambda s: html.unescape(re.sub('<[^>]+>','',s or '')).strip()
m=dict(type='image',url=ii['thumburl'],page=ii['descriptionurl'],author=strip(md.get('Artist',{}).get('value',''))[:120] or 'Unknown',license=lic,title=fn.replace('File:','').replace(' ','_'))
p='../entries.json';d=json.load(open(p))
e=[x for x in d['entries'] if x['id']==eid][0]
e['media']=[x for x in e['media'] if x['type']!='image']+[m]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
open('../data.js','w').write('// generated from entries.json - do not edit\nwindow.TIMELINE_DATA='+json.dumps(d,ensure_ascii=False)+';\n')
print(eid,m)
