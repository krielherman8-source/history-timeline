import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'penicillin-1928': 'discovery of penicillin Fleming', 'smallpox-eradication': 'smallpox eradication history', 'mendel-peas': 'Gregor Mendel peas genetics', 'expanding-universe-1929': 'Hubble expanding universe discovery', 'pulsars-lgm-1967': 'Jocelyn Bell Burnell pulsar discovery', 'vera-rubin-dark-matter': 'Vera Rubin dark matter', 'first-exoplanet-1995': '51 Pegasi b first exoplanet', 'human-genome-2003': 'Human Genome Project', 'indian-ocean-tsunami-2004': '2004 Indian Ocean tsunami', 'tohoku-2011': '2011 Japan tsunami Fukushima', 'halifax-explosion-1917': 'Halifax Explosion 1917', 'hyksos': 'Hyksos Egypt', 'enheduanna': 'Enheduanna first author', 'confucius': 'Confucius philosophy', 'laozi-daodejing': 'Laozi Taoism', 'the-buddha': 'life of the Buddha history', 'pythagoras': 'Pythagoras history', 'aristarchus-heliocentrism': 'Aristarchus heliocentric', 'emerald-tablet': 'Emerald Tablet Hermes Trismegistus', 'zhang-qian': 'Zhang Qian Silk Road', 'lindow-man': 'Lindow Man bog body', 'maeshowe': 'Maeshowe Orkney', 'agartha': 'Agartha hollow earth', 'bell-witch': 'Bell Witch legend', 'persian-princess-2000': 'Persian princess mummy fake', 'guadalupe-1531': 'Our Lady of Guadalupe history', 'lourdes-1858': 'Lourdes Bernadette history', 'platypus-1799': 'platypus hoax specimen', 'komodo-dragon-1910': 'Komodo dragon', 'wollemi-pine-1994': 'Wollemi pine', 'moshoeshoe-thaba-bosiu': 'Moshoeshoe Thaba Bosiu', 'kaggen-mantis': 'San rock art mantis Kaggen', 'molasses-flood-1919': 'Great Molasses Flood'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b30_candidates.json')) if retry and os.path.exists('videos_b30_candidates.json') else {}
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
  json.dump(candidates,open('videos_b30_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b30_candidates.json','w'),ensure_ascii=False,indent=1)
