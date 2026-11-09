import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'narmer-palette': 'Narmer Palette Smarthistory', 'diary-of-merer': 'Diary of Merer papyrus Wadi al-Jarf', 'amarna-letters': 'Amarna letters British Museum', 'battle-of-kadesh': 'Battle of Kadesh Ramesses Hittites', 'osiris-myth': 'myth of Osiris and Isis TED-Ed', 'abu-simbel': 'Abu Simbel temple relocation', 'tel-dan-stele': 'Tel Dan stele House of David', 'mesha-stele': 'Mesha stele Moabite stone', 'natufian-culture': 'Natufian culture first villages', 'proto-sinaitic-script': 'origin of the alphabet Proto-Sinaitic', 'battle-of-vienna-1683': 'Siege of Vienna 1683', 'devshirme-janissaries': 'Janissaries Ottoman devshirme', 'naqsh-e-jahan': 'Isfahan Naqsh-e Jahan square', 'shah-ismail': 'Shah Ismail Safavid empire', 'haitian-revolution': 'Haitian Revolution', 'kalinago-caribs': 'Kalinago Dominica', 'joya-de-ceren': 'Joya de Ceren', 'copan-stairway': 'Copan hieroglyphic stairway Maya', 'ciudad-blanca': 'lost city of the monkey god Honduras lidar', 'cadejo': 'Cadejo legend', 'inuksuk': 'inuksuk Inuit', 'sieidi': 'Sami sacred sieidi', 'potlatch-ban': 'potlatch ban Canada', 'sgang-gwaay': 'SGang Gwaay Haida Gwaii totem poles', 'tabon-caves': 'Tabon cave Palawan', 'code-of-kalantiaw': 'Code of Kalantiaw hoax', 'java-man': 'Java Man Dubois Homo erectus', 'degei': 'Fiji mythology Degei', 'marshall-stick-charts': 'Marshall Islands stick charts navigation', 'toraja-funerals': 'Toraja funeral Sulawesi', 'flannan-isles-1900': 'Flannan Isles lighthouse mystery', 'mad-gasser-mattoon': 'Mad Gasser of Mattoon', 'ghost-rockets-1946': 'ghost rockets 1946 Sweden', 'higgs-boson-2012': 'Higgs boson discovery 2012', 'h-pylori-ulcers': 'Barry Marshall H pylori drank', 'champ-lake-champlain': 'Champ Lake Champlain monster', 'vinland-map': 'Vinland Map fake Yale', 'glozel': 'Glozel', 'chernobyl-1986': 'Chernobyl disaster documentary', 'spanish-flu-1918': '1918 flu pandemic'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b22_candidates.json')) if retry and os.path.exists('videos_b22_candidates.json') else {}
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
  json.dump(candidates,open('videos_b22_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b22_candidates.json','w'),ensure_ascii=False,indent=1)
