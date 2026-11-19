import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'magna-carta-1215': 'Magna Carta history explained', 'ninety-five-theses-1517': 'Martin Luther 95 theses Reformation', 'magellan-elcano-1519': 'Magellan circumnavigation history', 'french-revolution-1789': 'French Revolution explained', 'watt-steam-engine': 'James Watt steam engine Industrial Revolution', 'meiji-restoration-1868': 'Meiji Restoration history', 'einstein-1905': 'Einstein 1905 miracle year', 'salt-march-1930': 'Gandhi Salt March', 'partition-of-india-1947': 'Partition of India 1947', 'berlin-wall-1989': 'fall of the Berlin Wall 1989', 'end-of-apartheid-1994': 'end of apartheid 1994 election Mandela', 'thor-mjolnir': 'Thor Norse mythology hammer', 'loki-bound': 'Loki Norse mythology punishment', 'weighing-of-the-heart': 'weighing of the heart Book of the Dead', 'kalki': 'Kalki avatar Vishnu', 'jonah-great-fish': 'Jonah and the whale story', 'momotaro': 'Momotaro peach boy', 'glooscap': 'Glooscap legend', 'spider-grandmother': 'Spider Woman Navajo weaving', 'pachamama': 'Pachamama Andes offering', 'coatlicue': 'Coatlicue Aztec statue', 'mwindo-epic': 'Mwindo epic Congo', 'nanabozho': 'Nanabozho Turtle Island story', 'patience-worth': 'Patience Worth Pearl Curran', 'amelia-earhart-1937': 'Amelia Earhart disappearance', 'hindenburg-1937': 'Hindenburg disaster 1937', 'san-francisco-1906': '1906 San Francisco earthquake', 'mount-st-helens-1980': 'Mount St Helens 1980 eruption', 'db-cooper-1971': 'D. B. Cooper hijacking', 'black-shuck-1577': 'Black Shuck legend', 'lusitania-1915': 'sinking of the Lusitania', 'zodiac-killer': 'Zodiac 340 cipher solved', 'jack-the-ripper-1888': 'Jack the Ripper history'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b32_candidates.json')) if retry and os.path.exists('videos_b32_candidates.json') else {}
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
  json.dump(candidates,open('videos_b32_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b32_candidates.json','w'),ensure_ascii=False,indent=1)
