import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'bayon-faces':'Bayon temple Angkor faces','ayutthaya-fall':'fall of Ayutthaya 1767','dong-son-drums':'Dong Son bronze drums','champa-kingdom':'Champa kingdom Vietnam','my-son-sanctuary':'My Son sanctuary UNESCO','sukhothai-kingdom':'Sukhothai kingdom Thailand','trung-sisters':'Trung sisters Vietnam','pyu-ancient-cities':'Pyu ancient cities Myanmar UNESCO',
'capacocha':'Inca capacocha child sacrifice Llullaillaco','chan-chan':'Chan Chan Chimor UNESCO','quipu':'quipu Inca knotted strings','amazon-geoglyphs':'Acre geoglyphs Amazon','qhapaq-nan':'Qhapaq Nan Inca road UNESCO','machu-picchu':'Machu Picchu National Geographic','wari-empire':'Wari empire Peru archaeology','coricancha':'Coricancha Cusco Temple of the Sun','huaca-del-sol':'Huaca de la Luna Moche','paracas-textiles':'Paracas textiles Peru',
'aksum-obelisks':'Obelisk of Axum Ethiopia','amanitore':'Amanitore Kush kandake','kanem-bornu':'Kanem Bornu empire','kebra-nagast':'Kebra Nagast Ethiopia','djenne-djenno':'Djenne Djenno archaeology','great-mosque-djenne':'Great Mosque of Djenne','askia-muhammad':'Askia Muhammad Songhai','ashanti-golden-stool':'Golden Stool Ashanti Yaa Asantewaa',
'amityville':'Amityville Horror hoax','area-51':'Area 51 Groom Lake history','cash-landrum':'Cash Landrum UFO','operation-highjump':'Operation Highjump Antarctica Byrd','archimedes':'Archimedes Syracuse SciShow','ibn-al-haytham':'Ibn al-Haytham Alhazen optics','cairo-geniza':'Cairo Geniza Schechter','grauballe-man':'Grauballe Man bog body','denisova-cave':'Denisovan cave PBS Eons','orontius-finaeus':'Oronce Fine map Hapgood'}
import sys,os
# second pass (python3 yt_b9.py retry): channel-targeted queries for ids with no hit, merged into the same candidates file
Q2_OLD={'peking-man':'Peking Man Homo erectus PBS Eons','black-death':'Black Death plague SciShow','yeti':'yeti DNA bear Smithsonian','kailasa':'Kailasa temple Ellora UNESCO NHK','urashima-taro':'Urashima Taro Japanese folktale animation','delhi-iron-pillar':'Delhi iron pillar Qutb Minar UNESCO','green-children':'green children of Woolpit BBC','foo-fighters':'foo fighters World War II History','kaguya-hime':'Princess Kaguya tale Japan NHK','wendigo':'wendigo Algonquian legend PBS','turkana-boy':'Nariokotome boy Homo erectus PBS Eons','apollo-11-cave':'oldest art in Africa Apollo 11 stones','death-worm':'Mongolian death worm National Geographic','shambhala':'Shambhala legend Tibet','diquis-spheres':'Costa Rica stone spheres UNESCO','mozu-kofun':'Mozu Kofun Nintoku tomb NHK','jiroft':'Jiroft Iran archaeology','min-min':'Min Min light ABC'}
Q2_B14={'rigveda-aryan-debate':'Rigveda Crash Course','fu-hao':'Fu Hao Shang dynasty queen general','zhang-heng-seismoscope':'Zhang Heng earthquake detector','taiping-rebellion':'Taiping Rebellion Crash Course','xuanzang-journey':'Xuanzang TED-Ed','dunhuang-library-cave':'Diamond Sutra British Library','hanging-coffins':'hanging coffins','lothal-dockyard':'Lothal Harappan','mustatils':'mustatils','dilmun':'Dilmun','marib-dam':'Marib dam','jinn':'jinn','viking-sunstone':'sunstone Vikings polarization','trundholm-sun-chariot':'sun chariot Trundholm National Museum Denmark','sputnik-1957':'Sputnik','starfish-prime':'Starfish Prime','malmstrom-1967':'Malmstrom UFO','belgian-ufo-wave':'Belgian UFO wave','thylacine':'Tasmanian tiger','jersey-devil':'Jersey Devil','mapinguari':'mapinguari','gw150914':'gravitational waves LIGO','venus-phosphine':'Venus phosphine','sabbatai-zevi':'Sabbatai Zevi','kaifeng-jews':'Kaifeng Jews','jal-1628':'JAL 1628 UFO'}
Q2={}
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b18_candidates.json')) if retry and os.path.exists('videos_b18_candidates.json') else {}
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
  json.dump(candidates,open('videos_b18_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b18_candidates.json','w'),ensure_ascii=False,indent=1)
