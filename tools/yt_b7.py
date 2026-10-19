import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video','UNESCO','The Met','Getty Museum','NHK WORLD-JAPAN','CBC News','ABC News In-depth','ABC Australia','PBS','Penn Museum','INAH TV','Stanford','University of Oxford','Cambridge University','Numberphile']
Q={
'snowball-earth':'Snowball Earth PBS Eons',
'lomekwi':'Lomekwi 3.3 million year old stone tools',
'turkana-boy':'Turkana Boy Homo erectus skeleton',
'dmanisi':'Dmanisi skull Homo erectus Georgia',
'peking-man':'Peking Man fossils lost',
'apollo-11-cave':'Apollo 11 cave stones Namibia rock art',
'tsodilo-python':'Tsodilo Hills Botswana UNESCO',
'altamira':'Cave of Altamira paintings',
'otzi':'Otzi the iceman',
'diquis-spheres':'stone spheres of Costa Rica Diquis',
'delhi-iron-pillar':'iron pillar of Delhi rust',
'nine-unknown-men':'Nine Unknown Men Ashoka',
'jiroft':'Jiroft civilization Iran Konar Sandal',
'mozu-kofun':'Mozu Furuichi Kofun Group UNESCO',
'urashima-taro':'Urashima Taro legend',
'kakudmi':'Kakudmi Brahma time dilation story',
'kaguya-hime':'Tale of the Bamboo Cutter Kaguya',
'kailasa':'Kailasa temple Ellora',
'shambhala':'Shambhala Kalachakra',
'yeti':'yeti DNA bears study',
'death-worm':'Mongolian death worm',
'baigong-pipes':'Baigong pipes',
'library-alexandria':'Library of Alexandria destruction',
'wagadu-bida':'Ghana Empire Wagadu history',
'gedi':'Gedi ruins Kenya',
'inkanyamba':'Inkanyamba Howick Falls',
'lake-nyos':'Lake Nyos disaster 1986',
'black-death':'Black Death plague origin DNA',
'green-children':'Green Children of Woolpit',
'dancing-plague':'dancing plague of 1518',
'salem':'Salem witch trials',
'oisin':'Oisin Tir na nOg legend',
'mary-celeste':'Mary Celeste mystery',
'hawaiki':'Polynesian voyaging Hokule\'a navigation',
'min-min':'Min Min lights outback',
'yowie':'yowie Australia',
'wendigo':'wendigo legend',
'foo-fighters':'foo fighters WWII UFO',
'dyatlov':'Dyatlov Pass avalanche study',
'chelyabinsk':'Chelyabinsk meteor 2013',
}
import sys,os
# second pass (python3 yt_b7.py retry): channel-targeted queries for ids with no hit, merged into the same candidates file
Q2={'peking-man':'Peking Man Homo erectus PBS Eons','black-death':'Black Death plague SciShow','yeti':'yeti DNA bear Smithsonian','kailasa':'Kailasa temple Ellora UNESCO NHK','urashima-taro':'Urashima Taro Japanese folktale animation','delhi-iron-pillar':'Delhi iron pillar Qutb Minar UNESCO','green-children':'green children of Woolpit BBC','foo-fighters':'foo fighters World War II History','kaguya-hime':'Princess Kaguya tale Japan NHK','wendigo':'wendigo Algonquian legend PBS','turkana-boy':'Nariokotome boy Homo erectus PBS Eons','apollo-11-cave':'oldest art in Africa Apollo 11 stones','death-worm':'Mongolian death worm National Geographic','shambhala':'Shambhala legend Tibet','diquis-spheres':'Costa Rica stone spheres UNESCO','mozu-kofun':'Mozu Kofun Nintoku tomb NHK','jiroft':'Jiroft Iran archaeology','min-min':'Min Min light ABC'}
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b7_candidates.json')) if retry and os.path.exists('videos_b7_candidates.json') else {}
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
json.dump(candidates,open('videos_b7_candidates.json','w'),ensure_ascii=False,indent=1)
