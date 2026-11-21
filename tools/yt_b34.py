import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'kabwe-skull': 'Kabwe Broken Hill skull', 'sibudu-cave': 'Sibudu Cave Middle Stone Age', 'lion-cavern-ngwenya': 'Ngwenya mine Eswatini oldest mine', 'nataruk-massacre': 'Nataruk massacre Turkana', 'red-deer-cave-people': 'Red Deer Cave people China', 'calanais-stones': 'Calanais standing stones Lewis', 'egtved-girl': 'Egtved Girl Bronze Age', 'mitanni-indo-aryan-gods': 'Mitanni kingdom history', 'gordion-midas': 'King Midas Gordion tomb', 'croesus-lydian-coins': 'first coins Lydia Croesus', 'pazyryk-burials': 'Pazyryk carpet frozen tombs', 'linear-b-decipherment': 'Linear B decipherment Ventris', 'sri-maha-bodhi': 'Sri Maha Bodhi tree Anuradhapura', 'baekje-incense-burner': 'Baekje gilt bronze incense burner', 'wu-zetian': 'Wu Zetian empress', 'an-lushan-rebellion': 'An Lushan rebellion', 'charlemagne': 'Charlemagne history', 'norse-greenland': 'Norse Greenland disappearance', 'huanchaquito-las-llamas': 'Huanchaquito child sacrifice Chimu', 'ten-lost-tribes': 'Ten Lost Tribes of Israel', 'lemba-ngoma': 'Lemba people DNA', 'city-of-ys': 'legend of Ys Brittany', 'zerzura': 'Zerzura lost oasis', 'gumiho': 'gumiho nine tailed fox Korea', 'adze-firefly-vampire': 'adze Ewe folklore', 'rakshasa': 'rakshasa mythology', 'sodder-children': 'Sodder children disappearance', 'billy-meier': 'Billy Meier UFO photos', 'raelism': 'Raelian movement', 'heavens-gate-1997': "Heaven's Gate cult 1997", 'aetherius-society': 'Aetherius Society', 'vril-coming-race': 'Vril The Coming Race Bulwer-Lytton', 'die-glocke': 'Die Glocke Nazi Bell', 'akakor-tatunca-nara': 'Akakor Tatunca Nara', 'kuchisake-onna': 'Kuchisake-onna legend', 'abiku-ogbanje': 'abiku ogbanje', 'curupira': 'Curupira legend Brazil', 'dulce-base': 'Dulce base Bennewitz'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b34_candidates.json')) if retry and os.path.exists('videos_b34_candidates.json') else {}
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
  json.dump(candidates,open('videos_b34_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b34_candidates.json','w'),ensure_ascii=False,indent=1)
