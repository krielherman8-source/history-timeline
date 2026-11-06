import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={
'anak-tomb':'Goguryeo tomb murals UNESCO','seokguram':'Seokguram Grotto Gyeongju UNESCO','hunminjeongeum':'Hangul King Sejong TED-Ed','dokkaebi':'dokkaebi Korean goblin folklore','korean-shamanism':'Korean shamanism mudang','silla-gold-crowns':'Silla gold crown Gyeongju','balhae':'Balhae Parhae kingdom','koryo-celadon':'Goryeo celadon pottery','jeju-samseong':'Jeju Samseonghyeol','hwandan-gogi':'Hwandan Gogi Korea',
'potala-palace':'Potala Palace Lhasa UNESCO','bon-religion':'Bon religion Tibet','mustang-caves':'Mustang sky caves Nepal','paro-taktsang':'Paro Taktsang Tiger Nest Bhutan','guge-kingdom':'Guge kingdom Tibet ruins','padmasambhava':'Padmasambhava Guru Rinpoche','thang-tong-gyalpo':'Thang Tong Gyalpo iron bridge','druk-thunder-dragon':'Bhutan thunder dragon Druk','malla-kathmandu':'Malla dynasty Kathmandu Durbar','kumari-nepal':'Kumari living goddess Nepal',
'rus-baptism':'Christianization of Kievan Rus 988','firebird':'Firebird Slavic folklore','koschei':'Koschei the Deathless','vinca-symbols':'Vinca symbols Neolithic','battle-of-kosovo':'Battle of Kosovo 1389','bogomils':'Bogomils medieval heresy','painted-monasteries-bucovina':'Painted monasteries Bucovina UNESCO','thracian-kings':'Valley of the Thracian Kings','cyril-methodius':'Cyril and Methodius Slavic alphabet','amber-room':'Amber Room Catherine Palace',
'falcon-lake-1967':'Falcon Lake UFO Michalak','solway-spaceman':'Solway Firth Spaceman photograph','jwst-early-galaxies':'JWST early galaxies NASA','schweitzer-dino-soft-tissue':'dinosaur soft tissue Schweitzer','kelly-hopkinsville':'Kelly Hopkinsville goblin encounter','karahan-tepe':'Karahan Tepe archaeology','wolfsegg-iron':'Wolfsegg Iron Salzburg cube','burrows-cave':'Burrows Cave hoax','kecksburg-ufo':'Kecksburg UFO 1965','london-hammer':'London Hammer artifact Texas'
}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b19_candidates.json')) if retry and os.path.exists('videos_b19_candidates.json') else {}
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
  json.dump(candidates,open('videos_b19_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b19_candidates.json','w'),ensure_ascii=False,indent=1)
