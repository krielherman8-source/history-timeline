import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'atrahasis': 'Atrahasis', 'colossus-of-rhodes': 'Colossus of Rhodes seven wonders', 'lighthouse-of-alexandria': 'Pharos lighthouse Alexandria history', 'galilee-boat': 'Jesus boat Galilee', 'minoan-snake-goddess': 'Minoan snake goddess forgery', 'cyclops-dwarf-elephants': 'cyclops myth elephant fossils', 'tall-el-hammam': 'Sodom airburst Tall el Hammam', 'ramayana': 'Ramayana story', 'change-moon-goddess': 'Chang e moon legend Mid-Autumn', 'shennong': 'Shennong', 'todaiji-great-buddha': 'Todaiji', 'ta-prohm-stegosaurus': 'Ta Prohm temple', 'hannibal-alps': 'Hannibal Alps elephants', 'mfecane': 'Shaka Zulu Mfecane history', 'tikal': 'Tikal Guatemala', 'sacred-cenote': 'Chichen Itza cenote', 'vlad-dracula': 'Vlad Dracula history', 'man-in-the-iron-mask': 'Iron Mask prisoner', 'nostradamus': 'Nostradamus', 'ball-lightning': 'ball lightning explained', 'enfield-poltergeist': 'Enfield haunting', 'lost-dutchman-mine': 'Lost Dutchman Superstition Mountains', 'mercy-brown': 'New England vampire panic'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b24_candidates.json'))
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
  json.dump(candidates,open('videos_b24_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b24_candidates.json','w'),ensure_ascii=False,indent=1)
