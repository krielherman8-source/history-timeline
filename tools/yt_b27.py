import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'chinchorro-mummies': 'Chinchorro mummies', 'ten-ten-vilu': 'Mapuche flood myth Trentren Kaikai', 'selknam-hain': 'Selknam Hain ceremony', 'caleuche': 'Caleuche ghost ship Chiloe', 'city-of-the-caesars': 'City of the Caesars Patagonia legend', 'cueva-de-las-manos': 'Cueva de las Manos', 'jemmy-button': 'Jemmy Button Fuegians Beagle', 'valdivia-1960': '1960 Valdivia earthquake', 'luison': 'Luison seventh son Argentina', 'mylodon-cave': 'Mylodon cave giant sloth Patagonia', 'patagonian-giants': 'Patagonian giants Magellan', 'nart-sagas': 'Nart sagas Caucasus', 'urartu': 'Urartu kingdom', 'vardzia': 'Vardzia cave city', 'gates-of-alexander': 'Gates of Alexander Gog Magog', 'khazar-conversion': 'Khazars Judaism conversion', 'oyo-empire': 'Oyo Empire', 'shango': 'Shango orisha', 'osun-osogbo': 'Osun Osogbo sacred grove', 'thunderstones': 'thunderstones prehistoric axes folklore', 'origin-of-death-myths': 'origin of death myths', 'hainuwele': 'Hainuwele myth', 'moon-rabbit': 'moon rabbit myth', 'ohalo-ii': 'Ohalo II', 'abu-hureyra': 'Abu Hureyra', 'guila-naquitz': 'teosinte maize domestication', 'dog-domestication': 'dog domestication origin', 'xianren-cave': 'oldest pottery Xianrendong', 'basque-witch-trials': 'Basque witch trials Zugarramurdi', 'north-berwick-witches': 'North Berwick witch trials', 'pendle-witches': 'Pendle witches', 'wurzburg-bamberg-witch-trials': 'Bamberg witch trials', 'vardo-witch-trials': 'Vardo witch trials Steilneset', 'torsaker-witch-trials': 'Torsaker witch trials', 'benandanti': 'benandanti night battles', 'voronezh-1989': 'Voronezh UFO 1989', 'ilkley-moor-1987': 'Ilkley Moor alien'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b27_candidates.json')) if retry and os.path.exists('videos_b27_candidates.json') else {}
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
  json.dump(candidates,open('videos_b27_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b27_candidates.json','w'),ensure_ascii=False,indent=1)
