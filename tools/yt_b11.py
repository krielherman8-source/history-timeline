import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={
'zarathustra':'Zoroaster Zoroastrianism history','jamshid-var':'Jamshid Shahnameh Yima','shahr-e-sukhteh':'Shahr-e Sukhteh Burnt City Iran',
'behistun':'Behistun inscription Darius cuneiform','cyrus-cylinder':'Cyrus Cylinder British Museum','cambyses-army':'lost army of Cambyses',
'qanats':'Persian qanat ancient water','alamut-assassins':'Assassins Alamut Hashashin history','jikji':'Jikji oldest movable metal type',
'egg-born-kings':'Silla Bak Hyeokgeose legend','turtle-ships':'turtle ship Yi Sun-sin','himiko-yamatai':'Himiko queen Yamatai',
'kitsune-tamamo':'kitsune Japanese fox folklore','takeuchi-documents':'Jesus tomb Shingo Japan','tsunami-stones':'tsunami stones Japan warning',
'namazu':'namazu earthquake catfish Japan','lucy':'Lucy Australopithecus afarensis','laas-geel':'Laas Geel rock art Somaliland',
'madagascar-settlement':'settlement of Madagascar Austronesian','vazimba-kalanoro':'Vazimba Madagascar',
'lepenski-vir':'Lepenski Vir','saqqara-bird':'Saqqara bird glider','helicopter-hieroglyphs':'Abydos helicopter hieroglyphs explained',
'hatshepsut':'Hatshepsut female pharaoh','pompeii':'Pompeii plaster casts DNA','eleusinian-mysteries':'Eleusinian Mysteries',
'sutton-hoo':'Sutton Hoo ship burial','berserkers':'berserkers Vikings history','uffington-white-horse':'Uffington White Horse',
'ulfberht':'Ulfberht Viking sword NOVA','battle-of-la-1942':'Battle of Los Angeles 1942','eddington-1919':'1919 eclipse Eddington Einstein',
'face-on-mars':'Face on Mars Cydonia','black-knight-satellite':'Black Knight satellite','belmez-faces':'Belmez faces',
'hitler-diaries':'Hitler diaries forgery Stern','alien-autopsy':'alien autopsy hoax Santilli','alh84001':'ALH84001 Mars meteorite life',
'richat-structure':'Richat Structure Eye of the Sahara','havana-syndrome':'Havana syndrome',
}
import sys,os
# second pass (python3 yt_b9.py retry): channel-targeted queries for ids with no hit, merged into the same candidates file
Q2_OLD={'peking-man':'Peking Man Homo erectus PBS Eons','black-death':'Black Death plague SciShow','yeti':'yeti DNA bear Smithsonian','kailasa':'Kailasa temple Ellora UNESCO NHK','urashima-taro':'Urashima Taro Japanese folktale animation','delhi-iron-pillar':'Delhi iron pillar Qutb Minar UNESCO','green-children':'green children of Woolpit BBC','foo-fighters':'foo fighters World War II History','kaguya-hime':'Princess Kaguya tale Japan NHK','wendigo':'wendigo Algonquian legend PBS','turkana-boy':'Nariokotome boy Homo erectus PBS Eons','apollo-11-cave':'oldest art in Africa Apollo 11 stones','death-worm':'Mongolian death worm National Geographic','shambhala':'Shambhala legend Tibet','diquis-spheres':'Costa Rica stone spheres UNESCO','mozu-kofun':'Mozu Kofun Nintoku tomb NHK','jiroft':'Jiroft Iran archaeology','min-min':'Min Min light ABC'}
Q2={'pompeii':'Vesuvius Challenge Herculaneum scroll read','face-on-mars':'Face on Mars NASA Mars Global Surveyor','tsunami-stones':'tsunami stones NHK','jikji':'Jikji UNESCO Memory of the World','behistun':'Behistun inscription Bisotun UNESCO','berserkers':'berserker Norse warriors TED-Ed','ulfberht':'Secrets of the Viking Sword NOVA','zarathustra':'Zoroastrianism Crash Course','turtle-ships':'Korean turtle ship geobukseon','kitsune-tamamo':'kitsune fox spirit TED-Ed','richat-structure':'Eye of the Sahara NASA','saqqara-bird':'Saqqara bird','uffington-white-horse':'Uffington White Horse BBC','eleusinian-mysteries':'Eleusinian Mysteries TED-Ed','namazu':'namazu catfish earthquake','alamut-assassins':'Order of Assassins History Time','madagascar-settlement':'Madagascar Austronesian ancestry','battle-of-la-1942':'Battle of Los Angeles 1942 PBS','shahr-e-sukhteh':'Burnt City Shahr-i Sokhta UNESCO','lepenski-vir':'Lepenski Vir Serbia Mesolithic','himiko-yamatai':'Himiko Yamatai NHK'}
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b11_candidates.json')) if retry and os.path.exists('videos_b11_candidates.json') else {}
for k,q in (Q2 if retry else Q).items():
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
    if any(o['author_name'].lower()==a.lower() or o['author_name'].lower().startswith(a.lower()) for a in OK):
      hits.append(dict(type='video',url='https://www.youtube.com/watch?v='+i,title=o['title'],channel=o['author_name']))
  candidates[k]=(candidates.get(k) or [])+hits
  print(k, '->', [(h['channel'], h['title'][:70]) for h in hits[:3]] or 'NONE')
json.dump(candidates,open('videos_b11_candidates.json','w'),ensure_ascii=False,indent=1)
