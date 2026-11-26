import re,json,urllib.request,urllib.parse
OK=['Vox','DW News','Radio Free Europe/Radio Liberty','The Royal Society','Royal Society of Chemistry','Science History Institute','Lyme Regis Museum','Arirang TV','KBS WORLD TV','Asian Civilisations Museum','Natural History Museum of Denmark','National Museum of Denmark','The Economist','NBC News','CBS News','Associated Press','Reuters','Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'moctezuma-headdress': 'Moctezuma headdress Vienna', 'la-malinche': 'La Malinche Malintzin', 'dresden-codex': 'Dresden Codex Maya', 'calakmul-snake-kingdom': 'Calakmul Snake Kingdom Maya', 'yaxchilan-lady-xoc': 'Yaxchilan Lintel 24 Lady Xoc', 'tlaloc-rain-god': 'Tlaloc Aztec rain god', 'baiame-sky-father': 'Baiame creation Aboriginal', 'tiddalik-frog': 'Tiddalik the frog', 'kow-swamp-burials': 'Kow Swamp skulls', 'wilgie-mia-ochre-mine': 'Wilgie Mia ochre mine', 'gympie-pyramid': 'Gympie pyramid', 'marree-man-1998': 'Marree Man geoglyph', 'knowles-nullarbor-1988': 'Knowles family Nullarbor UFO 1988', 'arioi-and-oro': 'Arioi Tahiti Oro', 'burning-of-books-213bce': 'burning of books burying of scholars Qin', 'hua-mulan': 'Ballad of Mulan history', 'boxer-rebellion': 'Boxer Rebellion', 'red-cliffs-208': 'Battle of Red Cliffs', 'fuxi-bagua': 'Leibniz binary I Ching', 'silk-secret-smuggled': 'silkworm smuggling Justinian monks silk', 'sima-qian-shiji': 'Sima Qian Records of the Grand Historian', 'merv-1221': 'Merv Mongol 1221', 'nabonidus-first-archaeologist': 'Nabonidus first archaeologist', 'behemoth-and-leviathan': 'Behemoth and Leviathan', 'uppsala-temple': 'Temple at Uppsala', 'minnesota-iceman': 'Minnesota Iceman', 'stargate-remote-viewing': 'Stargate project remote viewing', 'tiara-of-saitaphernes': 'Tiara of Saitaphernes Louvre fake', 'palomares-1966': 'Palomares 1966 H-bomb'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b39alt_candidates.json')) if retry and os.path.exists('videos_b39alt_candidates.json') else {}
import itertools
QQ=[(k,q+' '+suf) for k,q in Q.items() for suf in ['BBC','TED-Ed documentary']]
for k,q in QQ:
  pass
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
  json.dump(candidates,open('videos_b39alt_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b39alt_candidates.json','w'),ensure_ascii=False,indent=1)
