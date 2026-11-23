import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'burgess-shale': 'Burgess Shale Cambrian PBS Eons', 'archaeopteryx': 'Archaeopteryx feathered dinosaur bird evolution', 'florisbad-skull': 'Florisbad Homo sapiens origins Africa', 'bluefish-caves': 'Bluefish Caves first Americans', 'lonar-crater': 'Lonar lake meteorite crater India', 'sinauli-carts': 'Sanauli chariot burial', 'taxila': 'Taxila Gandhara Pakistan', 'brihadisvara-temple': 'Brihadisvara temple Chola Smarthistory', 'jatinga-birds': 'Jatinga birds Assam', 'lac-long-quan-au-co': 'Vietnamese origin myth dragon fairy', 'kuntilanak-pontianak': 'pontianak ghost Malaysia', 'bujang-valley': 'Lembah Bujang Kedah', 'mahendraparvata-lidar': 'lost city Cambodia lidar Angkor', 'spirit-cave-mummy': 'Spirit Cave mummy Nevada DNA', 'etowah-mounds': 'Etowah mounds Georgia', 'caracol-maya': 'Caracol Belize Maya', 'canudos-war': 'Canudos Brazil Conselheiro', 'fordlandia': 'Fordlandia', 'batavia-wreck-1629': 'Batavia shipwreck mutiny Abrolhos', 'leluh-kosrae': 'Kosrae Micronesia ruins', 'drop-bear': 'drop bears Australia', 'koumbi-saleh': 'Kumbi Saleh Ghana', 'khami-ruins': 'Khami Zimbabwe', 'thimlich-ohinga': 'Thimlich Ohinga Kenya', 'harar-hyenas': 'Harar hyena man Ethiopia', 'bambatha-rebellion': 'Bhambatha rebellion', 'maji-maji-rebellion': 'Maji Maji war Tanzania', 'mbuya-nehanda': 'Nehanda statue Zimbabwe'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b36alt_candidates.json')) if retry and os.path.exists('videos_b36alt_candidates.json') else {}
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
  json.dump(candidates,open('videos_b36alt_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b36alt_candidates.json','w'),ensure_ascii=False,indent=1)
