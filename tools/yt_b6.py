import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={
'lebombo-bone':'Lebombo bone oldest mathematical artifact',
'green-sahara':'Green Sahara African humid period',
'tassili-round-heads':"Tassili n'Ajjer rock art",
'lydenburg-heads':'Lydenburg heads terracotta',
'igbo-ukwu':'Igbo-Ukwu bronzes',
'sungbo-eredo':"Sungbo's Eredo Nigeria",
'adams-calendar':"Adam's Calendar Mpumalanga",
'thonis-heracleion':'Thonis-Heracleion sunken city',
'dendera-light':'Dendera light bulb relief',
'rain-queen':'Rain Queen Modjadji',
'tanganyika-laughter':'Tanganyika laughter epidemic 1962',
'liangzhu':'Liangzhu ancient city',
'tarim-mummies':'Tarim mummies DNA',
'roopkund':'Roopkund skeleton lake DNA',
'hou-yi':'Hou Yi ten suns Chang\'e myth',
'dangun':'Dangun myth Korea founding',
'cheomseongdae':'Cheomseongdae observatory',
'xin-zhui':'Lady Dai Xin Zhui mummy',
'imperial-regalia':'Imperial Regalia of Japan three sacred treasures',
'laguna-copperplate':'Laguna Copperplate Inscription',
'tasaday':'Tasaday hoax',
'iram-ubar':'Ubar lost city Atlantis of the Sands',
'tooth-relic':'Temple of the Tooth Kandy relic',
'ningyo-mermaids':'mermaid mummy Japan scan',
'rongorongo':'rongorongo Easter Island script',
'roi-mata':'Chief Roi Mata Vanuatu',
'haamonga':"Ha'amonga 'a Maui trilithon Tonga",
'seven-sisters':'Pleiades seven sisters oldest story',
'menehune':'Menehune Hawaii legend',
'kaimanawa-wall':'Kaimanawa wall',
'bunyip':'bunyip legend',
'pakal-lid':'Pakal sarcophagus Palenque',
'sipan':'Lord of Sipan tomb',
'maya-script':'Maya glyphs decipherment',
'chichen-equinox':'Chichen Itza equinox serpent shadow',
'aztlan':'Aztlan Aztec origin migration',
'haudenosaunee-eclipse':'Haudenosaunee Great Law of Peace Peacemaker',
'thunderbird':'Thunderbird legend pterosaur fossils',
'roanoke':'Roanoke lost colony',
'shag-harbour':'Shag Harbour UFO incident 1967',
}
import sys,os
# second pass (python3 yt_b6.py retry): channel-targeted queries for ids with no hit, merged into the same candidates file
Q2={'maya-script': 'Maya hieroglyphs decipherment Smithsonian', 'pakal-lid': 'Pakal Palenque Smithsonian Channel', 'roanoke': 'Roanoke lost colony Smithsonian Channel', 'tarim-mummies': 'Tarim mummies Nature DNA study', 'roopkund': 'Roopkund lake skeletons BBC', 'ningyo-mermaids': 'mermaid mummy Japan BBC', 'rongorongo': 'rongorongo Easter Island Smithsonian', 'sipan': 'Lord of Sipan National Geographic', 'xin-zhui': 'Lady Dai mummy Smithsonian', 'liangzhu': 'Liangzhu archaeology UNESCO', 'lebombo-bone': 'oldest mathematical object tally bone Numberphile', 'tanganyika-laughter': '1962 laughter epidemic SciShow', 'thunderbird': 'Thunderbird legend Smithsonian NMAI', 'menehune': 'Menehune legend Hawaii PBS', 'aztlan': 'Aztec origin Aztlan World History Encyclopedia', 'igbo-ukwu': 'Igbo-Ukwu bronze British Museum', 'tooth-relic': 'Sri Dalada Maligawa Kandy UNESCO', 'cheomseongdae': 'Gyeongju historic areas UNESCO', 'bunyip': 'bunyip ABC', 'dendera-light': 'Dendera light bulb myth'}
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b6_candidates.json')) if retry and os.path.exists('videos_b6_candidates.json') else {}
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
json.dump(candidates,open('videos_b6_candidates.json','w'),ensure_ascii=False,indent=1)
