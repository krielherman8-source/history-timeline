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
C.update({
'tanganyika-laughter':'history anomalies',
'liangzhu':'archaeology history catastrophes lost-civilisations',
'tarim-mummies':'archaeology science-cosmos anomalies',
'roopkund':'archaeology anomalies myth-legend catastrophes',
'hou-yi':'myth-legend catastrophes',
'dangun':'myth-legend religion history hoaxes',
'cheomseongdae':'archaeology science-cosmos history',
'xin-zhui':'archaeology history anomalies',
'imperial-regalia':'history myth-legend religion',
'laguna-copperplate':'history archaeology',
})
addt('collective-experiences','tanganyika-laughter popobawa ruwa-ariel miracle-of-sun phoenix-lights')
addt('civilisation-collapses','liangzhu')
addt('flood-myths','liangzhu')
addt('lost-civilisations','liangzhu')
addt('mummies','tarim-mummies xin-zhui siberian-ice-maiden')
addt('changed-understanding','tarim-mummies roopkund laguna-copperplate')
addt('deep-oral-memory','roopkund')
addt('sky-omens','hou-yi')
addt('world-ages-and-resets','hou-yi')
addt('sky-beings','dangun')
addt('hidden-tombs','dangun xin-zhui')
addt('knowledge-and-power','dangun imperial-regalia great-zimbabwe mound-builders-myth timbuktu-manuscripts kumari-kandam')
addt('sacred-kingship','rain-queen dangun imperial-regalia sumerian-king-list')
addt('ancient-astronomy','cheomseongdae laguna-copperplate')
addt('sacred-relics','imperial-regalia')
addt('serpent-beings','imperial-regalia')
addt('origins-of-writing','laguna-copperplate')
C.update({
'tasaday':'history hoaxes anomalies',
'iram-ubar':'myth-legend religion lost-civilisations archaeology',
'tooth-relic':'religion history',
'ningyo-mermaids':'hoaxes myth-legend anomalies',
'rongorongo':'history archaeology anomalies',
'roi-mata':'history archaeology myth-legend',
'haamonga':'archaeology science-cosmos myth-legend',
'seven-sisters':'myth-legend science-cosmos',
'menehune':'myth-legend lost-civilisations',
'kaimanawa-wall':'hoaxes lost-civilisations science-cosmos',
})
addt('hoaxes-exposed','tasaday ningyo-mermaids kaimanawa-wall')
addt('changed-understanding','tasaday rongorongo')
addt('knowledge-and-power','tasaday')
addt('lost-civilisations','iram-ubar kaimanawa-wall')
addt('lost-continents','iram-ubar')
addt('stories-proven-true','roi-mata')
addt('sacred-relics','tooth-relic')
addt('sacred-kingship','tooth-relic')
addt('mummies','ningyo-mermaids nazca-mummies')
addt('cryptids','ningyo-mermaids')
addt('origins-of-writing','rongorongo')
addt('ancient-astronomy','rongorongo haamonga seven-sisters')
addt('civilisation-collapses','rongorongo')
addt('hidden-tombs','roi-mata')
addt('deep-oral-memory','roi-mata seven-sisters menehune')
addt('giant-monuments','haamonga')
addt('giants-and-little-people','menehune')
addt('outsider-builder-claims','menehune kaimanawa-wall mound-builders-myth great-zimbabwe adams-calendar igbo-ukwu')
C.update({
'bunyip':'myth-legend anomalies science-cosmos',
'pakal-lid':'archaeology history aliens-ufo',
'sipan':'archaeology history',
'maya-script':'history archaeology',
'chichen-equinox':'archaeology science-cosmos anomalies',
'aztlan':'myth-legend lost-civilisations history',
'haudenosaunee-eclipse':'history science-cosmos myth-legend',
'thunderbird':'myth-legend religion science-cosmos',
'roanoke':'history anomalies',
'shag-harbour':'aliens-ufo anomalies',
})
addt('cryptids','bunyip thunderbird')
addt('dragons-and-fossils','bunyip thunderbird')
addt('deep-oral-memory','bunyip thunderbird haudenosaunee-eclipse aztlan')
addt('hidden-tombs','pakal-lid sipan')
addt('sky-beings','pakal-lid')
addt('mummies','sipan')
addt('origins-of-writing','maya-script')
addt('knowledge-and-power','maya-script')
addt('changed-understanding','maya-script')
addt('ancient-astronomy','chichen-equinox haudenosaunee-eclipse')
addt('serpent-beings','chichen-equinox thunderbird')
addt('lost-civilisations','aztlan')
addt('sky-omens','aztlan haudenosaunee-eclipse')
addt('disappearances','roanoke valentich-1978 mali-atlantic-voyage')
addt('ufo-encounters','shag-harbour')

# --- batch 7 (2026-10-19)
C.update({
'snowball-earth':'science-cosmos catastrophes',
'lomekwi':'archaeology science-cosmos',
'turkana-boy':'science-cosmos archaeology',
'dmanisi':'science-cosmos archaeology',
'peking-man':'science-cosmos archaeology history anomalies',
'apollo-11-cave':'archaeology myth-legend',
'tsodilo-python':'archaeology religion myth-legend',
'altamira':'archaeology history',
'otzi':'archaeology history science-cosmos',
'diquis-spheres':'archaeology anomalies lost-civilisations',
})
addt('human-origins','first-homo homo-sapiens laetoli homo-naledi homo-floresiensis neanderthal-dna border-cave lomekwi turkana-boy dmanisi peking-man')
addt('changed-understanding','snowball-earth lomekwi dmanisi altamira')
addt('lost-evidence','peking-man diquis-spheres timbuktu-manuscripts')
addt('disappearances','peking-man')
addt('knowledge-and-power','peking-man altamira')
addt('stories-proven-true','altamira')
addt('serpent-beings','tsodilo-python')
addt('creation-myths','tsodilo-python')
addt('mummies','otzi')
addt('lost-civilisations','diquis-spheres')
addt('giant-monuments','diquis-spheres')
addt('shapeshifters','apollo-11-cave')
C.update({
'delhi-iron-pillar':'archaeology history anomalies',
'nine-unknown-men':'myth-legend hoaxes',
'jiroft':'archaeology history lost-civilisations',
'mozu-kofun':'archaeology history',
'urashima-taro':'myth-legend anomalies',
'kakudmi':'myth-legend religion',
'kaguya-hime':'myth-legend aliens-ufo',
'kailasa':'archaeology history religion',
'shambhala':'myth-legend religion lost-civilisations',
'yeti':'myth-legend anomalies',
'death-worm':'myth-legend anomalies',
'baigong-pipes':'anomalies hoaxes',
})
addt('ancient-technology','delhi-iron-pillar baigong-pipes')
addt('outsider-builder-claims','delhi-iron-pillar kailasa')
addt('knowledge-and-power','nine-unknown-men mozu-kofun')
addt('hidden-kingdoms','nine-unknown-men shambhala prester-john el-dorado aztlan iram-ubar')
addt('origins-of-writing','jiroft')
addt('lost-civilisations','jiroft shambhala')
addt('lost-evidence','jiroft')
addt('hidden-tombs','mozu-kofun')
addt('sacred-kingship','mozu-kofun')
addt('giant-monuments','mozu-kofun kailasa')
addt('otherworld-visits','urashima-taro kakudmi')
addt('world-ages-and-resets','kakudmi shambhala')
addt('sky-beings','kaguya-hime')
addt('cryptids','yeti death-worm')
C.update({
'library-alexandria':'history',
'wagadu-bida':'myth-legend religion history',
'gedi':'history archaeology lost-civilisations',
'inkanyamba':'myth-legend anomalies',
'lake-nyos':'catastrophes science-cosmos myth-legend',
'black-death':'history catastrophes science-cosmos',
'green-children':'myth-legend anomalies aliens-ufo',
'dancing-plague':'history anomalies',
'salem':'history religion',
'oisin':'myth-legend',
'mary-celeste':'history anomalies',
})
addt('lost-evidence','library-alexandria')
addt('knowledge-and-power','library-alexandria salem')
addt('serpent-beings','wagadu-bida inkanyamba')
addt('civilisation-collapses','wagadu-bida gedi black-death')
addt('sacred-kingship','wagadu-bida')
addt('rain-and-drought','rain-queen wagadu-bida inkanyamba rainbow-serpent tsodilo-python nyaminyami')
addt('cryptids','inkanyamba')
addt('deep-oral-memory','lake-nyos wagadu-bida')
addt('stories-proven-true','lake-nyos')
addt('volcanoes-and-memory','lake-nyos')
addt('sky-omens','black-death')
addt('changed-understanding','black-death')
addt('otherworld-visits','green-children oisin')
addt('sky-beings','green-children')
addt('collective-experiences','dancing-plague salem')
addt('disappearances','mary-celeste')
C.update({
'hawaiki':'myth-legend religion history',
'min-min':'anomalies myth-legend aliens-ufo',
'yowie':'myth-legend anomalies',
'wendigo':'myth-legend religion',
'foo-fighters':'aliens-ufo anomalies history',
'dyatlov':'history anomalies',
'chelyabinsk':'science-cosmos catastrophes',
})
addt('ancestral-homelands','hawaiki aztlan kupe wagadu-bida dangun')
addt('ocean-voyagers','hawaiki')
addt('mysterious-lights','min-min foo-fighters hessdalen-lights naga-fireballs kaikoura-1978 phoenix-lights colares-1977')
addt('deep-oral-memory','min-min')
addt('cryptids','yowie')
addt('giants-and-little-people','yowie')
addt('shapeshifters','wendigo popobawa')
addt('ufo-encounters','foo-fighters')
addt('disappearances','dyatlov')
addt('cosmic-impacts','chelyabinsk')
addt('sky-omens','chelyabinsk')
# --- batch 8 (2026-10-20)
C.update({
'harbin-dragon-man':'science-cosmos archaeology',
'homo-luzonensis':'science-cosmos archaeology',
'chavin':'archaeology history religion',
'kuelap':'archaeology history lost-civilisations',
'paracas-skulls':'archaeology anomalies aliens-ufo',
'sacsayhuaman':'archaeology history anomalies',
'khipu':'history archaeology',
'paititi':'myth-legend lost-civilisations',
'llullaillaco':'archaeology history religion',
'fuente-magna':'archaeology anomalies',
})
addt('human-origins','harbin-dragon-man homo-luzonensis')
addt('changed-understanding','harbin-dragon-man homo-luzonensis khipu')
addt('lost-evidence','harbin-dragon-man')
addt('giants-and-little-people','homo-luzonensis')
addt('ocean-voyagers','homo-luzonensis')
addt('strange-sounds','chavin')
addt('underground-worlds','chavin')
addt('knowledge-and-power','chavin khipu')
addt('civilisation-collapses','chavin')
addt('giant-monuments','kuelap sacsayhuaman')
addt('lost-civilisations','kuelap')
addt('outsider-builder-claims','kuelap sacsayhuaman paracas-skulls fuente-magna')
addt('mummies','paracas-skulls llullaillaco')
addt('ancient-technology','sacsayhuaman')
addt('origins-of-writing','khipu fuente-magna')
addt('hidden-kingdoms','paititi')
addt('lost-treasures','paititi el-dorado genghis-tomb')
addt('returning-saviours','paititi quetzalcoatl cortes-quetzalcoatl arthur viracocha')
addt('hidden-tombs','llullaillaco')
addt('sacred-kingship','llullaillaco')
C.update({
'bmac':'archaeology history lost-civilisations',
'arkaim':'archaeology history anomalies',
'issyk-golden-man':'archaeology history',
'scythian-amazons':'myth-legend archaeology history',
'ulugh-beg':'history science-cosmos',
'tamgaly':'archaeology religion aliens-ufo',
'dead-sea-scrolls':'history religion archaeology',
'copper-scroll':'history religion archaeology',
'derinkuyu':'archaeology history',
'ark-covenant':'religion myth-legend',
'durupinar':'religion hoaxes anomalies',
'etemenanki':'history archaeology religion myth-legend',
})
addt('lost-civilisations','bmac')
addt('civilisation-collapses','bmac')
addt('changed-understanding','bmac')
addt('ancestral-homelands','arkaim')
addt('outsider-builder-claims','arkaim')
addt('ancient-astronomy','arkaim ulugh-beg tamgaly')
addt('hidden-tombs','issyk-golden-man')
addt('sacred-kingship','issyk-golden-man')
addt('origins-of-writing','issyk-golden-man')
addt('warrior-women','issyk-golden-man scythian-amazons')
addt('knowledge-and-power','ulugh-beg dead-sea-scrolls')
addt('lost-evidence','ulugh-beg')
addt('sky-beings','tamgaly')
addt('hoaxes-exposed','dead-sea-scrolls durupinar')
addt('stories-proven-true','dead-sea-scrolls')
addt('lost-treasures','copper-scroll ark-covenant')
addt('sacred-relics','copper-scroll ark-covenant')
addt('underground-worlds','derinkuyu')
addt('ancient-technology','derinkuyu')
addt('flood-myths','durupinar')
addt('giant-monuments','etemenanki')
addt('creation-myths','etemenanki')
C.update({
'ban-chiang':'archaeology history',
'srivijaya':'history archaeology lost-civilisations',
'orang-pendek':'myth-legend anomalies',
'manananggal':'myth-legend',
'night-marchers':'myth-legend religion anomalies',
'latte-stones':'archaeology history myth-legend',
'rai-stones':'history archaeology',
'john-frum':'history religion aliens-ufo',
'tamam-shud':'history anomalies',
})
addt('changed-understanding','ban-chiang srivijaya')
addt('ancient-technology','ban-chiang')
addt('lost-civilisations','srivijaya')
addt('civilisation-collapses','srivijaya')
addt('ocean-voyagers','srivijaya rai-stones latte-stones')
addt('cryptids','orang-pendek')
addt('giants-and-little-people','orang-pendek latte-stones')
addt('shapeshifters','manananggal')
addt('strange-sounds','night-marchers')
addt('sacred-kingship','night-marchers')
addt('deep-oral-memory','night-marchers rai-stones latte-stones')
addt('giant-monuments','latte-stones rai-stones')
addt('sky-beings','john-frum')
addt('returning-saviours','john-frum')
addt('collective-experiences','john-frum')
addt('disappearances','tamam-shud')
addt('stories-proven-true','tamam-shud')
C.update({
'jericho-tower':'archaeology history science-cosmos religion',
'cave-of-swimmers':'archaeology science-cosmos',
'bigo-chwezi':'archaeology history myth-legend religion',
'pied-piper':'myth-legend history anomalies',
'carrington-event':'science-cosmos catastrophes history',
'the-hum':'anomalies science-cosmos',
'baltic-anomaly':'aliens-ufo anomalies hoaxes',
})
addt('giant-monuments','jericho-tower bigo-chwezi')
addt('ancient-astronomy','jericho-tower')
addt('changed-understanding','jericho-tower cave-of-swimmers')
addt('vanished-landscapes','cave-of-swimmers green-sahara')
addt('rain-and-drought','cave-of-swimmers')
addt('sacred-kingship','bigo-chwezi')
addt('deep-oral-memory','bigo-chwezi')
addt('outsider-builder-claims','bigo-chwezi')
addt('disappearances','pied-piper bigo-chwezi')
addt('strange-sounds','pied-piper the-hum')
addt('underground-worlds','pied-piper')
addt('collective-experiences','pied-piper the-hum')
addt('otherworld-visits','pied-piper')
addt('sky-omens','carrington-event')
addt('mysterious-lights','carrington-event')
addt('ufo-encounters','baltic-anomaly')
addt('hoaxes-exposed','baltic-anomaly')
# --- batch 9
C.update({
'late-heavy-bombardment':'science-cosmos catastrophes',
'ediacaran-biota':'science-cosmos',
'lascaux':'archaeology science-cosmos',
'varna-gold':'archaeology history lost-civilisations',
'carnac':'archaeology myth-legend anomalies',
'newgrange':'archaeology myth-legend religion science-cosmos',
'skara-brae':'archaeology history catastrophes',
'knossos-labyrinth':'myth-legend archaeology history',
'delphi-oracle':'religion history science-cosmos anomalies',
'tollund-man':'archaeology history religion',
'steppe-migration':'history archaeology science-cosmos',
})
addt('cosmic-impacts','late-heavy-bombardment')
addt('changed-understanding','late-heavy-bombardment ediacaran-biota delphi-oracle steppe-migration')
addt('mass-extinctions','ediacaran-biota')
addt('lost-evidence','ediacaran-biota')
addt('ancient-astronomy','lascaux carnac newgrange')
addt('altered-states','lascaux delphi-oracle dancing-plague')
addt('origins-of-writing','lascaux')
addt('knowledge-and-power','varna-gold delphi-oracle')
addt('sacred-kingship','varna-gold newgrange tollund-man knossos-labyrinth')
addt('lost-civilisations','varna-gold')
addt('civilisation-collapses','varna-gold')
addt('giant-monuments','carnac newgrange')
addt('petrified-beings','carnac')
addt('otherworld-visits','newgrange tollund-man')
addt('underground-worlds','newgrange knossos-labyrinth')
addt('hidden-tombs','newgrange')
addt('vanished-landscapes','skara-brae')
addt('stories-proven-true','skara-brae knossos-labyrinth')
addt('human-sacrifice','tollund-man llullaillaco knossos-labyrinth')
addt('mummies','tollund-man')
addt('genetic-migrations','steppe-migration tarim-mummies polynesia-america-contact kennewick-man neanderthal-dna americas-peopling')
addt('ancestral-homelands','steppe-migration arkaim')
C.update({
'tuniit':'archaeology history myth-legend',
'sedna':'myth-legend religion',
'franklin-expedition':'history archaeology',
'mesa-verde':'archaeology history',
'taino-ocean-gourd':'myth-legend religion',
'taino-survival':'history science-cosmos',
'port-royal':'history catastrophes religion',
'haitian-zombies':'religion anomalies history',
'bimini-road':'lost-civilisations anomalies hoaxes',
'bermuda-triangle':'anomalies hoaxes',
'chupacabra':'myth-legend anomalies hoaxes',
})
addt('giants-and-little-people','tuniit')
addt('deep-oral-memory','tuniit franklin-expedition')
addt('genetic-migrations','tuniit taino-survival')
addt('disappearances','tuniit franklin-expedition mesa-verde bermuda-triangle')
addt('otherworld-visits','sedna')
addt('underground-worlds','sedna')
addt('altered-states','sedna haitian-zombies')
addt('stories-proven-true','franklin-expedition taino-survival')
addt('sea-mysteries','franklin-expedition bermuda-triangle bimini-road port-royal mary-celeste draupner-wave valentich-1978 giant-squid')
addt('rain-and-drought','mesa-verde')
addt('civilisation-collapses','mesa-verde taino-survival')
addt('ancestral-homelands','mesa-verde aztlan')
addt('flood-myths','taino-ocean-gourd')
addt('creation-myths','taino-ocean-gourd')
addt('changed-understanding','taino-survival franklin-expedition')
addt('sunken-cities','port-royal bimini-road')
addt('lost-continents','bimini-road')
addt('lost-civilisations','bimini-road')
addt('hoaxes-exposed','bimini-road bermuda-triangle chupacabra')
addt('cryptids','chupacabra')
addt('monster-panics','chupacabra popobawa')
C.update({
'bhimbetka':'archaeology history myth-legend',
'mehrgarh':'archaeology history science-cosmos',
'sarasvati-river':'myth-legend religion science-cosmos archaeology',
'rakhigarhi-genome':'archaeology history science-cosmos',
'patala':'myth-legend religion',
'sigiriya':'history archaeology',
'gwion-gwion':'archaeology history lost-civilisations',
'tycho-supernova':'science-cosmos history religion',
'eyam-plague':'history catastrophes religion',
'beast-of-gevaudan':'history myth-legend anomalies',
'lisbon-1755':'catastrophes history religion science-cosmos',
})
addt('changed-understanding','bhimbetka mehrgarh tycho-supernova gwion-gwion lisbon-1755')
addt('origins-of-writing','bhimbetka')
addt('ancient-technology','mehrgarh')
addt('vanished-landscapes','sarasvati-river')
addt('rain-and-drought','sarasvati-river')
addt('civilisation-collapses','sarasvati-river')
addt('knowledge-and-power','sarasvati-river rakhigarhi-genome')
addt('genetic-migrations','rakhigarhi-genome')
addt('serpent-beings','patala')
addt('underground-worlds','patala')
addt('hidden-kingdoms','patala')
addt('sacred-kingship','sigiriya')
addt('outsider-builder-claims','gwion-gwion')
addt('sky-omens','tycho-supernova sn-1054')
addt('ancient-astronomy','tycho-supernova')
addt('plagues-and-epidemics','eyam-plague black-death dancing-plague tanganyika-laughter')
addt('collective-experiences','eyam-plague beast-of-gevaudan')
addt('cryptids','beast-of-gevaudan')
addt('shapeshifters','beast-of-gevaudan')
addt('monster-panics','beast-of-gevaudan')
addt('divine-punishment','lisbon-1755 port-royal eyam-plague')
C.update({
'war-of-the-worlds-1938':'history aliens-ufo hoaxes',
'philadelphia-experiment':'hoaxes anomalies history',
'flatwoods-monster':'aliens-ufo anomalies',
'socorro-zamora':'aliens-ufo anomalies history',
'kecksburg-1965':'aliens-ufo anomalies',
'mothman':'anomalies myth-legend',
})
addt('collective-experiences','war-of-the-worlds-1938 mothman')
addt('monster-panics','war-of-the-worlds-1938 flatwoods-monster mothman')
addt('hoaxes-exposed','war-of-the-worlds-1938 philadelphia-experiment flatwoods-monster')
addt('sea-mysteries','philadelphia-experiment')
addt('disappearances','philadelphia-experiment')
addt('ufo-encounters','flatwoods-monster socorro-zamora kecksburg-1965')
addt('lost-evidence','kecksburg-1965')
addt('mysterious-lights','flatwoods-monster kecksburg-1965')
addt('cryptids','mothman')
addt('sky-omens','mothman')
# --- batch 10 part 1 (Africa)
C.update({
'jebel-sahaba':'archaeology history',
'garamantes':'history archaeology lost-civilisations',
'carthage-tophet':'archaeology religion history',
'akhenaten':'history religion archaeology',
'pharaohs-curse':'hoaxes anomalies archaeology',
'taung-child':'science-cosmos archaeology',
'san-rock-art':'archaeology religion myth-legend',
'dahomey-amazons':'history',
'nzinga':'history',
'nongqawuse':'history religion',
})
addt('changed-understanding','jebel-sahaba taung-child carthage-tophet')
addt('human-origins','taung-child')
addt('civilisation-collapses','garamantes')
addt('rain-and-drought','garamantes san-rock-art')
addt('vanished-landscapes','garamantes jebel-sahaba')
addt('human-sacrifice','carthage-tophet')
addt('knowledge-and-power','akhenaten')
addt('lost-evidence','akhenaten')
addt('sacred-kingship','akhenaten nzinga')
addt('outsider-builder-claims','akhenaten')
addt('hidden-tombs','pharaohs-curse')
addt('mummies','pharaohs-curse akhenaten')
addt('hoaxes-exposed','pharaohs-curse')
addt('altered-states','san-rock-art')
addt('shapeshifters','san-rock-art')
addt('warrior-women','dahomey-amazons nzinga scythian-amazons')
addt('returning-saviours','nongqawuse')
addt('millenarian-movements','nongqawuse john-frum maya-2012')
addt('rejected-pioneers','taung-child wegener ediacaran-biota')
addt('giant-birds','taung-child haasts-eagle thunderbird')
# --- batch 10 part 2 (Mesoamerica, Native North America)
C.update({
'cholula':'archaeology myth-legend history',
'tenochtitlan-founding':'myth-legend history',
'la-llorona':'myth-legend anomalies',
'spiro-mounds':'archaeology history',
'skinwalker':'myth-legend anomalies aliens-ufo',
'ghost-dance':'history religion',
'white-sands-footprints':'archaeology science-cosmos',
'piasa':'myth-legend archaeology',
})
addt('giant-monuments','cholula')
addt('giants-and-little-people','cholula')
addt('flood-myths','cholula')
addt('divine-punishment','cholula')
addt('ancestral-homelands','tenochtitlan-founding aztlan')
addt('sky-omens','la-llorona ghost-dance')
addt('strange-sounds','la-llorona')
addt('lost-evidence','spiro-mounds')
addt('hidden-tombs','spiro-mounds')
addt('serpent-beings','spiro-mounds piasa tenochtitlan-founding')
addt('shapeshifters','skinwalker')
addt('ufo-encounters','skinwalker')
addt('mysterious-lights','skinwalker')
addt('returning-saviours','ghost-dance')
addt('millenarian-movements','ghost-dance')
addt('human-origins','white-sands-footprints')
addt('changed-understanding','white-sands-footprints')
addt('genetic-migrations','white-sands-footprints')
addt('giant-birds','piasa')
addt('cryptids','piasa')
