import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'newton-principia-1687': 'Isaac Newton Principia gravity', 'faraday-induction-1831': 'Michael Faraday electromagnetic induction', 'telegraph-1844': 'Samuel Morse telegraph history', 'broad-street-cholera-1854': 'John Snow cholera map Broad Street', 'pasteur-germ-theory': 'Louis Pasteur germ theory', 'roentgen-xrays-1895': 'discovery of X-rays Roentgen', 'curie-radioactivity': 'Marie Curie radioactivity', 'wright-flyer-1903': 'Wright brothers first flight', 'dna-double-helix-1953': 'Rosalind Franklin DNA double helix', 'arpanet-1969': 'ARPANET first message internet history', 'crispr-2012': 'CRISPR explained', 'enigma-bletchley': 'Enigma code breaking Bletchley Park', 'hiroshima-nagasaki-1945': 'Hiroshima atomic bomb history', 'gagarin-1961': 'Yuri Gagarin first man in space', 'cuban-missile-crisis-1962': 'Cuban Missile Crisis Arkhipov', 'apollo-13-1970': 'Apollo 13 explosion', 'petrov-1983': 'Stanislav Petrov 1983 false alarm', 'challenger-1986': 'Challenger disaster O-ring', 'hiv-aids': 'origin of HIV AIDS', 'covid-19-pandemic': 'COVID-19 pandemic explained', 'antonine-plague': 'Antonine Plague Rome', 'polio-vaccine-1955': 'Jonas Salk polio vaccine', 'orpheus-eurydice': 'myth of Orpheus and Eurydice', 'persephone-demeter': 'myth of Persephone', 'pandoras-jar': "myth of Pandora's box", 'labours-of-heracles': 'twelve labors of Hercules', 'odyssey-homer': 'the Odyssey Homer', 'daedalus-icarus': 'myth of Icarus and Daedalus', 'cassandra': 'myth of Cassandra', 'oedipus': 'myth of Oedipus', 'sisyphus': 'myth of Sisyphus', 'garden-of-eden': 'Garden of Eden location history', 'lake-fundudzi': 'Lake Fundudzi Venda'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b31_candidates.json')) if retry and os.path.exists('videos_b31_candidates.json') else {}
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
  json.dump(candidates,open('videos_b31_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b31_candidates.json','w'),ensure_ascii=False,indent=1)
