import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'early-stromatolites': 'stromatolites PBS Eons', 'mitochondrial-eve': 'mitochondrial Eve explained SciShow', 'mrs-ples': 'Cradle of Humankind Sterkfontein fossils', 'fall-of-nineveh': 'Nineveh Fall of Civilizations Assyria', 'siloam-tunnel': 'Hezekiah tunnel Jerusalem archaeology', 'lilith': 'Lilith TED-Ed', 'battle-of-marathon': 'Marathon 490 BC battle documentary', 'battle-of-salamis': 'Salamis 480 BC naval battle', 'tale-of-genji': 'Tale of Genji Murasaki Shikibu TED-Ed', 'grand-canal-china': 'Grand Canal China UNESCO', 'tengu': 'tengu yokai', 'treaty-of-waitangi': 'Te Tiriti o Waitangi explained', 'isandlwana-1879': 'Isandlwana 1879 Zulu War', 'yggdrasil': 'Norse cosmology nine worlds TED-Ed', 'max-headroom-1987': 'Max Headroom broadcast intrusion 1987 Chicago', 'kryptos': 'Kryptos K4 code', 'grusch-hearing-2023': 'UAP hearing Congress 2023 Grusch Fravor Graves', 'red-sprites': 'sprites jets elves upper atmosphere lightning', 'mpemba-effect': 'does hot water freeze faster than cold', 'sailing-stones': 'sailing stones mystery solved', 'klerksdorp-spheres': 'Klerksdorp spheres concretions'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b29alt_candidates.json')) if retry and os.path.exists('videos_b29alt_candidates.json') else {}
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
  json.dump(candidates,open('videos_b29alt_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b29alt_candidates.json','w'),ensure_ascii=False,indent=1)
