# categories / threads per entry id (merged into entries.json by apply_tags)
C={
'big-bang':'science-cosmos','earth-forms':'science-cosmos','great-oxidation':'science-cosmos','cambrian':'science-cosmos',
'kpg':'science-cosmos catastrophes','dragons-fossils':'myth-legend science-cosmos','first-homo':'science-cosmos archaeology',
'homo-sapiens':'science-cosmos archaeology','toba':'catastrophes science-cosmos','neanderthal-dna':'science-cosmos archaeology',
'sulawesi-art':'archaeology','chauvet':'archaeology','americas-peopling':'archaeology history','mwp1a':'science-cosmos catastrophes',
'younger-dryas':'science-cosmos catastrophes','lost-civilisation':'lost-civilisations anomalies','gobekli-tepe':'archaeology anomalies',
'sundaland':'catastrophes lost-civilisations','aboriginal-coast':'myth-legend catastrophes','doggerland':'catastrophes archaeology',
'black-sea-flood':'catastrophes','catalhoyuk':'archaeology','writing':'history archaeology','stonehenge':'archaeology history',
'great-pyramid':'archaeology history anomalies','sphinx-water':'archaeology anomalies lost-civilisations','gilgamesh':'myth-legend religion',
'yu-flood':'myth-legend catastrophes history','thera':'catastrophes archaeology','exodus':'religion history','bronze-collapse':'history catastrophes',
'troy':'history archaeology myth-legend','genesis-flood':'religion myth-legend','manu':'religion myth-legend','deucalion':'myth-legend',
'atlantis':'myth-legend lost-civilisations','enoch':'religion myth-legend aliens-ufo','antikythera':'archaeology science-cosmos anomalies',
'popol-vuh':'myth-legend religion','pangu':'myth-legend','ragnarok':'myth-legend religion','vinland':'history archaeology',
'arthur':'myth-legend history','shroud':'religion anomalies','printing':'history','heliocentrism':'science-cosmos history religion',
'tunguska':'catastrophes science-cosmos anomalies','piltdown':'hoaxes science-cosmos','plate-tectonics':'science-cosmos','moon-landing':'history science-cosmos',
'oumuamua':'science-cosmos anomalies','uap-hearing-2023':'aliens-ufo anomalies history','eht-m87':'science-cosmos','gunung-padang':'archaeology lost-civilisations hoaxes'}
T={'flood-myths':'gilgamesh genesis-flood manu deucalion yu-flood popol-vuh aboriginal-coast black-sea-flood mwp1a doggerland sundaland younger-dryas',
'lost-civilisations':'lost-civilisation atlantis sundaland sphinx-water gunung-padang gobekli-tepe younger-dryas great-pyramid thera',
'sky-beings':'enoch uap-hearing-2023',
'cosmic-impacts':'kpg younger-dryas tunguska',
'changed-understanding':'earth-forms kpg homo-sapiens americas-peopling neanderthal-dna plate-tectonics heliocentrism troy vinland piltdown gunung-padang gobekli-tepe',
'dragons-and-fossils':'dragons-fossils kpg'}
def apply(entries):
  for e in entries:
    e['categories']=C[e['id']].split()
    e['threads']=[t for t,ids in T.items() if e['id'] in ids.split()]
# --- batch 2
C.update({'kenneth-arnold':'aliens-ufo anomalies','roswell':'aliens-ufo anomalies history','project-blue-book':'aliens-ufo history','betty-barney-hill':'aliens-ufo',
'chariots-of-the-gods':'aliens-ufo lost-civilisations','rendlesham':'aliens-ufo anomalies','phoenix-lights':'aliens-ufo anomalies','nimitz-tic-tac':'aliens-ufo anomalies',
'fermi-paradox':'science-cosmos aliens-ufo','wow-signal':'science-cosmos aliens-ufo anomalies','oklo':'science-cosmos anomalies','nazca-lines':'archaeology anomalies',
'baghdad-battery':'archaeology anomalies','voynich':'anomalies history','dropa-stones':'hoaxes aliens-ufo','piri-reis':'history anomalies lost-civilisations',
'fast-radio-bursts':'science-cosmos anomalies','tabbys-star':'science-cosmos anomalies aliens-ufo','crop-circles':'hoaxes anomalies','cottingley-fairies':'hoaxes',
'silurian-hypothesis':'science-cosmos lost-civilisations','sumerian-king-list':'myth-legend religion history','puma-punku':'archaeology anomalies lost-civilisations',
'baalbek':'archaeology anomalies','bosnian-pyramids':'hoaxes lost-civilisations','nebra-sky-disc':'archaeology science-cosmos','kensington-runestone':'history hoaxes',
'indus-valley':'history archaeology','rome-founding':'myth-legend history','rome-fall':'history','mazama-klamath':'myth-legend catastrophes science-cosmos',
'wegener':'science-cosmos','anunnaki':'myth-legend religion aliens-ufo','vimanas':'myth-legend religion aliens-ufo','dogon-sirius':'myth-legend aliens-ufo science-cosmos',
'nephilim':'religion myth-legend','ezekiel-wheel':'religion aliens-ufo','miracle-of-sun':'religion anomalies','loch-ness':'hoaxes myth-legend','bigfoot-film':'anomalies'})
def addt(t,ids): T[t]=(T.get(t,'')+' '+ids).strip()
addt('sky-beings','chariots-of-the-gods anunnaki vimanas dogon-sirius nephilim ezekiel-wheel betty-barney-hill sumerian-king-list')
addt('lost-civilisations','chariots-of-the-gods silurian-hypothesis puma-punku baalbek bosnian-pyramids piri-reis sumerian-king-list nazca-lines')
addt('ufo-encounters','kenneth-arnold roswell project-blue-book betty-barney-hill rendlesham phoenix-lights nimitz-tic-tac uap-hearing-2023 wow-signal')
addt('hoaxes-exposed','piltdown crop-circles cottingley-fairies loch-ness dropa-stones gunung-padang')
addt('flood-myths','sumerian-king-list')
addt('changed-understanding','wegener nebra-sky-disc roswell')

# --- batch 3
C.update({
'great-zimbabwe':'history archaeology lost-civilisations',
'mapungubwe':'history archaeology',
'aksum':'history archaeology',
'nok-culture':'archaeology history',
'mansa-musa':'history',
'benin-bronzes':'history archaeology',
'blombos':'archaeology science-cosmos',
'border-cave':'archaeology science-cosmos',
'meroe':'history archaeology',
'laetoli':'science-cosmos archaeology',
'jomon-pottery':'archaeology history',
'sanxingdui':'archaeology anomalies lost-civilisations',
'xia-dynasty':'history archaeology',
'harappan-script':'history archaeology anomalies',
'angkor':'history archaeology',
'nan-madol':'archaeology lost-civilisations anomalies',
'rapa-nui-moai':'archaeology history anomalies',
'lapita':'archaeology history',
'wandjina':'myth-legend religion archaeology',
'kupe':'myth-legend history',
'cahokia':'archaeology history',
'teotihuacan':'archaeology history',
'olmec-heads':'archaeology history anomalies',
'caral':'archaeology history',
'monte-verde':'archaeology history',
'clovis-first':'archaeology history',
'ica-stones':'hoaxes anomalies',
'acambaro-figures':'hoaxes',
'quetzalcoatl':'myth-legend religion',
'viracocha':'myth-legend religion',
'westall-ufo':'aliens-ufo anomalies',
'ruwa-ariel':'aliens-ufo anomalies',
'vela-incident':'anomalies history science-cosmos',
'mokele-mbembe':'myth-legend anomalies',
'popobawa':'myth-legend',
'nyaminyami':'myth-legend catastrophes',
'wilusa':'history archaeology myth-legend',
'izanagi-izanami':'myth-legend religion',
'bunjil':'myth-legend religion',
'curuca-event':'catastrophes science-cosmos anomalies',
})
addt('lost-civilisations','great-zimbabwe sanxingdui nan-madol rapa-nui-moai')
addt('hoaxes-exposed','ica-stones acambaro-figures')
addt('ufo-encounters','westall-ufo ruwa-ariel')
addt('sky-beings','wandjina quetzalcoatl viracocha')
addt('flood-myths','nyaminyami')
addt('cosmic-impacts','vela-incident curuca-event')
addt('changed-understanding','great-zimbabwe monte-verde clovis-first wilusa')
addt('giant-monuments','great-zimbabwe nan-madol rapa-nui-moai baalbek puma-punku olmec-heads teotihuacan angkor cahokia meroe')
addt('cryptids','mokele-mbembe loch-ness bigfoot-film')
addt('stories-proven-true','wilusa troy great-zimbabwe')

# --- batch 4
C.update({
'lalibela':'history archaeology religion',
'kilwa':'history archaeology',
'timbuktu-manuscripts':'history',
'ishango-bone':'archaeology science-cosmos anomalies',
'prester-john':'myth-legend religion history lost-civilisations',
'qin-mausoleum':'archaeology history anomalies',
'borobudur':'archaeology history religion',
'zheng-he':'history hoaxes',
'homo-floresiensis':'science-cosmos archaeology myth-legend',
'siberian-ice-maiden':'archaeology history',
'chaco-canyon':'archaeology science-cosmos',
'kennewick-man':'archaeology science-cosmos',
'polynesia-america-contact':'history archaeology science-cosmos',
'budj-bim':'archaeology catastrophes myth-legend',
'cascadia-1700':'catastrophes history myth-legend',
'sn-1054':'science-cosmos history',
'volcanic-winter-536':'catastrophes history science-cosmos',
'giant-impact-moon':'science-cosmos catastrophes',
'great-dying':'science-cosmos catastrophes',
'draupner-wave':'science-cosmos anomalies',
'anansi':'myth-legend religion',
'rainbow-serpent':'myth-legend religion',
'maui':'myth-legend',
'pele':'myth-legend religion catastrophes',
'five-suns':'myth-legend religion catastrophes',
'el-dorado':'myth-legend lost-civilisations archaeology',
'nuwa':'myth-legend religion',
'bakunawa':'myth-legend science-cosmos',
'naga-fireballs':'myth-legend anomalies',
'kumari-kandam':'myth-legend lost-civilisations',
'nuremberg-1561':'aliens-ufo anomalies history',
'tehran-1976':'aliens-ufo anomalies',
'colares-1977':'aliens-ufo anomalies',
'valentich-1978':'aliens-ufo anomalies',
'hessdalen-lights':'anomalies science-cosmos aliens-ufo',
'aaro-2024':'aliens-ufo history',
'cardiff-giant':'hoaxes',
'fujimura-hoax':'hoaxes archaeology',
'coelacanth':'science-cosmos anomalies',
'laigle-meteorites':'science-cosmos history',
'lemuria-mu':'lost-civilisations myth-legend hoaxes',
})
addt('flood-myths','nuwa five-suns kumari-kandam cascadia-1700 rainbow-serpent')
addt('lost-civilisations','kumari-kandam lemuria-mu el-dorado prester-john')
addt('sky-beings','nuremberg-1561')
addt('cosmic-impacts','giant-impact-moon laigle-meteorites great-dying')
addt('changed-understanding','kennewick-man polynesia-america-contact homo-floresiensis coelacanth laigle-meteorites draupner-wave lemuria-mu cascadia-1700 giant-impact-moon fujimura-hoax')
addt('ufo-encounters','nuremberg-1561 tehran-1976 colares-1977 valentich-1978 hessdalen-lights aaro-2024')
addt('hoaxes-exposed','cardiff-giant fujimura-hoax prester-john')
addt('giant-monuments','lalibela borobudur chaco-canyon qin-mausoleum')
addt('cryptids','homo-floresiensis coelacanth')
addt('stories-proven-true','cascadia-1700 coelacanth draupner-wave laigle-meteorites el-dorado budj-bim qin-mausoleum pele polynesia-america-contact')
addt('deep-oral-memory','budj-bim cascadia-1700 pele mazama-klamath aboriginal-coast homo-floresiensis kumari-kandam wilusa')
addt('serpent-beings','rainbow-serpent bakunawa naga-fireballs nyaminyami quetzalcoatl')
addt('lost-continents','atlantis lemuria-mu kumari-kandam sundaland doggerland')
addt('sky-omens','sn-1054 nuremberg-1561 volcanic-winter-536 bakunawa miracle-of-sun')
addt('world-ages-and-resets','five-suns popol-vuh ragnarok viracocha')
addt('creation-myths','pangu izanagi-izanami bunjil nuwa rainbow-serpent maui pele five-suns popol-vuh viracocha anansi')
addt('volcanoes-and-memory','budj-bim pele mazama-klamath thera toba volcanic-winter-536')
addt('giants-and-little-people','nephilim cardiff-giant homo-floresiensis')
addt('ocean-voyagers','zheng-he polynesia-america-contact kupe lapita maui vinland')
addt('mass-extinctions','great-dying kpg')

# --- batch 5
C.update({
'vredefort':'science-cosmos catastrophes',
'homo-naledi':'science-cosmos archaeology',
'madjedbebe':'archaeology history',
'lake-mungo':'archaeology history religion',
'nabta-playa':'archaeology science-cosmos anomalies',
'kerma':'history archaeology',
'punt':'history archaeology',
'queen-of-sheba':'myth-legend religion history',
'ife-heads':'history archaeology lost-civilisations',
'sundiata':'myth-legend history',
'mali-atlantic-voyage':'history anomalies',
'jiahu-symbols':'archaeology history anomalies',
'oracle-bones':'history archaeology religion',
'plain-of-jars':'archaeology history myth-legend',
'genghis-tomb':'history myth-legend anomalies',
'xu-fu':'history myth-legend',
'tambora-1815':'catastrophes history science-cosmos lost-civilisations',
'kuk-swamp':'archaeology history',
'kuwae':'myth-legend catastrophes science-cosmos',
'haasts-eagle':'science-cosmos myth-legend',
})
addt('cosmic-impacts','vredefort')
addt('changed-understanding','homo-naledi madjedbebe lake-mungo kerma ife-heads oracle-bones')
addt('ancient-astronomy','nabta-playa stonehenge chaco-canyon nebra-sky-disc antikythera sn-1054 ishango-bone')
addt('ocean-voyagers','punt mali-atlantic-voyage xu-fu')
addt('serpent-beings','queen-of-sheba')
addt('sacred-relics','queen-of-sheba shroud')
addt('lost-civilisations','ife-heads tambora-1815')
addt('deep-oral-memory','sundiata kuwae haasts-eagle')
addt('origins-of-writing','writing harappan-script jiahu-symbols oracle-bones')
addt('dragons-and-fossils','oracle-bones')
addt('stories-proven-true','oracle-bones haasts-eagle')
addt('giants-and-little-people','plain-of-jars')
addt('giant-monuments','plain-of-jars kerma')
addt('hidden-tombs','genghis-tomb qin-mausoleum')
addt('volcanoes-and-memory','tambora-1815 kuwae')
addt('lost-continents','kuwae')
C.update({
'serpent-mound':'archaeology history religion',
'mound-builders-myth':'hoaxes lost-civilisations history',
'amazon-cities':'archaeology history lost-civilisations',
'maya-collapse':'history archaeology catastrophes',
'cortes-quetzalcoatl':'history myth-legend religion',
'tokoloshe':'myth-legend anomalies',
'mami-wata':'myth-legend religion',
'ram-setu':'myth-legend religion science-cosmos anomalies',
'yonaguni':'archaeology lost-civilisations anomalies',
'sunken-dwarka':'myth-legend religion archaeology lost-civilisations',
'crystal-skulls':'hoaxes anomalies',
'maya-2012':'hoaxes myth-legend catastrophes',
'nazca-mummies':'hoaxes aliens-ufo',
'utsuro-bune':'myth-legend aliens-ufo anomalies',
'varginha-1996':'aliens-ufo anomalies',
'kaikoura-1978':'aliens-ufo anomalies',
'okapi':'science-cosmos anomalies myth-legend',
'giant-squid':'science-cosmos myth-legend anomalies',
})
addt('serpent-beings','serpent-mound mami-wata')
addt('sky-omens','serpent-mound cortes-quetzalcoatl')
addt('lost-civilisations','mound-builders-myth amazon-cities yonaguni sunken-dwarka')
addt('hoaxes-exposed','mound-builders-myth crystal-skulls nazca-mummies')
addt('giants-and-little-people','mound-builders-myth tokoloshe')
addt('changed-understanding','mound-builders-myth amazon-cities cortes-quetzalcoatl okapi giant-squid')
addt('stories-proven-true','amazon-cities okapi giant-squid')
addt('giant-monuments','serpent-mound')
addt('civilisation-collapses','bronze-collapse rome-fall maya-collapse')
addt('lost-continents','ram-setu yonaguni mound-builders-myth')
addt('flood-myths','sunken-dwarka')
addt('world-ages-and-resets','maya-2012')
addt('ufo-encounters','utsuro-bune varginha-1996 kaikoura-1978')
addt('cryptids','okapi giant-squid')

# --- batch 6
C.update({
'lebombo-bone':'archaeology science-cosmos anomalies',
'green-sahara':'science-cosmos catastrophes archaeology',
'tassili-round-heads':'archaeology anomalies religion',
'lydenburg-heads':'archaeology history',
'igbo-ukwu':'archaeology history',
'sungbo-eredo':'archaeology history myth-legend',
'adams-calendar':'archaeology lost-civilisations aliens-ufo',
'thonis-heracleion':'archaeology history lost-civilisations',
'dendera-light':'archaeology anomalies religion',
'rain-queen':'history myth-legend religion',
})
addt('ancient-astronomy','lebombo-bone adams-calendar')
addt('changed-understanding','green-sahara igbo-ukwu thonis-heracleion')
addt('civilisation-collapses','green-sahara')
addt('sky-beings','adams-calendar')
addt('lost-civilisations','adams-calendar')
addt('giant-monuments','sungbo-eredo')
addt('serpent-beings','dendera-light')
addt('ancient-technology','dendera-light baghdad-battery antikythera vimanas')
addt('stories-proven-true','thonis-heracleion')
addt('sunken-cities','thonis-heracleion sunken-dwarka yonaguni atlantis kuwae')
addt('vanished-landscapes','green-sahara tassili-round-heads nabta-playa doggerland sundaland')
