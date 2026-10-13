import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video']
Q={'big-bang':'PBS Space Time big bang','kpg':'PBS Eons asteroid dinosaurs extinction','younger-dryas':'Younger Dryas impact hypothesis PBS','gobekli-tepe':'Gobekli Tepe documentary','gilgamesh':'British Museum flood tablet Irving Finkel','troy':'Fall of Civilizations Bronze Age collapse','bronze-collapse':'Fall of Civilizations Bronze Age collapse','atlantis':'TED-Ed Atlantis','piltdown':'Piltdown man hoax','antikythera':'Antikythera mechanism Nature video','neanderthal-dna':'PBS Eons Denisovans','great-pyramid':'how were the pyramids built TED-Ed','plate-tectonics':'Crash Course plate tectonics','toba':'PBS Eons Toba'}
res={}
for k,q in Q.items():
  h=urllib.request.urlopen(urllib.request.Request('https://www.youtube.com/results?search_query='+urllib.parse.quote(q),headers={'User-Agent':'Mozilla/5.0','Accept-Language':'en'}),timeout=30).read().decode()
  ids=list(dict.fromkeys(re.findall(r'"videoId":"([\w-]{11})"',h)))[:8]
  for i in ids:
    try: o=json.load(urllib.request.urlopen('https://www.youtube.com/oembed?format=json&url='+urllib.parse.quote('https://www.youtube.com/watch?v='+i),timeout=20))
    except Exception: continue
    if any(o['author_name'].lower()==a.lower() or o['author_name'].lower().startswith(a.lower()) for a in OK):
      res[k]=dict(type='video',url='https://www.youtube.com/watch?v='+i,title=o['title'],channel=o['author_name']);break
  print(k,res.get(k))
json.dump(res,open('videos.json','w'),ensure_ascii=False,indent=1)
