import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={
'tuatha-de-danann':'Tuatha De Danann Irish mythology','brendan-voyage':'Saint Brendan voyage Tim Severin','hy-brasil':'Hy-Brasil phantom island',
'gundestrup-cauldron':'Gundestrup cauldron','ogham':'Ogham stones Ireland','giants-causeway':'Giant\'s Causeway formation basalt columns',
'druids':'druids history Celts','selkies':'selkie folklore Scotland','cantre-gwaelod':'Cantre\'r Gwaelod sunken forest Borth','ys':'legend of Ys Brittany',
'kaali-crater':'Kaali crater Estonia','sampo':'Kalevala Sampo','lithuania-last-pagans':'Lithuania last pagan Europe','sami-drums':'Sami drum noaidi',
'amber-road':'Amber Road Baltic amber trade','areni-1':'Areni-1 cave oldest shoe winery','zorats-karer':'Zorats Karer Carahunge','amirani':'Amirani Georgian myth Prometheus',
'golden-fleece':'Golden Fleece Colchis Jason Argonauts','vishap-stones':'vishap dragon stones Armenia',
'shigir-idol':'Shigir idol oldest wooden sculpture','deer-stones':'deer stones Mongolia','king-gesar':'Epic of King Gesar','denisovan-tibet':'Denisovan Tibet EPAS1 Xiahe jaw',
'terma-tibet':'terma Tibetan hidden treasure texts','kimpa-vita':'Kimpa Vita Kongo','senegambian-circles':'Senegambian stone circles Wassu','lake-bosumtwi':'Lake Bosumtwi crater Ghana',
'nsibidi':'Nsibidi script','titicaca-offerings':'Lake Titicaca underwater offerings Tiwanaku',
'greek-fire':'Greek fire Byzantine weapon','justinian-plague':'Plague of Justinian','marble-emperor':'Constantine XI fall of Constantinople 1453','donation-of-constantine':'Donation of Constantine forgery Lorenzo Valla',
'john-dee-enochian':'John Dee Edward Kelley angels','dodo':'dodo extinction Mauritius','miyake-774':'Miyake event 774 solar storm tree rings','hidden-christians-japan':'Kakure Kirishitan hidden Christians Japan',
'henderson-island':'Henderson Island plastic Pitcairn','kap-kobenhavn-edna':'2 million year old DNA Greenland',
}
import sys,os
# second pass (python3 yt_b9.py retry): channel-targeted queries for ids with no hit, merged into the same candidates file
Q2_OLD={'peking-man':'Peking Man Homo erectus PBS Eons','black-death':'Black Death plague SciShow','yeti':'yeti DNA bear Smithsonian','kailasa':'Kailasa temple Ellora UNESCO NHK','urashima-taro':'Urashima Taro Japanese folktale animation','delhi-iron-pillar':'Delhi iron pillar Qutb Minar UNESCO','green-children':'green children of Woolpit BBC','foo-fighters':'foo fighters World War II History','kaguya-hime':'Princess Kaguya tale Japan NHK','wendigo':'wendigo Algonquian legend PBS','turkana-boy':'Nariokotome boy Homo erectus PBS Eons','apollo-11-cave':'oldest art in Africa Apollo 11 stones','death-worm':'Mongolian death worm National Geographic','shambhala':'Shambhala legend Tibet','diquis-spheres':'Costa Rica stone spheres UNESCO','mozu-kofun':'Mozu Kofun Nintoku tomb NHK','jiroft':'Jiroft Iran archaeology','min-min':'Min Min light ABC'}
Q2={'tuatha-de-danann':'Tuatha De Danann Irish mythology TED-Ed','brendan-voyage':'St Brendan voyage Atlantic BBC','ogham':'Ogham stones Ireland British Museum','selkies':'selkie legend TED-Ed','kaali-crater':'Kaali crater Estonia meteorite','sami-drums':'Sami drum returned BBC','amber-road':'amber Baltic ancient trade Smithsonian','areni-1':'Areni-1 cave oldest winery National Geographic','zorats-karer':'Zorats Karer Carahunge Armenia','shigir-idol':'Shigir idol oldest wooden sculpture','deer-stones':'deer stones Mongolia Smithsonian','denisovan-tibet':'Denisovan jaw Xiahe Tibet PBS Eons','kimpa-vita':'Kimpa Vita Kongo','lake-bosumtwi':'Lake Bosumtwi Ghana','nsibidi':'Nsibidi writing','justinian-plague':'Plague of Justinian TED-Ed','john-dee-enochian':'John Dee British Museum magic mirror','miyake-774':'Miyake event 774 AD tree rings','donation-of-constantine':'Donation of Constantine forgery Lorenzo Valla','titicaca-offerings':'Lake Titicaca underwater offerings Khoa'}
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b12_candidates.json')) if retry and os.path.exists('videos_b12_candidates.json') else {}
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
    if any(o.get('author_name','').lower()==a.lower() or o.get('author_name','').lower().startswith(a.lower()) for a in OK):
      hits.append(dict(type='video',url='https://www.youtube.com/watch?v='+i,title=o['title'],channel=o['author_name']))
  candidates[k]=(candidates.get(k) or [])+hits
  print(k, '->', [(h['channel'], h['title'][:70]) for h in hits[:3]] or 'NONE', flush=True)
  json.dump(candidates,open('videos_b12_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b12_candidates.json','w'),ensure_ascii=False,indent=1)
