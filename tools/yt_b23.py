import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'alexander-the-great': 'Alexander the Great documentary', 'eratosthenes-earth': 'Eratosthenes measured the Earth', 'thermopylae': 'Battle of Thermopylae history', 'mask-of-agamemnon': 'Mask of Agamemnon Schliemann Mycenae', 'sibylline-books': 'Sibylline Books Rome', 'caesars-comet': 'Caesar comet 44 BC', 'teutoburg-forest': 'Teutoburg Forest battle Kalkriese', 'ninth-legion': 'Ninth Legion disappearance', 'liqian-roman-legion': 'Liqian Roman legion China', 'hypatia': 'Hypatia of Alexandria', 'codex-gigas': "Codex Gigas Devil's Bible", 'rok-runestone': 'Rök runestone', 'lambton-worm': 'Lambton Worm legend', 'golem-of-prague': 'Golem of Prague legend', 'malleus-maleficarum': 'Malleus Maleficarum witch trials', 'bayeux-comet-1066': 'Bayeux Tapestry Halley comet', 'ibn-battuta': 'Ibn Battuta travels', 'hildegard-of-bingen': 'Hildegard of Bingen', 'melusine': 'Melusine legend', 'mandeville-travels': 'Travels of Sir John Mandeville', 'hanno-periplus': 'Hanno the Navigator Carthage', 'mutapa-ophir': 'Mutapa empire Zimbabwe', 'battle-of-adwa': 'Battle of Adwa 1896', 'heike-crabs': 'Heike crab samurai Sagan', 'ainu': 'Ainu people Hokkaido', 'peach-blossom-spring': 'Peach Blossom Spring Tao Yuanming', 'hampi-vijayanagara': 'Hampi Vijayanagara', 'monte-alban': 'Monte Alban Zapotec', 'pueblo-revolt': 'Pueblo Revolt 1680', 'fountain-of-youth': 'Ponce de Leon Fountain of Youth myth', 'oak-island': 'Oak Island money pit', 'beale-ciphers': 'Beale ciphers', 'symmes-hollow-earth': 'hollow earth theory Symmes', 'shaver-mystery': 'Shaver mystery deros', 'ley-lines': 'ley lines', 'velikovsky-worlds-in-collision': 'Velikovsky Worlds in Collision', 'versailles-time-slip-1901': 'Moberly Jourdain Versailles ghosts', 'princess-caraboo': 'Princess Caraboo', 'origin-of-species-1859': 'Darwin Origin of Species natural selection', 'miller-urey-1953': 'Miller Urey experiment'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b23_candidates.json')) if retry and os.path.exists('videos_b23_candidates.json') else {}
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
  json.dump(candidates,open('videos_b23_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b23_candidates.json','w'),ensure_ascii=False,indent=1)
