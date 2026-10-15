import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video']
Q={
'great-zimbabwe':'Great Zimbabwe Fall of Civilizations',
'mapungubwe':'Mapungubwe kingdom National Geographic',
'aksum':'Kingdom of Aksum History Time',
'mansa-musa':'Mansa Musa TED-Ed',
'benin-bronzes':'Benin Bronzes British Museum',
'blombos':'Blombos Cave PBS Eons',
'laetoli':'Laetoli footprints PBS Eons',
'jomon-pottery':'Jomon pottery Japan National Geographic',
'sanxingdui':'Sanxingdui China National Geographic',
'angkor':'Angkor Wat Fall of Civilizations',
'nan-madol':'Nan Madol Micronesia',
'rapa-nui-moai':'Easter Island moai TED-Ed',
'lapita':'Lapita culture Polynesia',
'cahokia':'Cahokia mounds Fall of Civilizations',
'teotihuacan':'Teotihuacan Fall of Civilizations',
'olmec-heads':'Olmec civilization National Geographic',
'caral':'Caral Peru oldest city',
'monte-verde':'Monte Verde peopling Americas PBS',
'wilusa':'Troy Wilusa Hittite Fall of Civilizations',
'meroe':'Nubian pyramids Meroe National Geographic',
}
candidates={}
for k,q in Q.items():
  try:
    h=urllib.request.urlopen(urllib.request.Request('https://www.youtube.com/results?search_query='+urllib.parse.quote(q),headers={'User-Agent':'Mozilla/5.0','Accept-Language':'en'}),timeout=30).read().decode()
  except Exception as e:
    print(k,'SEARCH FAIL',e); continue
  ids=list(dict.fromkeys(re.findall(r'"videoId":"([\w-]{11})"',h)))[:10]
  hits=[]
  for i in ids:
    try: o=json.load(urllib.request.urlopen('https://www.youtube.com/oembed?format=json&url='+urllib.parse.quote('https://www.youtube.com/watch?v='+i),timeout=20))
    except Exception: continue
    if any(o['author_name'].lower()==a.lower() or o['author_name'].lower().startswith(a.lower()) for a in OK):
      hits.append(dict(type='video',url='https://www.youtube.com/watch?v='+i,title=o['title'],channel=o['author_name']))
  candidates[k]=hits
  print(k, '->', [(h['channel'], h['title'][:70]) for h in hits[:3]] or 'NONE')
json.dump(candidates,open('videos_b3_candidates.json','w'),ensure_ascii=False,indent=1)
