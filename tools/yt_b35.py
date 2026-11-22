import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={'shanidar-flower-burial': 'Shanidar Cave Neanderthal flower burial', 'star-carr': 'Star Carr Mesolithic headdress', 'atlit-yam': 'Atlit Yam submerged village', 'ain-dara-footprints': 'Ain Dara temple footprints', 'vix-grave': 'Vix krater Lady of Vix', 'xiongnu': 'Xiongnu empire history', 'kushan-kanishka': 'Kushan Empire history', 'sogdian-merchants': 'Sogdians Silk Road merchants', 'al-andalus-cordoba': 'Al-Andalus Cordoba caliphate history', 'boskop-man': 'Boskop skull', 'atlantic-slave-trade': 'Atlantic slave trade history', 'potosi-silver': 'Potosi silver mine history', 'defenestration-thirty-years-war': 'Thirty Years War explained', 'tulip-mania-1637': 'tulip mania 1637', 'great-fire-of-london-1666': 'Great Fire of London 1666', 'south-sea-bubble-1720': 'South Sea Bubble 1720', 'sakoku-closed-japan': 'sakoku Japan closed country Edo', 'cook-terra-australis-lono': 'Captain Cook voyages', 'first-opium-war': 'First Opium War', 'great-trek-1836': 'Great Trek Voortrekkers', 'berlin-conference-1884': 'Berlin Conference 1884 Scramble for Africa', 'world-war-one': 'World War I explained', 'angels-of-mons': 'Angels of Mons', 'world-war-two': 'World War II explained', 'holocaust': 'The Holocaust history', 'sharpeville-massacre-1960': 'Sharpeville massacre 1960', 'mau-mau-uprising': 'Mau Mau uprising Kenya', 'rwandan-genocide-1994': 'Rwandan genocide 1994', 'september-11-attacks': 'September 11 attacks 2001', 'richard-iii-car-park': 'Richard III car park Leicester', 'prince-madoc': 'Prince Madoc Welsh America', 'wandering-jew': 'Wandering Jew legend', 'lorelei-rhine': 'Lorelei Rhine legend', 'tarasque': 'Tarasque Tarascon', 'simurgh': 'Simurgh Persian mythology', 'mbombo-kuba-creation': 'Kuba kingdom Congo', 'elizabeth-klarer': 'Elizabeth Klarer', 'im1-interstellar-meteor': 'Avi Loeb interstellar meteor spherules', 'north-sentinel-island': 'North Sentinel Island Sentinelese', 'tanis-kpg-site': 'Tanis fossil site dinosaur impact'}
import sys,os
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b35_candidates.json')) if retry and os.path.exists('videos_b35_candidates.json') else {}
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
  json.dump(candidates,open('videos_b35_candidates.json','w'),ensure_ascii=False,indent=1)
json.dump(candidates,open('videos_b35_candidates.json','w'),ensure_ascii=False,indent=1)
