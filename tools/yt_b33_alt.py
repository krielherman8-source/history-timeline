import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile','History Hit','English Heritage','Historic England','Science History Institute','Archaeology Magazine']
Q={'nevali-cori': 'Nevali Cori History Hit', 'durrington-walls': 'Durrington Walls English Heritage', 'talheim-death-pit': 'Neolithic massacre Talheim PBS Eons', 'ness-of-brodgar': 'Ness of Brodgar History Hit', 'yamnaya-steppe': 'Yamnaya PBS Eons', 'dholavira': 'Dholavira UNESCO', 'watson-brake': 'Watson Brake oldest mounds', 'boudican-revolt': 'Boudica History Hit', 'hadrians-wall': "Hadrian's Wall English Heritage", 'vindolanda-tablets': 'Vindolanda tablets British Museum', 'plague-of-cyprian': 'Plague of Cyprian Rome pandemic', 'cai-lun-paper': 'history of paper TED-Ed', 'council-of-nicaea': 'Council of Nicaea Crash Course', 'thomas-in-india': 'Thomas apostle India BBC', 'lady-of-cao': 'Lady of Cao National Geographic', 'attila-the-hun': 'Attila the Hun TED-Ed', 'sack-of-rome-410': 'Fall of Rome 410 History Hit', 'georgia-guidestones': 'Georgia Guidestones destroyed news', 'dogu-figurines': 'dogu Jomon Tokyo National Museum', 'polywater': 'polywater Science History Institute', 'planet-vulcan': 'planet Vulcan Einstein PBS', 'men-in-black': 'men in black UFO folklore', 'owlman-1976': 'Owlman Mawnan', 'aswang': 'aswang folklore documentary', 'tikbalang': 'Philippine mythology tikbalang', 'kruger-millions': 'Kruger millions treasure', 'lost-city-kalahari': 'Lost City Kalahari Farini', 'daedalus-sea-serpent': 'sea serpent sightings history oarfish', 'simon-magus': 'Simon Magus early Christianity', 'apollonius-of-tyana': 'Apollonius of Tyana Jesus', 'montauk-project': 'Camp Hero Montauk conspiracy', 'heitsi-eibib': 'Khoikhoi Khoekhoe history', 'banpo': 'Banpo Xian museum', 'taosi-observatory': 'ancient Chinese astronomy observatory'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b33alt_candidates.json')) if retry and os.path.exists('videos_b33alt_candidates.json') else {}
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
  json.dump(candidates,open('videos_b33alt_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b33alt_candidates.json','w'),ensure_ascii=False,indent=1)
