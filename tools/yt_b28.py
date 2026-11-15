import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'rain-of-animals': 'raining animals fish frogs explained', 'kentucky-meat-shower': 'Kentucky meat shower 1876', 'spontaneous-human-combustion': 'spontaneous human combustion science', 'devils-sea': "Devil's Sea Dragon's Triangle", 'carroll-deering': 'Carroll A Deering ghost ship', 'baychimo': 'SS Baychimo ghost ship', 'victor-of-aveyron': 'Victor of Aveyron wild boy', 'hinterkaifeck': 'Hinterkaifeck murders', 'fiji-mermaid': 'Fiji mermaid Barnum', 'lakenheath-1956': 'Lakenheath Bentwaters 1956 UFO', 'exeter-1965': 'Exeter incident 1965 UFO', 'gulf-breeze-1987': 'Gulf Breeze UFO', 'leonids-1833': '1833 Leonid meteor storm', 'shoemaker-levy-9': 'Shoemaker-Levy 9 Jupiter impact', 'keplers-supernova': 'Kepler supernova 1604', 'spaghetti-tree': 'spaghetti harvest BBC 1957', 'cold-fusion-1989': 'cold fusion Pons Fleischmann', 'bantu-expansion': 'Bantu expansion', 'benin-walls': 'Walls of Benin', 'tula-toltecs': 'Toltecs Tula', 'el-mirador': 'El Mirador Maya', 'paquime': 'Paquime Casas Grandes', 'manco-capac': 'Inca origin myth Manco Capac', 'coyote-trickster': 'Coyote trickster Native American', 'cowherd-weaver-girl': 'Cowherd and Weaver Girl Qixi', 'garuda': 'Garuda myth', 'uruk': 'Uruk first city', 'merneptah-stele': 'Merneptah Stele Israel', 'dendera-zodiac': 'Dendera zodiac', 'hallstatt': 'Hallstatt salt mine prehistoric', 'amesbury-archer': 'Amesbury Archer', 'seahenge': 'Seahenge', 'lewis-chessmen': 'Lewis chessmen', 'cerne-abbas-giant': 'Cerne Abbas Giant dating', 'long-man-wilmington': 'Long Man of Wilmington', 'arthurs-grave-glastonbury': 'King Arthur grave Glastonbury'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b28_candidates.json')) if retry and os.path.exists('videos_b28_candidates.json') else {}
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
  json.dump(candidates,open('videos_b28_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b28_candidates.json','w'),ensure_ascii=False,indent=1)
