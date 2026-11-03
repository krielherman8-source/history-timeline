# Batch 16 (2026-11-03): Etruscans and the classical/Aegean Mediterranean, Russia and the North Pacific/Arctic,
# Japan and Mesoamerica, 20th-century UFO investigations, scientific hoaxes and anomalies
H,M='history','myth'
def X(id,title,lane,status,pr,start,ev,main,alts,src,img=None,end=None,changed=None,dateNote=None):
  d=dict(id=id,title=title,lane=lane,status=status,priority=pr,start=start,end=end,ev=ev,main=main,alts=alts,src=src,img=img)
  if changed:d['changed']=changed
  if dateNote:d['dateNote']=dateNote
  return d
E=[]
# --- part 1: Etruscans, Aegean scripts, Egypt and Rome
E+=[
X('etruscan-origins','Where did the Etruscans come from?',H,'disputed',2,-900,['textual','archaeological','genetic (ancient DNA)','linguistic'],
 "The Etruscans dominated central Italy from roughly the 9th century BCE until they were absorbed by Rome, speaking a non-Indo-European language that is readable (it uses a Greek-derived alphabet) but still only partly understood. Ancient writers disagreed about their origin: Herodotus said they came from Lydia in Anatolia, while Dionysius of Halicarnassus said they were native to Italy. Most archaeologists trace Etruscan culture to the local Villanovan culture, and a 2021 ancient-DNA study (Posth et al., Science Advances) found that Etruscans were genetically similar to their Latin neighbours, with steppe-related ancestry and no sign of a recent Anatolian migration.",
 [('Lydian migration','The Herodotus account of a migration from Lydia was long popular and some earlier modern DNA studies of cattle and present-day Tuscans were read as supporting an eastern link; the 2021 ancient-DNA results weigh against this.'),
  ('Language puzzle','Because Etruscan is related only to the scarcely attested Raetic and Lemnian languages, some researchers propose an Aegean or Alpine connection for the language even if the population was largely local.')],
 ['wiki:Etruscan_origins','doi:10.1126/sciadv.abi7673','wiki:Etruscan_civilization'],img='Etruscan_civilization',
 changed="Debated since antiquity; archaeology from the 20th century favoured local origins, and ancient DNA in 2021 found no recent Anatolian ancestry."),
X('liber-linteus','Liber Linteus: an Etruscan book wrapped around an Egyptian mummy',H,'confirmed',3,-250,['textual','archaeological'],
 "The Liber Linteus Zagrabiensis is the longest surviving Etruscan text and the only known surviving linen book from antiquity. It was cut into strips and used to wrap a female mummy in Ptolemaic Egypt; a Croatian official bought the mummy in Alexandria in 1848 and it is now in the Archaeological Museum in Zagreb. Only in 1891-92 was the writing identified as Etruscan. Its roughly 1,200 legible words appear to form a ritual calendar listing ceremonies and offerings to gods, dated to around the 3rd century BCE.",
 [('Why in Egypt','How an Etruscan religious book ended up as mummy wrappings is unknown; suggestions include an Etruscan community in Egypt or linen simply being reused, and none is proven.')],
 ['wiki:Liber_Linteus'],img='Liber_Linteus'),
X('pyrgi-tablets','Pyrgi Tablets: an Etruscan-Phoenician bilingual',H,'confirmed',3,-500,['textual','archaeological'],
 "Three gold sheets found in 1964 at Pyrgi, the harbour sanctuary of the Etruscan city of Caere, record a dedication by the ruler Thefarie Velianas to the goddess Uni, identified with the Phoenician Astarte, around 500 BCE. Two are in Etruscan and one in Phoenician, making them a partial bilingual text that has helped scholars understand Etruscan vocabulary, though the two versions are not word-for-word translations. They also show close Etruscan-Carthaginian ties at the time.",
 [('Interpretation','Scholars debate whether the dedication implies Phoenician/Carthaginian political influence over Caere or simply religious and trade links.')],
 ['wiki:Pyrgi_Tablets'],img='Pyrgi_Tablets'),
X('phaistos-disc','Phaistos Disc',H,'disputed',2,-1700,['archaeological','textual'],
 "A fired clay disc about 16 cm across, found in 1908 by Luigi Pernier in the Minoan palace of Phaistos on Crete, is stamped on both sides with 241 impressions of 45 different signs arranged in a spiral, made with individual punches, an early form of movable-type printing. It is usually dated to the Middle or Late Minoan Bronze Age (roughly 1850-1600 BCE). The script matches no other known find, and with so short a text it has not been deciphered; most specialists think it cannot be without further examples.",
 [('Proposed decipherments','Many readings have been published, as Greek, Luwian, Minoan prayers, a calendar or a game board; none has gained scholarly acceptance.'),
  ('Forgery suggestion','A minority view (e.g. Jerome Eisenberg, 2008) argues the disc is a modern forgery; this is not widely accepted and the museum has not permitted thermoluminescence testing.')],
 ['wiki:Phaistos_Disc'],img='Phaistos_Disc'),
X('linear-a','Linear A: the undeciphered Minoan script',H,'confirmed',2,-1800,['textual','archaeological'],
 "Linear A was used by the Minoans of Crete from about 1800 to 1450 BCE, mostly on clay tablets recording goods. Its successor Linear B was deciphered by Michael Ventris in 1952 as an early form of Greek, so many Linear A signs can be given approximate sound values, but the resulting words do not match Greek or any known language and the script remains undeciphered.",
 [('Language family','Proposals link the underlying Minoan language to Luwian/Anatolian, Semitic, Indo-Iranian or Tyrsenian (Etruscan-related) languages; none is generally accepted.')],
 ['wiki:Linear_A'],img='Linear_A'),
X('tutankhamun-tomb',"Tutankhamun's tomb and the 'curse'",H,'confirmed',1,-1323,['archaeological','textual'],
 "Howard Carter, funded by Lord Carnarvon, found the almost intact tomb KV62 of the boy king Tutankhamun (died c. 1323 BCE) in the Valley of the Kings in November 1922. It held over 5,000 objects, including the gold mask. Carnarvon's death in April 1923 from an infected mosquito bite fuelled press stories of a 'curse'; studies of the people present at the opening found no unusual death rates. CT scans and DNA work (2010) examined his health and family, suggesting he was a son of Akhenaten.",
 [('Hidden chambers','In 2015 Nicholas Reeves proposed hidden chambers behind the tomb walls, possibly the tomb of Nefertiti; radar surveys gave conflicting results and the idea remains unconfirmed.'),
  ('Curse','The curse story is treated by historians as a media creation; some writers have suggested mould or bacteria in sealed tombs could cause illness, which is speculative for this case.')],
 ['wiki:Tutankhamun','wiki:KV62','doi:10.1001/jama.2010.121'],img='Tutankhamun',
 changed="Found 1922; curse stories 1923; DNA and CT study 2010; hidden-chamber debate since 2015."),
X('sea-peoples','The Sea Peoples',H,'disputed',2,-1200,['textual','archaeological'],
 "Egyptian records, above all the reliefs of Ramesses III at Medinet Habu (c. 1175 BCE), describe a confederation of seafaring invaders, including the Peleset, Sherden, Shekelesh and Denyen, who attacked Egypt and the eastern Mediterranean at the end of the Bronze Age. The modern term 'Sea Peoples' dates from the 19th century. The Peleset are widely identified with the Philistines, whose settlement in southern Canaan is supported by ancient DNA showing a European-related component (Feldman et al., 2019). Their role in the wider Bronze Age collapse is debated.",
 [('Cause or symptom','Some historians see the Sea Peoples as the main cause of the collapse; others see them as displaced people fleeing drought, famine, earthquakes and systems failure.'),
  ('Origins','Homelands proposed include the Aegean, western Anatolia, Sardinia (Sherden) and Sicily (Shekelesh), based on name similarities that are not proven.')],
 ['wiki:Sea_Peoples','doi:10.1126/sciadv.aax0061'],img='Sea_Peoples'),
X('nemi-ships',"Caligula's Nemi ships",H,'confirmed',3,40,['archaeological','textual'],
 "Two huge ships, about 70 and 73 metres long, were built on the small volcanic Lake Nemi near Rome for the emperor Caligula (reigned 37-41 CE), apparently as floating palaces and temples. Legends of the sunken ships persisted for centuries and divers recovered pieces from the 15th century onwards. Mussolini's government drained the lake in 1928-32 to recover them, revealing advanced features such as bilge pumps and rotating platforms on bearings. They were displayed in a purpose-built museum but burned in 1944 during the Second World War; who set the fire is disputed.",
 [('The 1944 fire','An Italian commission blamed retreating German troops; others have suggested American shelling or local looters. It has never been settled.')],
 ['wiki:Nemi_ships'],img='Nemi_ships'),
X('talos-automaton','Talos, the bronze giant of Crete',M,'myth-legend',3,-700,['textual','iconographic'],
 "In Greek myth Talos was a giant bronze man made by Hephaestus (or given to Minos by Zeus) who circled Crete three times a day, throwing rocks at ships. He had a single vein closed by a bronze nail; in Apollonius of Rhodes' Argonautica (3rd century BCE) Medea brings about his death and the ichor drains out. He is often cited as one of the earliest imagined robots or automata, and appears on a 5th-century BCE vase, the Talos Vase.",
 [('Ancient technology readings','Classicist Adrienne Mayor (Gods and Robots, 2018) explores Talos as evidence that ancient Greeks imagined artificial life and automata; claims that the myth preserves memories of real ancient robots are speculative and not supported.')],
 ['wiki:Talos'],img='Talos'),
X('herculaneum-papyri','Herculaneum papyri and the Vesuvius Challenge',H,'confirmed',2,79,['archaeological','textual','computational imaging'],
 "About 1,800 carbonised papyrus scrolls were found from 1752 in the Villa of the Papyri at Herculaneum, buried by Vesuvius in 79 CE; it is the only intact library known from the classical world. Many were damaged by early attempts to unroll them. Most of those read so far are Epicurean works, many by Philodemus. From 2015, X-ray tomography and later machine learning allowed unopened scrolls to be read virtually; in 2023-24 the Vesuvius Challenge prize was won by students who recovered passages from a sealed scroll, apparently by Philodemus on pleasure. In 2025 researchers reported reading the title of another scroll.",
 [('Unexcavated library','Parts of the villa remain unexcavated and some scholars hope more scrolls, perhaps including lost Latin or Greek works, are still buried; this is unproven.')],
 ['wiki:Herculaneum_papyri','wiki:Vesuvius_Challenge','wiki:Villa_of_the_Papyri'],img='Herculaneum_papyri',
 changed="Found 1752; destructive unrolling 18th-19th c.; virtual unrolling from 2015; Vesuvius Challenge readings 2023-25."),
]
