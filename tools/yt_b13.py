import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={
'enuma-elish':'Enuma Elish Babylonian creation myth','sargon-akkad':'Sargon of Akkad first empire','hattusa-hittites':'Hittites Hattusa empire','ugarit-baal':'Ugarit alphabet Baal cycle',
'necho-circumnavigation':'Phoenicians circumnavigate Africa Necho Herodotus','ashurbanipal-library':'Library of Ashurbanipal British Museum','hanging-gardens':'Hanging Gardens of Babylon Nineveh Dalley','ebla-tablets':'Ebla tablets archive Syria',
'descent-of-inanna':'Inanna descent underworld myth','apkallu-oannes':'Apkallu Oannes fish sage','nag-hammadi':'Nag Hammadi library gnostic gospels','gospel-of-judas':'Gospel of Judas National Geographic',
'gospel-jesus-wife':'Gospel of Jesus Wife forgery','knights-templar':'Knights Templar arrest 1307','holy-grail':'Holy Grail legend history','pope-joan':'Pope Joan legend',
'childrens-crusade':'Children\'s Crusade 1212','joan-of-arc':'Joan of Arc history','wild-hunt':'Wild Hunt folklore','cathars':'Cathars Albigensian Crusade Montsegur',
'mechanical-turk':'Mechanical Turk chess automaton','mesmer':'Mesmer animal magnetism Franklin commission','spring-heeled-jack':'Spring-heeled Jack Victorian','missoula-floods':'Missoula floods Bretz scablands',
'trinity-1945':'Trinity test 1945','dna-photo-51':'Rosalind Franklin Photo 51 DNA','cmb-1965':'cosmic microwave background discovery Penzias Wilson','pulsar-lgm1':'Jocelyn Bell Burnell pulsar discovery',
'voyager-golden-record':'Voyager Golden Record','laschamp-excursion':'Laschamp event magnetic field 42000 years','unkulunkulu':'Zulu creation myth Unkulunkulu chameleon','shaka-zulu':'Shaka Zulu kingdom history',
'nyai-roro-kidul':'Nyai Roro Kidul queen southern sea','majapahit':'Majapahit empire history','ifugao-terraces':'Ifugao rice terraces','tangata-manu':'Easter Island birdman Orongo',
'hokulea-1976':'Hokulea voyage 1976 Mau Piailug','terra-preta':'terra preta Amazon dark earth','fawcett-z':'Percy Fawcett lost city Z','bighorn-medicine-wheel':'Bighorn Medicine Wheel Wyoming',
}
import sys,os
# second pass (python3 yt_b9.py retry): channel-targeted queries for ids with no hit, merged into the same candidates file
Q2_OLD={'peking-man':'Peking Man Homo erectus PBS Eons','black-death':'Black Death plague SciShow','yeti':'yeti DNA bear Smithsonian','kailasa':'Kailasa temple Ellora UNESCO NHK','urashima-taro':'Urashima Taro Japanese folktale animation','delhi-iron-pillar':'Delhi iron pillar Qutb Minar UNESCO','green-children':'green children of Woolpit BBC','foo-fighters':'foo fighters World War II History','kaguya-hime':'Princess Kaguya tale Japan NHK','wendigo':'wendigo Algonquian legend PBS','turkana-boy':'Nariokotome boy Homo erectus PBS Eons','apollo-11-cave':'oldest art in Africa Apollo 11 stones','death-worm':'Mongolian death worm National Geographic','shambhala':'Shambhala legend Tibet','diquis-spheres':'Costa Rica stone spheres UNESCO','mozu-kofun':'Mozu Kofun Nintoku tomb NHK','jiroft':'Jiroft Iran archaeology','min-min':'Min Min light ABC'}
Q2={'enuma-elish':'Enuma Elish TED-Ed','hattusa-hittites':'Hittites Fall of Civilizations','ugarit-baal':'Ugarit Fall of Civilizations','ashurbanipal-library':'Ashurbanipal library Nineveh','hanging-gardens':'Hanging Gardens Babylon TED-Ed','nag-hammadi':'Nag Hammadi gnostic','knights-templar':'Knights Templar History','holy-grail':'Holy Grail TED-Ed','joan-of-arc':'Joan of Arc TED-Ed','mechanical-turk':'Mechanical Turk chess hoax','missoula-floods':'Missoula floods Channeled Scablands','trinity-1945':'Trinity test atomic bomb','cmb-1965':'cosmic microwave background PBS Space Time','pulsar-lgm1':'pulsar discovery Jocelyn Bell','voyager-golden-record':'Voyager Golden Record NASA','shaka-zulu':'Shaka Zulu','majapahit':'Majapahit','ifugao-terraces':'Rice terraces Philippine Cordilleras UNESCO','tangata-manu':'Rapa Nui birdman','hokulea-1976':'Hokulea Polynesian voyaging','terra-preta':'Amazon dark earth','fawcett-z':'Percy Fawcett'}
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b13_candidates.json')) if retry and os.path.exists('videos_b13_candidates.json') else {}
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
  json.dump(candidates,open('videos_b13_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b13_candidates.json','w'),ensure_ascii=False,indent=1)
