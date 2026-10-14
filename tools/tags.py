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
