import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'rangi-papa':'Ranginui Papatuanuku Te Papa','tupaia-chart':'Tupaia map navigator','taputapuatea':'Taputapuatea UNESCO','moriori':'Moriori Chatham Islands','kon-tiki':'Kon-Tiki Heyerdahl','bounty-pitcairn':'Mutiny on the Bounty history','moa-extinction':'moa extinction PBS Eons','taupo-hatepe':'Taupo supervolcano',
'timur-tomb-curse':'Timur tomb Gur-e-Amir','al-khwarizmi':'al-Khwarizmi algebra','ai-khanoum':'Ai Khanoum Greek city Afghanistan','bamiyan-buddhas':'Bamiyan Buddhas','aral-sea':'Aral Sea disappearing','tillya-tepe':'Bactrian gold Tillya Tepe','tengri':'Tengri sky god',
'columbus-eclipse-1504':'Columbus lunar eclipse 1504','pelee-1902':'Mount Pelee 1902 Saint-Pierre','olduvai-gorge':'Olduvai Gorge','little-foot':'Little Foot Australopithecus','pinnacle-point':'Pinnacle Point early humans','wonderwerk-fire':'earliest fire Homo erectus',
'lion-man':'Lion Man ivory British Museum','hohle-fels-venus':'Venus of Hohle Fels','schoningen-spears':'Schoningen spears','kalambo-wood':'Kalambo Falls oldest wooden structure','harvey-circulation':'William Harvey circulation blood','leeuwenhoek':'Leeuwenhoek microscope','transit-of-venus-1769':'transit of Venus 1769 history','mary-toft':'Mary Toft rabbits','vegetable-lamb':'Vegetable Lamb of Tartary'}
import sys,os
# second pass (python3 yt_b9.py retry): channel-targeted queries for ids with no hit, merged into the same candidates file
Q2_OLD={'peking-man':'Peking Man Homo erectus PBS Eons','black-death':'Black Death plague SciShow','yeti':'yeti DNA bear Smithsonian','kailasa':'Kailasa temple Ellora UNESCO NHK','urashima-taro':'Urashima Taro Japanese folktale animation','delhi-iron-pillar':'Delhi iron pillar Qutb Minar UNESCO','green-children':'green children of Woolpit BBC','foo-fighters':'foo fighters World War II History','kaguya-hime':'Princess Kaguya tale Japan NHK','wendigo':'wendigo Algonquian legend PBS','turkana-boy':'Nariokotome boy Homo erectus PBS Eons','apollo-11-cave':'oldest art in Africa Apollo 11 stones','death-worm':'Mongolian death worm National Geographic','shambhala':'Shambhala legend Tibet','diquis-spheres':'Costa Rica stone spheres UNESCO','mozu-kofun':'Mozu Kofun Nintoku tomb NHK','jiroft':'Jiroft Iran archaeology','min-min':'Min Min light ABC'}
Q2_B14={'rigveda-aryan-debate':'Rigveda Crash Course','fu-hao':'Fu Hao Shang dynasty queen general','zhang-heng-seismoscope':'Zhang Heng earthquake detector','taiping-rebellion':'Taiping Rebellion Crash Course','xuanzang-journey':'Xuanzang TED-Ed','dunhuang-library-cave':'Diamond Sutra British Library','hanging-coffins':'hanging coffins','lothal-dockyard':'Lothal Harappan','mustatils':'mustatils','dilmun':'Dilmun','marib-dam':'Marib dam','jinn':'jinn','viking-sunstone':'sunstone Vikings polarization','trundholm-sun-chariot':'sun chariot Trundholm National Museum Denmark','sputnik-1957':'Sputnik','starfish-prime':'Starfish Prime','malmstrom-1967':'Malmstrom UFO','belgian-ufo-wave':'Belgian UFO wave','thylacine':'Tasmanian tiger','jersey-devil':'Jersey Devil','mapinguari':'mapinguari','gw150914':'gravitational waves LIGO','venus-phosphine':'Venus phosphine','sabbatai-zevi':'Sabbatai Zevi','kaifeng-jews':'Kaifeng Jews','jal-1628':'JAL 1628 UFO'}
Q2={}
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b17_candidates.json')) if retry and os.path.exists('videos_b17_candidates.json') else {}
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
  json.dump(candidates,open('videos_b17_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b17_candidates.json','w'),ensure_ascii=False,indent=1)
