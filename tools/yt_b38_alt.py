import re,json,urllib.request,urllib.parse
OK=['Vox','DW News','Radio Free Europe/Radio Liberty','The Royal Society','Royal Society of Chemistry','Science History Institute','Lyme Regis Museum','Arirang TV','KBS WORLD TV','Asian Civilisations Museum','Natural History Museum of Denmark','National Museum of Denmark','The Economist','NBC News','CBS News','Associated Press','Reuters','Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'thousand-and-one-nights': 'One Thousand and One Nights history Scheherazade', 'al-biruni-earth-radius': 'al-Biruni measure the Earth radius', 'al-jazari-automata': 'al-Jazari elephant clock automata', 'sack-of-baghdad-1258': 'Mongol siege of Baghdad 1258', 'isra-and-miraj': 'Isra and Miraj night journey art', 'year-of-the-elephant': 'Abraha Year of the Elephant Mecca', 'al-hakim-disappearance': 'al-Hakim Fatimid caliph', 'zahhak-serpent-king': 'Zahhak Shahnameh serpent king', 'tusi-couple-maragheh': 'Tusi couple Copernicus', 'michizane-tenjin': 'Sugawara no Michizane Tenjin', 'abe-no-seimei': 'Abe no Seimei onmyoji', 'okiku-plate-mansion': 'Okiku Banchō Sarayashiki ghost', 'shimabara-rebellion': 'Shimabara Rebellion 1637', 'ryukyu-kingdom': 'Ryukyu Kingdom history', 'heo-hwang-ok': 'Heo Hwang-ok Indian princess Korea', 'emille-bell': 'Emille Bell King Seongdeok', 'mimana-gaya-debate': 'Gaya confederacy Korea iron', 'thule-migration': 'Thule people Inuit migration', 'qilakitsoq-mummies': 'Qilakitsoq Greenland mummies', 'labynkyr-devil': 'Labynkyr lake monster', 'la-navidad-1492': 'La Navidad Columbus fort Haiti', 'tula-curacao-1795': 'Tula slave revolt Curacao 1795', 'nanny-of-the-maroons': 'Nanny of the Maroons Jamaica', 'white-witch-rose-hall': 'Rose Hall White Witch Annie Palmer', 'laperouse-vanikoro': 'Laperouse expedition Vanikoro shipwreck', 'tui-tonga-maritime-empire': 'Tui Tonga empire history', 'marcahuasi-stone-forest': 'Marcahuasi stone forest', 'vilcabamba-last-inca': 'Vilcabamba last Inca stronghold', 'lavoisier-oxygen': 'Lavoisier oxygen phlogiston', 'neptune-discovery-1846': 'discovery of Neptune Le Verrier', 'galvani-frankenstein': 'Galvani frog legs Aldini Frankenstein', 'utah-monolith-2020': 'Utah monolith 2020'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b38alt_candidates.json')) if retry and os.path.exists('videos_b38alt_candidates.json') else {}
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
  json.dump(candidates,open('videos_b38alt_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b38alt_candidates.json','w'),ensure_ascii=False,indent=1)
