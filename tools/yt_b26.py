import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'laki-1783': 'Laki eruption 1783', 'event-8200': '8.2 kiloyear event Lake Agassiz', 'armero-1985': 'Armero tragedy Nevado del Ruiz', 'messina-1908': '1908 Messina earthquake', 'kanto-1923': 'Great Kanto earthquake 1923', 'tangshan-1976': 'Tangshan earthquake 1976', 'smong-2004': 'Simeulue smong tsunami', 'samalas-1257': 'Samalas 1257 eruption', 'huaynaputina-1600': 'Huaynaputina eruption 1600', 'cocoliztli-1545': 'cocoliztli epidemic', 'shimao': 'Shimao ancient city China', 'hohokam': 'Hohokam canals', 'marajoara': 'Marajoara culture', 'nuragic-sardinia': 'Nuragic civilization Sardinia', 'mont-e-prama': 'Giants of Mont e Prama', 'talaiotic-menorca': 'Talayotic Menorca', 'elam': 'Elam ancient civilization', 'magan': 'Magan Umm an-Nar Oman', 'akrotiri': 'Akrotiri Santorini', 'ubaid-lizard-figurines': 'Ubaid lizard figurines', 'vilas-boas-1957': 'Antonio Vilas Boas abduction', 'brown-mountain-lights': 'Brown Mountain lights', 'marfa-lights': 'Marfa lights', 'geipan': 'GEIPAN UFO France', 'project-condign': 'Project Condign UFO report', 'cometa-report': 'COMETA report UFO', 'drake-equation': 'Drake equation', 'trindade-1958': 'Trindade island UFO 1958', 'mcminnville-1950': 'McMinnville UFO photos', 'battle-of-los-angeles': 'Battle of Los Angeles 1942', 'lead-masks-1966': 'lead masks case Brazil', 'protocols-elders-zion': 'Protocols of the Elders of Zion forgery', 'ossian': 'Ossian Macpherson', 'ern-malley': 'Ern Malley hoax', 'drakes-plate-of-brass': 'Drake plate of brass hoax', 'michigan-relics': 'Michigan relics hoax', 'los-lunas-stone': 'Los Lunas Decalogue Stone', 'davenport-tablets': 'Davenport tablets', 'bat-creek-stone': 'Bat Creek stone', 'tichborne-claimant': 'Tichborne claimant', 'grave-creek-stone': 'Grave Creek Mound'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b26_candidates.json')) if retry and os.path.exists('videos_b26_candidates.json') else {}
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
  json.dump(candidates,open('videos_b26_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b26_candidates.json','w'),ensure_ascii=False,indent=1)
