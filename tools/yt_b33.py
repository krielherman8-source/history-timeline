import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'nevali-cori': 'Nevali Cori Neolithic temple', 'durrington-walls': 'Durrington Walls Stonehenge', 'banpo': 'Banpo Neolithic village Yangshao', 'talheim-death-pit': 'Talheim death pit Neolithic massacre', 'ness-of-brodgar': 'Ness of Brodgar Orkney', 'yamnaya-steppe': 'Yamnaya steppe migration Indo-European', 'taosi-observatory': 'Taosi observatory China', 'dholavira': 'Dholavira Harappan city', 'watson-brake': 'Watson Brake mounds Louisiana', 'boudican-revolt': 'Boudica revolt Romans', 'hadrians-wall': "Hadrian's Wall history", 'vindolanda-tablets': 'Vindolanda tablets', 'plague-of-cyprian': 'Plague of Cyprian', 'cai-lun-paper': 'invention of paper Cai Lun', 'council-of-nicaea': 'Council of Nicaea', 'apollonius-of-tyana': 'Apollonius of Tyana', 'simon-magus': 'Simon Magus', 'thomas-in-india': 'St Thomas Christians India', 'lady-of-cao': 'Lady of Cao Moche', 'attila-the-hun': 'Attila the Hun', 'sack-of-rome-410': 'sack of Rome 410 Alaric', 'georgia-guidestones': 'Georgia Guidestones', 'montauk-project': 'Montauk Project Camp Hero', 'dogu-figurines': 'Jomon dogu figurines', 'polywater': 'polywater', 'planet-vulcan': 'planet Vulcan Mercury Einstein', 'nibiru-cataclysm': 'Nibiru Planet X NASA', 'y2k-bug': 'Y2K bug', 'owlman-1976': 'Owlman Cornwall', 'men-in-black': 'Men in Black UFO history', 'slender-man': 'Slender Man internet legend', 'heitsi-eibib': 'Khoikhoi mythology', 'lost-city-kalahari': 'Lost City of the Kalahari', 'kruger-millions': 'Kruger Millions gold', 'daedalus-sea-serpent': 'HMS Daedalus sea serpent', 'aswang': 'aswang Philippine folklore', 'tikbalang': 'tikbalang'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b33_candidates.json')) if retry and os.path.exists('videos_b33_candidates.json') else {}
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
  json.dump(candidates,open('videos_b33_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b33_candidates.json','w'),ensure_ascii=False,indent=1)
