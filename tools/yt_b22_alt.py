import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'narmer-palette': 'Narmer Palette', 'tel-dan-stele': 'House of David inscription Tel Dan', 'natufian-culture': 'Natufian', 'battle-of-vienna-1683': 'Battle of Vienna 1683 winged hussars', 'devshirme-janissaries': 'Janissaries', 'naqsh-e-jahan': 'Isfahan Safavid', 'shah-ismail': 'Safavid Empire rise', 'kalinago-caribs': 'Kalinago people Caribbean', 'joya-de-ceren': 'Joya de Ceren UNESCO', 'inuksuk': 'Inuksuk meaning', 'potlatch-ban': 'potlatch', 'tabon-caves': 'Tabon Man Palawan', 'java-man': 'Java Man', 'toraja-funerals': 'Toraja death ritual', 'flannan-isles-1900': 'Flannan Isles', 'higgs-boson-2012': 'Higgs boson explained', 'champ-lake-champlain': 'Lake Champlain monster Champ', 'vinland-map': 'Vinland Map', 'mesha-stele': 'Moabite stone', 'ghost-rockets-1946': 'ghost rockets Scandinavia'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b22_candidates.json'))
for k,q in Q.items():
  if retry and candidates.get(k): continue
  try:
    h=urllib.request.urlopen(urllib.request.Request('https://www.youtube.com/results?search_query='+urllib.parse.quote(q),headers={'User-Agent':'Mozilla/5.0','Accept-Language':'en'}),timeout=30).read().decode()
  except Exception as e:
    print(k,'SEARCH FAIL',e); continue
  ids=list(dict.fromkeys(re.findall(r'"videoId":"([\w-]{11})"',h)))[:10]
  hits=[]
  for i in ids:
    try: o=json.load(urllib.request.urlopen('https://www.youtube.com/oembed?format=json&url='+urllib.parse.quote('https://www.youtube.com/watch?v='+i),timeout=20))
    except Exception: continue
    if any(o.get('author_name','').lower()==a.lower() or o.get('author_name','').lower().startswith(a.lower()) for a in OK):
      hits.append(dict(type='video',url='https://www.youtube.com/watch?v='+i,title=o['title'],channel=o['author_name']))
  candidates[k]=(candidates.get(k) or [])+hits
  print(k, '->', [(h['channel'], h['title'][:70]) for h in hits[:3]] or 'NONE', flush=True)
  json.dump(candidates,open('videos_b22_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b22_candidates.json','w'),ensure_ascii=False,indent=1)
