import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={
'late-heavy-bombardment':'Late Heavy Bombardment early Earth',
'ediacaran-biota':'Ediacaran biota first animals',
'lascaux':'Lascaux cave paintings',
'varna-gold':'Varna necropolis oldest gold',
'carnac':'Carnac stones Brittany megaliths',
'newgrange':'Newgrange winter solstice',
'skara-brae':'Skara Brae Neolithic Orkney',
'knossos-labyrinth':'Knossos Minotaur labyrinth myth',
'delphi-oracle':'Oracle of Delphi Pythia',
'tollund-man':'Tollund Man bog body',
'steppe-migration':'Yamnaya steppe migration ancient DNA',
'tuniit':'Dorset culture Tuniit Arctic',
'sedna':'Sedna Inuit sea goddess',
'franklin-expedition':'Franklin expedition HMS Erebus Terror wreck',
'mesa-verde':'Mesa Verde cliff dwellings',
'taino-ocean-gourd':'Taino mythology',
'taino-survival':'Taino ancient DNA Caribbean',
'port-royal':'Port Royal Jamaica 1692 earthquake sunken city',
'haitian-zombies':'Haitian zombie Wade Davis',
'bimini-road':'Bimini Road Atlantis',
'bermuda-triangle':'Bermuda Triangle explained',
'chupacabra':'chupacabra mange coyote',
'bhimbetka':'Bhimbetka rock shelters UNESCO',
'mehrgarh':'Mehrgarh Neolithic Pakistan',
'sarasvati-river':'Sarasvati river Ghaggar Hakra',
'rakhigarhi-genome':'Rakhigarhi DNA Harappan genome',
'patala':'Patala Hindu underworld Nagas',
'sigiriya':'Sigiriya Lion Rock Sri Lanka',
'gwion-gwion':'Gwion Gwion Kimberley rock art',
'tycho-supernova':'Tycho supernova 1572',
'eyam-plague':'Eyam plague village',
'beast-of-gevaudan':'Beast of Gevaudan',
'lisbon-1755':'1755 Lisbon earthquake',
'war-of-the-worlds-1938':'War of the Worlds 1938 panic myth',
'philadelphia-experiment':'Philadelphia Experiment USS Eldridge',
'flatwoods-monster':'Flatwoods monster',
'socorro-zamora':'Lonnie Zamora Socorro UFO',
'kecksburg-1965':'Kecksburg UFO incident',
'mothman':'Mothman Point Pleasant',
}
import sys,os
# second pass (python3 yt_b9.py retry): channel-targeted queries for ids with no hit, merged into the same candidates file
Q2_OLD={'peking-man':'Peking Man Homo erectus PBS Eons','black-death':'Black Death plague SciShow','yeti':'yeti DNA bear Smithsonian','kailasa':'Kailasa temple Ellora UNESCO NHK','urashima-taro':'Urashima Taro Japanese folktale animation','delhi-iron-pillar':'Delhi iron pillar Qutb Minar UNESCO','green-children':'green children of Woolpit BBC','foo-fighters':'foo fighters World War II History','kaguya-hime':'Princess Kaguya tale Japan NHK','wendigo':'wendigo Algonquian legend PBS','turkana-boy':'Nariokotome boy Homo erectus PBS Eons','apollo-11-cave':'oldest art in Africa Apollo 11 stones','death-worm':'Mongolian death worm National Geographic','shambhala':'Shambhala legend Tibet','diquis-spheres':'Costa Rica stone spheres UNESCO','mozu-kofun':'Mozu Kofun Nintoku tomb NHK','jiroft':'Jiroft Iran archaeology','min-min':'Min Min light ABC'}
Q2={
'late-heavy-bombardment':'early Earth bombardment PBS Eons','ediacaran-biota':'Ediacaran PBS Eons','varna-gold':'Varna gold Bulgaria history','carnac':'Carnac menhirs history','newgrange':'Newgrange UNESCO NHK','skara-brae':'Skara Brae Orkney UNESCO','knossos-labyrinth':'Minotaur myth TED-Ed','delphi-oracle':'Delphi oracle gas Smithsonian','tollund-man':'bog bodies National Geographic','steppe-migration':'Indo-European migration DNA Yamnaya','tuniit':'Dorset Paleo-Eskimo DNA','sedna':'Sedna myth Inuit animation','franklin-expedition':'HMS Terror wreck Parks Canada','mesa-verde':'Mesa Verde UNESCO NHK','taino-survival':'Taino genome Puerto Rico','port-royal':'Port Royal sunken pirate city','bimini-road':'Bimini road geology','bermuda-triangle':'Bermuda Triangle mystery SciShow','chupacabra':'chupacabra legend National Geographic','bhimbetka':'Bhimbetka UNESCO NHK','sigiriya':'Sigiriya UNESCO NHK','gwion-gwion':'Kimberley rock art ABC','tycho-supernova':'Tycho Brahe supernova NASA','eyam-plague':'Eyam plague BBC','beast-of-gevaudan':'Beast of Gevaudan history','lisbon-1755':'Lisbon earthquake 1755 history','war-of-the-worlds-1938':'War of the Worlds broadcast 1938','philadelphia-experiment':'Philadelphia Experiment explained','socorro-zamora':'Socorro UFO 1964','mothman':'Mothman legend'}
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b9_candidates.json')) if retry and os.path.exists('videos_b9_candidates.json') else {}
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
json.dump(candidates,open('videos_b9_candidates.json','w'),ensure_ascii=False,indent=1)
