import re,json,urllib.request,urllib.parse
OK=['Fall of Civilizations','SciShow','Veritasium','Smarthistory','Khan Academy','Natural History Museum of Los Angeles County','Scientific American','PBS NewsHour','DW Documentary','Al Jazeera English','Museum of New Zealand Te Papa Tongarewa','NASA','NASA Goddard','European Space Agency, ESA','Royal Museums Greenwich','MinuteEarth','PBS Eons','Kurzgesagt','Crash Course','CrashCourse','BBC','National Geographic','PBS Space Time','Smithsonian','The British Museum','Royal Institution','NOVA PBS Official','Stated Clearly','Natural History Museum','History Time','Ted-Ed','TED-Ed','Sabine Hossenfelder','World History Encyclopedia','Science Magazine','Nature Video']
Q={
'vredefort':'Vredefort crater impact South Africa',
'homo-naledi':'Homo naledi Rising Star cave PBS Eons',
'madjedbebe':'Madjedbebe 65000 years Australia',
'lake-mungo':'Mungo Man Lake Mungo',
'nabta-playa':'Nabta Playa stone circle',
'kerma':'Kingdom of Kerma Nubia',
'punt':'Land of Punt Hatshepsut expedition',
'queen-of-sheba':'Queen of Sheba Ark of the Covenant Aksum',
'ife-heads':'Ife head bronze British Museum',
'sundiata':'Sundiata Keita epic TED-Ed',
'mali-atlantic-voyage':'Mansa Musa predecessor Atlantic voyage',
'jiahu-symbols':'Jiahu symbols earliest writing China',
'oracle-bones':'Shang oracle bones',
'plain-of-jars':'Plain of Jars Laos',
'genghis-tomb':'Genghis Khan tomb search',
'xu-fu':'Xu Fu elixir of life voyage',
'tambora-1815':'Tambora 1815 year without a summer',
'kuk-swamp':'Kuk swamp agriculture New Guinea',
'kuwae':'Kuwae eruption Vanuatu',
'haasts-eagle':'Haast\'s eagle moa',
'serpent-mound':'Serpent Mound Ohio',
'mound-builders-myth':'Mound Builders myth',
'amazon-cities':'lidar Amazon lost cities Upano',
'maya-collapse':'Classic Maya collapse drought',
'cortes-quetzalcoatl':'Cortes Quetzalcoatl myth Moctezuma',
'tokoloshe':'Tokoloshe South Africa',
'mami-wata':'Mami Wata',
'ram-setu':'Adam\'s Bridge Rama Setu',
'yonaguni':'Yonaguni monument',
'sunken-dwarka':'Dwarka underwater city',
'crystal-skulls':'crystal skulls British Museum Smithsonian',
'maya-2012':'2012 Maya calendar end of the world',
'nazca-mummies':'Nazca mummies alien hoax',
'utsuro-bune':'Utsuro-bune 1803',
'varginha-1996':'Varginha UFO incident',
'kaikoura-1978':'Kaikoura lights UFO 1978',
'okapi':'okapi discovery',
'giant-squid':'giant squid first footage',
}
import sys,os
# second pass (python3 yt_b5.py retry): channel-targeted queries for ids with no hit, merged into the same candidates file
Q2={
'vredefort':'Vredefort Dome NASA',
'lake-mungo':'Mungo Man oldest Australian Smithsonian',
'madjedbebe':'first Australians 65,000 years Nature video',
'nabta-playa':'Nabta Playa Stonehenge of Africa',
'kerma':'Kerma Nubia Fall of Civilizations',
'punt':'Land of Punt baboon mummies',
'tambora-1815':'Tambora eruption 1816 SciShow',
'haasts-eagle':'Haast\'s eagle PBS Eons',
'plain-of-jars':'Plain of Jars DW Documentary',
'maya-collapse':'Maya collapse drought National Geographic',
'amazon-cities':'Amazon lost cities lidar Nature video',
'okapi':'okapi National Geographic',
'giant-squid':'giant squid filmed first time National Geographic',
'maya-2012':'2012 Mayan calendar NASA',
'mound-builders-myth':'mound builders myth Smithsonian',
'serpent-mound':'Serpent Mound Smithsonian',
'kuk-swamp':'New Guinea first farmers agriculture',
'cortes-quetzalcoatl':'Aztec conquest Cortes Moctezuma Crash Course',
'jiahu-symbols':'Jiahu flutes Neolithic China',
'mami-wata':'Mami Wata Smithsonian African art',
'tokoloshe':'Tokoloshe myth',
}
retry=len(sys.argv)>1 and sys.argv[1]=='retry'
candidates=json.load(open('videos_b5_candidates.json')) if retry and os.path.exists('videos_b5_candidates.json') else {}
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
json.dump(candidates,open('videos_b5_candidates.json','w'),ensure_ascii=False,indent=1)
