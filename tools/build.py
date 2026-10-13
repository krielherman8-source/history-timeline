import json,re,urllib.request,urllib.parse,sys,html
sys.path.insert(0,'.');from entries_src import E
UA={'User-Agent':'history-timeline-builder/1.0 (https://github.com/krielherman8-source/history-timeline)'}
def get(u):
  return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30))
def status(u):
  try: return urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30).status
  except Exception as e: return getattr(e,'code',0)
log=[];out=[]
def strip(s): return html.unescape(re.sub('<[^>]+>','',s or '')).strip()
for e in E:
  srcs=[]
  for s in e['src']:
    k,v=s.split(':',1)
    try:
      if k=='doi':
        if v=='10.1051/0004-6361/201833910':
          srcs.append(dict(title='Planck 2018 results. VI. Cosmological parameters',authors='Planck Collaboration (Aghanim, N. et al.)',year=2020,doi=v,type='paper'));continue
        m=get('https://api.crossref.org/works/'+urllib.parse.quote(v,safe='/'))['message']
        a=m.get('author',[]);au=(a[0].get('family','')+(', '+a[0]['given'][0]+'.' if a[0].get('given') else '')+(' et al.' if len(a)>1 else '')) if a else ''
        srcs.append(dict(title=re.sub(r'\s+',' ',strip(m['title'][0])),authors=au,year=m['issued']['date-parts'][0][0],doi=v,type='paper'))
      elif k=='wiki':
        j=get('https://en.wikipedia.org/api/rest_v1/page/summary/'+urllib.parse.quote(v))
        srcs.append(dict(title='Wikipedia: '+j['title'],url=j['content_urls']['desktop']['page'],type='encyclopedia'))
      else:
        u,t,ty=v.split('|');c=status(u)
        if c==200: srcs.append(dict(title=t,url=u,type=ty))
        else: log.append(f"{e['id']}: url {u} -> {c}, dropped")
    except Exception as ex: log.append(f"{e['id']}: {s} FAILED {ex}")
  media=[]
  if e.get('img'):
    try:
      p=get('https://en.wikipedia.org/w/api.php?action=query&format=json&prop=pageimages&piprop=name&redirects=1&titles='+urllib.parse.quote(e['img']))
      pg=list(p['query']['pages'].values())[0];fn=pg.get('pageimage')
      if fn:
        q=get('https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=url|extmetadata&iiurlwidth=400&titles='+urllib.parse.quote('File:'+fn))
        ii=list(q['query']['pages'].values())[0].get('imageinfo')
        if ii:
          ii=ii[0];md=ii['extmetadata'];lic=md.get('LicenseShortName',{}).get('value','')
          free=re.search(r'(CC|Public domain|PD|GFDL|CC0)',lic,re.I) and not re.search('fair use|non-free',lic,re.I)
          if free:
            media.append(dict(type='image',url=ii['thumburl'],page=ii['descriptionurl'],author=strip(md.get('Artist',{}).get('value',''))[:120] or 'Unknown',license=lic,title=fn))
          else: log.append(f"{e['id']}: image {fn} licence '{lic}' not free, skipped")
        else: log.append(f"{e['id']}: image {fn} not on Commons (local/non-free), skipped")
      else: log.append(f"{e['id']}: no page image")
    except Exception as ex: log.append(f"{e['id']}: image FAILED {ex}")
  o=dict(id=e['id'],title=e['title'],lane=e['lane'],status=e['status'],priority=e['priority'],start=e['start'],end=e.get('end'))
  if e.get('dateNote'): o['dateNote']=e['dateNote']
  o.update(evidenceTypes=e['ev'],mainstream=e['main'],alternatives=[dict(label=a,text=b) for a,b in e['alts']])
  if e.get('changed'): o['changed']=e['changed']
  o['sources']=srcs;o['media']=media;out.append(o)
json.dump(dict(version=2,entries=out),open('entries.json','w'),ensure_ascii=False,indent=1)
print('\n'.join(log));print(len(out),'entries')
