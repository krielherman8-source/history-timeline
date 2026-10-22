import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={
'jebel-sahaba':'Jebel Sahaba oldest war evidence',
'garamantes':'Garamantes Sahara civilization',
'carthage-tophet':'Carthage child sacrifice tophet',
'akhenaten':'Akhenaten heretic pharaoh Amarna',
'pharaohs-curse':'curse of Tutankhamun tomb',
'taung-child':'Taung Child Australopithecus Raymond Dart',
'san-rock-art':'San rock art southern Africa',
'dahomey-amazons':'Dahomey Amazons Agojie women warriors',
'nzinga':'Queen Nzinga Ndongo Angola',
'nongqawuse':'Xhosa cattle killing Nongqawuse',
'cholula':'Great Pyramid of Cholula',
'tenochtitlan-founding':'founding of Tenochtitlan Aztec',
'la-llorona':'La Llorona legend origin',
'spiro-mounds':'Spiro Mounds Oklahoma',
'skinwalker':'skinwalker Navajo legend',
'ghost-dance':'Ghost Dance Wounded Knee 1890',
'white-sands-footprints':'White Sands footprints 23000 years',
'piasa':'Piasa bird Alton Illinois',
'tartaria-tablets':'Tartaria tablets Vinca script',
'cucuteni-trypillia':'Cucuteni Trypillia mega-sites',
'kitezh':'Kitezh invisible city lake Svetloyar',
'baba-yaga':'Baba Yaga Slavic folklore',
'arnold-paole':'Arnold Paole vampire Serbia',
'anna-anderson':'Anna Anderson Anastasia DNA',
'house-of-wisdom':'House of Wisdom Baghdad',
'ibn-fadlan':'Ibn Fadlan Rus Vikings',
'seven-sleepers':'Seven Sleepers of Ephesus',
'roc-elephant-bird':'elephant bird Madagascar',
'wolfe-creek':'Wolfe Creek crater',
'mahogany-ship':'Mahogany Ship Warrnambool',
'great-moon-hoax':'Great Moon Hoax 1835',
'mystery-airships':'mystery airship 1897',
'fox-sisters':'Fox sisters spiritualism',
'semmelweis':'Ignaz Semmelweis handwashing',
'martian-canals':'canals on Mars Percival Lowell',
'n-rays':'N-rays Blondlot',
'krakatoa-1883':'Krakatoa 1883 eruption',
'devils-footprints':"Devil's Footprints Devon 1855",
'halley-1910':'Halley comet 1910 panic',
'kaspar-hauser':'Kaspar Hauser mystery',
}
import sys,os
# second pass (python3 yt_b9.py retry): channel-targeted queries for ids with no hit, merged into the same candidates file
Q2_OLD={'peking-man':'Peking Man Homo erectus PBS Eons','black-death':'Black Death plague SciShow','yeti':'yeti DNA bear Smithsonian','kailasa':'Kailasa temple Ellora UNESCO NHK','urashima-taro':'Urashima Taro Japanese folktale animation','delhi-iron-pillar':'Delhi iron pillar Qutb Minar UNESCO','green-children':'green children of Woolpit BBC','foo-fighters':'foo fighters World War II History','kaguya-hime':'Princess Kaguya tale Japan NHK','wendigo':'wendigo Algonquian legend PBS','turkana-boy':'Nariokotome boy Homo erectus PBS Eons','apollo-11-cave':'oldest art in Africa Apollo 11 stones','death-worm':'Mongolian death worm National Geographic','shambhala':'Shambhala legend Tibet','diquis-spheres':'Costa Rica stone spheres UNESCO','mozu-kofun':'Mozu Kofun Nintoku tomb NHK','jiroft':'Jiroft Iran archaeology','min-min':'Min Min light ABC'}
Q2={
'krakatoa-1883':'Krakatoa eruption documentary BBC',
'martian-canals':'Percival Lowell Mars canals NASA',
'n-rays':'N-rays Veritasium',
'halley-1910':'1910 comet panic Smithsonian',
'dahomey-amazons':'women warriors of Dahomey Smithsonian',
'ghost-dance':'Ghost Dance Lakota Smithsonian',
'la-llorona':'La Llorona Weeping Woman TED-Ed',
'kitezh':'Kitezh legend',
'baba-yaga':'Baba Yaga folklore History',
'carthage-tophet':'Carthage child sacrifice evidence',
'cholula':'Cholula pyramid National Geographic',
'garamantes':'Garamantes Fall of Civilizations',
'seven-sleepers':'Seven Sleepers Ashab al-Kahf',
'anna-anderson':'Anna Anderson Anastasia impostor',
'fox-sisters':'Fox sisters Spiritualism Smithsonian',
'mystery-airships':'1897 airship sightings History',
'san-rock-art':'San rock art Smarthistory',
'nongqawuse':'Xhosa cattle killing 1856',
'kaspar-hauser':'Kaspar Hauser History',
'skinwalker':'Skinwalker legend Navajo',
}
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b10_candidates.json')) if retry and os.path.exists('videos_b10_candidates.json') else {}
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
json.dump(candidates,open('videos_b10_candidates.json','w'),ensure_ascii=False,indent=1)
