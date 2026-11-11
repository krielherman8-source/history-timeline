import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'atrahasis': 'Atrahasis flood epic', 'ishtar-gate': 'Ishtar Gate Babylon', 'rosetta-stone': 'Rosetta Stone decipherment', 'galilee-boat': 'Sea of Galilee boat ancient', 'colossus-of-rhodes': 'Colossus of Rhodes', 'lighthouse-of-alexandria': 'Lighthouse of Alexandria Pharos', 'minoan-snake-goddess': 'Minoan snake goddess', 'nimrud-lens': 'Nimrud lens', 'cyclops-dwarf-elephants': 'dwarf elephant cyclops skull', 'tall-el-hammam': 'Tall el-Hammam airburst', 'ramayana': 'Ramayana epic', 'change-moon-goddess': "Chang'e moon goddess", 'penglai': 'Penglai island immortals', 'shennong': 'Shennong divine farmer', 'yamato-takeru': 'Yamato Takeru', 'ajanta-caves': 'Ajanta caves', 'todaiji-great-buddha': 'Todaiji Great Buddha Nara', 'priest-king-mohenjo-daro': 'Mohenjo-daro priest king', 'ta-prohm-stegosaurus': 'Ta Prohm stegosaurus', 'chola-srivijaya-1025': 'Chola navy Srivijaya', 'hannibal-alps': 'Hannibal crossing the Alps', 'impundulu': 'lightning bird impundulu', 'mfecane': 'Mfecane', 'thulamela': 'Thulamela Kruger', 'tikal': 'Tikal Maya', 'sacred-cenote': 'Chichen Itza sacred cenote', 'lost-dutchman-mine': 'Lost Dutchman mine', 'vlad-dracula': 'Vlad the Impaler', 'mercy-brown': 'Mercy Brown vampire', 'man-in-the-iron-mask': 'Man in the Iron Mask', 'princes-in-the-tower': 'Princes in the Tower', 'nostradamus': 'Nostradamus prophecies', 'rasputin-death': 'death of Rasputin', 'ball-lightning': 'ball lightning', 'coso-artifact': 'Coso artifact spark plug', 'aurora-texas-1897': 'Aurora Texas 1897 UFO', 'gef-talking-mongoose': 'Gef talking mongoose', 'enfield-poltergeist': 'Enfield poltergeist', 'ourang-medan': 'Ourang Medan', 'radiocarbon-dating-1949': 'radiocarbon dating how it works'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b24_candidates.json')) if retry and os.path.exists('videos_b24_candidates.json') else {}
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
