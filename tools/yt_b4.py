import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video']
Q={
'lalibela':'Lalibela rock churches Ethiopia',
'kilwa':'Kilwa Kisiwani Swahili coast history',
'timbuktu-manuscripts':'Timbuktu manuscripts',
'ishango-bone':'Ishango bone mathematics',
'prester-john':'Prester John legend',
'qin-mausoleum':'Qin Shi Huang tomb mercury',
'borobudur':'Borobudur temple history',
'zheng-he':'Zheng He treasure fleet',
'homo-floresiensis':'Homo floresiensis hobbit PBS Eons',
'siberian-ice-maiden':'Siberian Ice Maiden Pazyryk',
'chaco-canyon':'Chaco Canyon Ancestral Puebloans',
'kennewick-man':'Kennewick Man DNA',
'polynesia-america-contact':'Polynesians Native Americans contact DNA',
'budj-bim':'Budj Bim eel traps',
'cascadia-1700':'Cascadia earthquake 1700 orphan tsunami',
'sn-1054':'Crab Nebula supernova 1054',
'volcanic-winter-536':'536 AD worst year volcanic winter',
'giant-impact-moon':'how the Moon formed giant impact',
'great-dying':'Great Dying Permian extinction PBS Eons',
'draupner-wave':'Draupner rogue wave',
'anansi':'Anansi the spider TED-Ed',
'rainbow-serpent':'Rainbow Serpent Aboriginal',
'maui':'Maui Polynesian myth TED-Ed',
'pele':'Pele Hawaiian goddess volcano',
'five-suns':'Aztec Five Suns myth TED-Ed',
'el-dorado':'El Dorado legend Muisca',
'nuwa':'Nuwa Chinese myth TED-Ed',
'bakunawa':'Bakunawa Philippine mythology',
'naga-fireballs':'Naga fireballs Mekong',
'kumari-kandam':'Kumari Kandam',
'nuremberg-1561':'1561 Nuremberg celestial phenomenon',
'tehran-1976':'1976 Tehran UFO incident',
'colares-1977':'Colares UFO Operacao Prato',
'valentich-1978':'Frederick Valentich disappearance',
'hessdalen-lights':'Hessdalen lights Norway',
'aaro-2024':'AARO UAP report 2024',
'cardiff-giant':'Cardiff Giant hoax',
'fujimura-hoax':'Shinichi Fujimura archaeology hoax',
'coelacanth':'coelacanth living fossil discovery',
'laigle-meteorites':'L Aigle meteorite 1803 Biot',
'lemuria-mu':'Lemuria lost continent',
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
json.dump(candidates,open('videos_b4_candidates.json','w'),ensure_ascii=False,indent=1)
