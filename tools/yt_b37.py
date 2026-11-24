import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'perun-thunder-god': 'Perun Slavic god of thunder', 'veles-serpent-god': 'Veles Slavic god', 'mokosh': 'Mokosh Slavic goddess', 'rusalka': 'rusalka Slavic folklore', 'domovoy': 'domovoi Slavic house spirit', 'leshy': 'leshy Slavic forest spirit', 'kupala-night': 'Kupala Night festival', 'morana-marzanna': 'Marzanna drowning effigy spring', 'zbruch-idol': 'Zbruch idol', 'arkona-svantevit': 'Arkona Svantevit temple Rügen', 'rethra': 'Rethra Slavic temple', 'wawel-dragon': 'Wawel dragon Krakow legend', 'lech-czech-rus': 'Lech Czech Rus legend', 'libuse-prague': 'Libuse Prague legend', 'biskupin': 'Biskupin Iron Age settlement', 'book-of-veles': 'Book of Veles forgery', 'tale-of-igor': "Tale of Igor's Campaign", 'prague-orloj': 'Prague astronomical clock history', 'jan-hus': 'Jan Hus Council of Constance', 'onfim-birch-bark': 'Novgorod birch bark letters Onfim', 'turul': 'Turul bird Hungary legend', 'ilya-muromets': 'Ilya Muromets bylina', 'svyatogor': 'Svyatogor bogatyr', 'sadko': 'Sadko bylina Novgorod', 'sarmizegetusa-regia': 'Sarmizegetusa Regia Dacian', 'zalmoxis': 'Zalmoxis Dacian god', 'elizabeth-bathory': 'Elizabeth Bathory history', 'mohacs-1526': 'Battle of Mohacs 1526', 'plogojowitz-1725': 'Petar Blagojevic vampire 1725', 'vampire-burials': 'vampire burial Poland sickle', 'bucegi-sphinx': 'Bucegi Sphinx Romania', 'hoia-baciu-forest': 'Hoia Baciu forest', 'botai-horses': 'Botai horse domestication', 'otrar-1219': 'Otrar Genghis Khan Khwarazm', 'chud-legend': 'Chud people legend', 'holodomor': 'Holodomor famine 1932', 'katyn-1940': 'Katyn massacre 1940', 'kyshtym-1957': 'Kyshtym disaster 1957', 'medjugorje-1981': 'Medjugorje apparitions'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b37_candidates.json')) if retry and os.path.exists('videos_b37_candidates.json') else {}
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
  json.dump(candidates,open('videos_b37_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b37_candidates.json','w'),ensure_ascii=False,indent=1)
