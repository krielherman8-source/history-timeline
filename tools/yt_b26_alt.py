import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'drake-equation': 'Drake equation PBS Space Time', 'event-8200': '8200 years ago climate event PBS Eons', 'messina-1908': 'Messina earthquake 1908 history', 'tangshan-1976': 'Tangshan earthquake documentary', 'smong-2004': '2004 tsunami oral tradition saved island', 'marfa-lights': 'Marfa lights mystery Texas', 'brown-mountain-lights': 'Brown Mountain lights North Carolina mystery', 'battle-of-los-angeles': 'Battle of Los Angeles 1942 air raid', 'protocols-elders-zion': 'Protocols of the Elders of Zion Holocaust Museum', 'hohokam': 'Hohokam Phoenix canals PBS', 'nuragic-sardinia': 'nuraghe Sardinia Bronze Age history', 'akrotiri': 'Akrotiri frescoes', 'huaynaputina-1600': 'Huaynaputina volcano Russian famine', 'tichborne-claimant': 'Tichborne claimant BBC', 'ossian': 'Ossian poems Macpherson BBC', 'marajoara': 'Marajo island ancient Amazon', 'shimao': 'Shimao pyramid China archaeology', 'samalas-1257': '1257 eruption Samalas Lombok', 'mcminnville-1950': 'McMinnville UFO photograph', 'geipan': 'France UFO investigation CNES', 'project-condign': 'Ministry of Defence UFO files released', 'drakes-plate-of-brass': 'Drake Plate of Brass Bancroft', 'michigan-relics': 'Michigan relics hoax', 'elam': 'Elamite civilization history'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b26alt_candidates.json')) if retry and os.path.exists('videos_b26alt_candidates.json') else {}
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
  json.dump(candidates,open('videos_b26alt_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b26alt_candidates.json','w'),ensure_ascii=False,indent=1)
