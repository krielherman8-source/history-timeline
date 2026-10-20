import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={
'harbin-dragon-man':'Harbin Dragon Man skull Denisovan',
'homo-luzonensis':'Homo luzonensis Callao Cave new species',
'chavin':'Chavin de Huantar temple Peru',
'kuelap':'Kuelap fortress Chachapoyas',
'paracas-skulls':'Paracas elongated skulls',
'sacsayhuaman':'Sacsayhuaman Inca walls how built',
'khipu':'Inca khipu quipu knots writing',
'paititi':'Paititi lost city Inca',
'llullaillaco':'Llullaillaco Inca child mummies',
'fuente-magna':'Fuente Magna bowl',
'bmac':'Oxus civilization Gonur Depe',
'arkaim':'Arkaim Sintashta',
'issyk-golden-man':'Golden Man Issyk kurgan Kazakhstan',
'scythian-amazons':'Amazons Scythian women warriors archaeology',
'ulugh-beg':'Ulugh Beg observatory Samarkand',
'tamgaly':'Tamgaly petroglyphs Kazakhstan UNESCO',
'dead-sea-scrolls':'Dead Sea Scrolls discovery',
'copper-scroll':'Copper Scroll Dead Sea treasure',
'derinkuyu':'Derinkuyu underground city',
'ark-covenant':'Ark of the Covenant Ethiopia Aksum',
'durupinar':'Durupinar Noah\'s Ark site geology',
'etemenanki':'Tower of Babel Etemenanki ziggurat',
'ban-chiang':'Ban Chiang archaeological site Thailand',
'srivijaya':'Srivijaya empire history',
'orang-pendek':'orang pendek Sumatra',
'manananggal':'manananggal Philippine folklore',
'night-marchers':'Hawaiian night marchers legend',
'latte-stones':'latte stones Guam Chamorro',
'rai-stones':'Yap stone money rai',
'john-frum':'John Frum cargo cult Tanna',
'tamam-shud':'Somerton Man identified DNA',
'jericho-tower':'Tower of Jericho Neolithic',
'cave-of-swimmers':'Cave of Swimmers Gilf Kebir',
'bigo-chwezi':'Bigo bya Mugenyi Chwezi Uganda',
'pied-piper':'Pied Piper of Hamelin true story',
'carrington-event':'Carrington Event 1859 solar storm',
'the-hum':'the Hum mystery sound Taos Windsor',
'baltic-anomaly':'Baltic Sea anomaly sonar',
}
import sys,os
# second pass (python3 yt_b7.py retry): channel-targeted queries for ids with no hit, merged into the same candidates file
Q2_OLD={'peking-man':'Peking Man Homo erectus PBS Eons','black-death':'Black Death plague SciShow','yeti':'yeti DNA bear Smithsonian','kailasa':'Kailasa temple Ellora UNESCO NHK','urashima-taro':'Urashima Taro Japanese folktale animation','delhi-iron-pillar':'Delhi iron pillar Qutb Minar UNESCO','green-children':'green children of Woolpit BBC','foo-fighters':'foo fighters World War II History','kaguya-hime':'Princess Kaguya tale Japan NHK','wendigo':'wendigo Algonquian legend PBS','turkana-boy':'Nariokotome boy Homo erectus PBS Eons','apollo-11-cave':'oldest art in Africa Apollo 11 stones','death-worm':'Mongolian death worm National Geographic','shambhala':'Shambhala legend Tibet','diquis-spheres':'Costa Rica stone spheres UNESCO','mozu-kofun':'Mozu Kofun Nintoku tomb NHK','jiroft':'Jiroft Iran archaeology','min-min':'Min Min light ABC'}
Q2={'harbin-dragon-man':'Dragon Man Denisovan skull Nature Video','chavin':'Chavin de Huantar UNESCO NHK','sacsayhuaman':'Sacsayhuaman Inca stonework Smarthistory','kuelap':'Kuelap Peru Chachapoyas documentary','paititi':'Paititi Inca lost city expedition','bmac':'Bactria Margiana Oxus civilization','ulugh-beg':'Ulugh Beg astronomer Samarkand','scythian-amazons':'Amazons were real TED-Ed','issyk-golden-man':'Golden Man Kazakhstan Saka','copper-scroll':'Copper Scroll Qumran','etemenanki':'Tower of Babel archaeology Babylon ziggurat','srivijaya':'Srivijaya Kingdom Sumatra history','rai-stones':'Yap rai stones money NPR Planet Money','john-frum':'John Frum Tanna Vanuatu BBC','tamam-shud':'Somerton Man mystery solved ABC','jericho-tower':'Jericho oldest city UNESCO','cave-of-swimmers':'green Sahara African humid period','pied-piper':'Pied Piper Hamelin history','carrington-event':'Carrington Event solar storm SciShow','the-hum':'The Hum noise BBC','baltic-anomaly':'Baltic Sea anomaly geologist','night-marchers':'night marchers Hawaii PBS','manananggal':'aswang manananggal folklore','orang-pendek':'orang pendek search Sumatra','durupinar':'Noah\'s Ark Turkey site claim','arkaim':'Arkaim Russia ancient city','paracas-skulls':'elongated skulls Paracas cranial deformation','fuente-magna':'Fuente Magna Bolivia','bigo-chwezi':'Chwezi Uganda history'}
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b8_candidates.json')) if retry and os.path.exists('videos_b8_candidates.json') else {}
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
json.dump(candidates,open('videos_b8_candidates.json','w'),ensure_ascii=False,indent=1)
