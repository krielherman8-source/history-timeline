import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'yeha-temple': 'Yeha Ethiopia temple documentary', 'fasil-ghebbi': 'Fasil Ghebbi Gondar UNESCO', 'makuria-faras': 'Faras cathedral Nubia paintings museum', 'queen-gudit': 'Aksum fall history documentary', 'famadihana': 'famadihana Madagascar BBC', 'hagia-sophia': 'Hagia Sophia Smarthistory', 'fall-of-constantinople': 'fall of Constantinople 1453 TED-Ed', 'nika-riots': 'Nika riots Constantinople history', 'karakorum': 'Karakorum Mongolia ancient capital', 'malta-boy': 'ancient Siberian genome Native American ancestry', 'orkhon-inscriptions': 'Orkhon Valley UNESCO', 'patomskiy-crater': 'Patom crater mystery', 'andree-balloon': 'Andrée balloon expedition Svalbard', 'royal-cemetery-ur': 'Royal tombs of Ur Smarthistory', 'kanesh-archives': 'Old Assyrian merchants Kanesh', 'poverty-point': 'Poverty Point UNESCO', 'walam-olum': 'Walam Olum', 'sky-woman': 'Sky Woman Iroquois creation myth', 'newark-earthworks': 'Hopewell Ceremonial Earthworks UNESCO', 'nemrut-dag': 'Nemrut Dag UNESCO', 'jack-hills-zircons': 'oldest zircon Jack Hills 4.4 billion', 'prambanan': 'Prambanan UNESCO', 'battle-of-mactan': 'Lapulapu Magellan Mactan 1521', 'pink-face-atapuerca': 'Atapuerca oldest face Europe 2025', 'mantell-1948': 'Thomas Mantell UFO', 'pascagoula-1973': 'Pascagoula UFO Hickson Parker', 'travis-walton-1975': 'Travis Walton Fire in the Sky', 'ohare-2006': 'O Hare airport UFO 2006', 'ogopogo': 'Ogopogo', 'dover-demon': 'Dover Demon cryptid', 'calaveras-skull': 'Calaveras skull', 'kinderhook-plates': 'Kinderhook plates Joseph Smith'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b21_candidates.json')) if retry and os.path.exists('videos_b21_candidates.json') else {}
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
  json.dump(candidates,open('videos_b21_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b21_candidates.json','w'),ensure_ascii=False,indent=1)
