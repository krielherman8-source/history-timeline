import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'world-war-one': 'World War I Crash Course', 'september-11-attacks': '9/11 attacks documentary National Geographic', 'great-fire-of-london-1666': 'Great Fire of London BBC', 'tulip-mania-1637': 'tulip mania TED-Ed', 'first-opium-war': 'Opium Wars Crash Course', 'sakoku-closed-japan': 'Tokugawa Japan isolation Crash Course', 'cook-terra-australis-lono': 'James Cook voyage Pacific Smithsonian', 'richard-iii-car-park': 'Richard III skeleton found Leicester BBC', 'shanidar-flower-burial': 'Shanidar Z Neanderthal Cambridge', 'mau-mau-uprising': 'Mau Mau Kenya Al Jazeera', 'al-andalus-cordoba': 'Islamic Spain al-Andalus documentary', 'potosi-silver': 'Potosi Cerro Rico DW', 'defenestration-thirty-years-war': 'Thirty Years War Crash Course', 'xiongnu': 'Xiongnu nomads Han dynasty', 'angels-of-mons': 'Angels of Mons legend World War', 'south-sea-bubble-1720': 'South Sea Bubble history', 'north-sentinel-island': 'Sentinelese uncontacted tribe', 'simurgh': 'Conference of the Birds TED-Ed', 'great-trek-1836': 'Great Trek South Africa history', 'wandering-jew': 'Wandering Jew legend history', 'im1-interstellar-meteor': 'interstellar meteor Avi Loeb Pacific expedition', 'vix-grave': 'Vix krater', 'sogdian-merchants': 'Sogdians Silk Road'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b35alt_candidates.json')) if retry and os.path.exists('videos_b35alt_candidates.json') else {}
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
  json.dump(candidates,open('videos_b35alt_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b35alt_candidates.json','w'),ensure_ascii=False,indent=1)
