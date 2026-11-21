import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'kabwe-skull': 'Broken Hill skull Natural History Museum', 'sibudu-cave': 'Sibudu cave arrows Wits', 'red-deer-cave-people': 'Red Deer Cave people new species', 'calanais-stones': 'Callanish stones Historic Environment Scotland', 'egtved-girl': 'Egtved girl National Museum Denmark', 'mitanni-indo-aryan-gods': 'Mitanni History Time', 'croesus-lydian-coins': 'Croesus Lydia first coins British Museum', 'pazyryk-burials': 'Pazyryk Scythians British Museum', 'sri-maha-bodhi': 'Anuradhapura sacred city UNESCO', 'baekje-incense-burner': 'Baekje kingdom history', 'wu-zetian': 'Wu Zetian only female emperor of China', 'an-lushan-rebellion': 'An Lushan rebellion Tang dynasty history', 'charlemagne': 'Charlemagne Crash Course', 'huanchaquito-las-llamas': 'Chimu mass child sacrifice National Geographic', 'ten-lost-tribes': 'lost tribes of Israel documentary', 'lemba-ngoma': 'Lemba Jewish tribe Zimbabwe', 'city-of-ys': 'Ys sunken city Brittany legend', 'gumiho': 'kumiho fox spirit folklore', 'rakshasa': 'Ravana Ramayana explained', 'billy-meier': 'Billy Meier hoax', 'raelism': 'Rael UFO religion', 'heavens-gate-1997': "Heaven's Gate mass suicide Hale-Bopp", 'die-glocke': 'Nazi Bell wunderwaffe myth', 'kuchisake-onna': 'slit mouthed woman Japan', 'curupira': 'Curupira Brazil folklore', 'dulce-base': 'Paul Bennewitz Project Beta', 'vril-coming-race': 'Vril society myth', 'zerzura': 'Gilf Kebir Almasy Cave of Swimmers', 'sodder-children': 'Sodder children mystery'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b34alt_candidates.json')) if retry and os.path.exists('videos_b34alt_candidates.json') else {}
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
  json.dump(candidates,open('videos_b34alt_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b34alt_candidates.json','w'),ensure_ascii=False,indent=1)
