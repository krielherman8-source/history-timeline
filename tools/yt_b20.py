import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={
'book-of-kells':'Book of Kells Trinity College illuminated manuscript','hill-of-tara':'Hill of Tara Ireland archaeology','cu-chulainn':'Cú Chulainn Irish mythology','mabinogion':'Mabinogion Welsh mythology','fionn-mac-cumhaill':'Fionn mac Cumhaill Irish legend','cattle-raid-cooley':'Táin Bó Cúailnge Cattle Raid of Cooley','lindisfarne-gospels':'Lindisfarne Gospels British Library','iona-abbey':'Iona Abbey Columba Scotland','pictish-symbol-stones':'Pictish symbol stones Scotland','manannan-mac-lir':'Manannán mac Lir sea god',
'persepolis':'Persepolis UNESCO Achaemenid','sasanian-empire':'Sasanian Empire Persia history','parthian-empire':'Parthian Empire history','armenian-alphabet':'Armenian alphabet Mesrop Mashtots','etchmiadzin':'Etchmiadzin Cathedral Armenia UNESCO','shahnameh':'Shahnameh Ferdowsi Persian epic','mithraism':'Mithraism Roman mysteries','manichaeism':'Manichaeism Mani religion','taq-kasra':'Taq Kasra Arch of Ctesiphon','pasargadae':'Pasargadae Cyrus tomb UNESCO',
'yoruba-orisha':'Orisha Yoruba religion','oduduwa':'Oduduwa Ile-Ife Yoruba','ifa-divination':'Ifá divination Yoruba UNESCO','mapuche-resistance':'Lautaro Mapuche Arauco War','guarani-land-without-evil':'Guaraní Land without Evil','tiwanaku':'Tiwanaku Bolivia archaeology UNESCO','kalevala-epic':'Kalevala Finnish epic Lönnrot','vainamoinen':'Väinämöinen Kalevala','kingdom-of-kongo':'Kingdom of Kongo history','swahili-coast':'Swahili coast Kilwa Indian Ocean',
'phantom-time-hypothesis':'phantom time hypothesis Illig','fomenko-new-chronology':'Fomenko New Chronology debunked','tartarian-architecture':'Tartarian Empire mud flood conspiracy','freemasonry-origins':'origins of Freemasonry history','valensole-1965':'Valensole UFO 1965 France','trans-en-provence-1981':'Trans-en-Provence UFO 1981','hudson-valley-ufo':'Hudson Valley UFO sightings 1980s','belgium-wave-1989-90':'Belgian UFO wave 1989 triangles','sayburc':'Sayburç Taş Tepeler Neolithic','ain-ghazal':'Ain Ghazal statues Neolithic Jordan'
}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b20_candidates.json')) if retry and os.path.exists('videos_b20_candidates.json') else {}
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
  json.dump(candidates,open('videos_b20_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b20_candidates.json','w'),ensure_ascii=False,indent=1)
