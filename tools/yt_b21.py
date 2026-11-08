import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={
'yeha-temple':'Yeha temple Ethiopia pre-Aksumite','fasil-ghebbi':'Gondar castles Fasil Ghebbi Ethiopia','tiya-stelae':'Tiya stelae Ethiopia','makuria-faras':'Makuria Christian Nubia kingdom','queen-gudit':'Queen Gudit Yodit Aksum',
'famadihana':'Famadihana turning of the bones Madagascar','ambohimanga':'Ambohimanga royal hill Madagascar','hagia-sophia':'Hagia Sophia history architecture','fall-of-constantinople':'Fall of Constantinople 1453','nika-riots':'Nika riots Justinian Theodora',
'karakorum':'Karakorum Mongol capital archaeology','secret-history-mongols':'Secret History of the Mongols','malta-boy':"Mal'ta boy genome Native Americans Siberia",'orkhon-inscriptions':'Orkhon inscriptions Old Turkic','patomskiy-crater':'Patomskiy crater Siberia',
'andree-balloon':'Andree balloon expedition 1897 North Pole','zhokhov-island':'Zhokhov sled dogs 9500 years Arctic','royal-cemetery-ur':'Royal Cemetery of Ur Puabi','code-of-hammurabi':'Code of Hammurabi stele','kanesh-archives':'Kanesh Kultepe Assyrian merchants tablets',
'poverty-point':'Poverty Point earthworks Louisiana','walam-olum':'Walam Olum hoax Rafinesque','sky-woman':'Sky Woman Haudenosaunee creation story','newark-earthworks':'Newark Earthworks Octagon Hopewell','nemrut-dag':'Mount Nemrut Antiochus statues',
'messinian-zanclean':'Messinian salinity crisis Zanclean flood Mediterranean','jack-hills-zircons':'Jack Hills zircon oldest Earth crystal','petm':'Paleocene Eocene Thermal Maximum','prambanan':'Prambanan temple Java Roro Jonggrang','battle-of-mactan':'Battle of Mactan Lapulapu Magellan',
'ebu-gogo':'Ebu gogo Flores hobbit legend','pink-face-atapuerca':'earliest human face western Europe Atapuerca Pink','mantell-1948':'Mantell UFO incident 1948','pascagoula-1973':'Pascagoula abduction 1973','travis-walton-1975':'Travis Walton abduction 1975',
'ohare-2006':"O'Hare UFO sighting 2006",'ogopogo':'Ogopogo Okanagan Lake monster','dover-demon':'Dover Demon 1977','calaveras-skull':'Calaveras skull hoax','kinderhook-plates':'Kinderhook plates hoax'
}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b21_candidates.json')) if retry and os.path.exists('videos_b21_candidates.json') else {}
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
  json.dump(candidates,open('videos_b21_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b21_candidates.json','w'),ensure_ascii=False,indent=1)
