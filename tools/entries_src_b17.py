# Batch 17 (2026-11-04): Polynesia/Pacific, Central Asia, Caribbean, Southern/East Africa, deep prehistory, early modern science
H,M='history','myth'
def X(id,title,lane,status,pr,start,ev,main,alts,src,img=None,end=None,changed=None,dateNote=None):
  d=dict(id=id,title=title,lane=lane,status=status,priority=pr,start=start,end=end,ev=ev,main=main,alts=alts,src=src,img=img)
  if changed:d['changed']=changed
  if dateNote:d['dateNote']=dateNote
  return d
E=[]
# --- part 1: Polynesia and the Pacific
E+=[
X('rangi-papa','Ranginui and Papatuanuku: the separation of sky and earth',M,'myth-legend',2,1300,['oral tradition'],
 "In Maori tradition the sky father Ranginui and earth mother Papatuanuku lay locked in an embrace, their children trapped in darkness between them. The forest god Tane pushed them apart, letting light into the world; Rangi's tears are the rain and mist. Versions of a sky-earth separation are found across Polynesia and in many other cultures worldwide, including Egyptian (Geb and Nut) and Chinese (Pangu) stories.",
 [('Comparative mythology','Some scholars treat the separation of sky and earth as one of the most widespread creation motifs, possibly very ancient; others see independent invention of an intuitive image.')],
 ['wiki:Rangi_and_Papa'],img='Rangi_and_Papa',dateNote='Oral tradition; first written down in the 19th century'),
X('kumulipo','The Kumulipo: a Hawaiian creation chant',M,'myth-legend',3,1700,['oral tradition','textual'],
 "The Kumulipo is a Hawaiian genealogical chant of over 2,000 lines tracing the origin of the world from darkness (po), through the emergence of coral polyps, sea creatures, plants and animals, to gods and the chiefly line of Hawaii. It was composed for the chief Ka-I-imamao around the early 18th century and published by King Kalakaua in 1889; Queen Liliuokalani translated it into English in 1897. Its sequence from simple sea life to humans is often compared to evolution.",
 [('Evolutionary reading','Some modern readers see the chant as an indigenous anticipation of evolution; most scholars regard it as a genealogical cosmology whose order reflects Hawaiian ideas of kinship between all living things.')],
 ['wiki:Kumulipo'],img='Kumulipo'),
X('taniwha','Taniwha: Maori guardian water beings',M,'myth-legend',3,1300,['oral tradition'],
 "Taniwha are powerful beings in Maori tradition living in rivers, lakes, caves and the sea. Some are protective guardians of a tribe, others dangerous. They remain culturally significant: in 2002 concerns about a taniwha named Karutahi were raised by Ngati Naho during the construction of a State Highway 1 section near Meremere, and the road was rerouted in consultation.",
 [('Natural hazards','Some researchers suggest taniwha stories encoded knowledge of dangerous waters, floods and unstable ground.')],
 ['wiki:Taniwha'],img='Taniwha'),
X('tupaia-chart','Tupaia and his chart of the Pacific',H,'confirmed',2,1769,['textual','cartographic'],
 "Tupaia, a Raiatean priest and navigator, joined James Cook's Endeavour in 1769 at Tahiti. He produced a chart showing some 74 islands spread across a vast area of the Pacific, combining Polynesian navigational knowledge with European mapping. He guided the ship and acted as interpreter in New Zealand, where Maori addressed him rather than Cook. He died in Batavia in 1770. How to read his chart was long debated; scholars since the 2010s argue it uses a navigator-centred system of directions rather than a European north-up grid.",
 [('Reinterpretation','Earlier historians dismissed the chart as muddled; recent analyses argue it accurately encodes sailing directions from Tahiti.')],
 ['wiki:Tupaia_(navigator)'],img='Tupaia_(navigator)',changed="Long considered inaccurate; re-read from the 2010s as a coherent Polynesian wayfinding map."),
X('taputapuatea','Taputapuatea marae: centre of the Polynesian world',H,'confirmed',2,1000,['archaeological','oral tradition'],
 "Taputapuatea on Raiatea in French Polynesia is a ceremonial complex of marae (sacred stone platforms) that was a political and religious centre of eastern Polynesia, associated with the god Oro. Voyagers from across the region reportedly gathered there, and stones from it were taken to found new marae elsewhere. It became a UNESCO World Heritage Site in 2017.",
 [('Hawaiki','Raiatea (formerly Havai\'i) is often linked with Hawaiki, the legendary Polynesian homeland, though Hawaiki may be a mythic as well as geographic place.')],
 ['wiki:Taputapuatea_marae'],img='Taputapuatea_marae'),
X('moriori','The Moriori of the Chatham Islands',H,'confirmed',2,1500,['oral tradition','genetic','textual'],
 "The Moriori are the Polynesian people of the Chatham Islands (Rekohu), east of New Zealand, who settled there from mainland New Zealand around the 16th century. They adopted Nunuku's law, a code forbidding war and killing. In 1835 Maori groups from Taranaki invaded; many Moriori were killed or enslaved. A myth arose in the 19th and 20th centuries that Moriori were a pre-Maori race in New Zealand displaced by Maori; this is rejected by historians.",
 [('Pre-Maori race myth','Once taught in New Zealand schools, the idea that Moriori were earlier, Melanesian inhabitants of mainland New Zealand was debunked by linguistic and archaeological work from the 1960s onwards.')],
 ['wiki:Moriori'],img='Moriori',changed="Pre-Maori race theory popular c.1900-1960s; now discredited."),
X('taupo-hatepe','Hatepe eruption of Lake Taupo',H,'confirmed',2,232,['geological','radiocarbon'],
 "The Hatepe eruption of the Taupo volcano in New Zealand around 232 CE (plus or minus about 10 years) was one of the most violent eruptions of the last 5,000 years, with pyroclastic flows covering some 20,000 square km. New Zealand was uninhabited at the time. Claims that it produced red skies recorded in Rome and China have not been substantiated.",
 [('Historical records','Some writers link sky phenomena in ancient Roman and Chinese texts to the eruption; ice-core and dating studies do not support those links.')],
 ['wiki:Hatepe_eruption'],img='Lake_Taupo'),
X('kon-tiki','Kon-Tiki expedition',H,'confirmed',2,1947,['experimental','documentary'],
 "In 1947 Thor Heyerdahl and five companions sailed the balsa raft Kon-Tiki from Peru to the Tuamotu Islands, about 6,900 km, to show South Americans could have reached Polynesia. The voyage succeeded, but his theory that Polynesia was settled from the Americas was rejected: linguistics, archaeology and genetics show Polynesians came from Island Southeast Asia. A 2020 genetic study did find evidence of some contact between Polynesians and Native Americans around 1200 CE.",
 [('Heyerdahl theory','Heyerdahl argued for American (and even bearded white) settlers of Polynesia; this is not supported, although limited trans-Pacific contact is now accepted.')],
 ['wiki:Kon-Tiki_expedition'],img='Kon-Tiki_expedition'),
X('bounty-pitcairn','Mutiny on the Bounty and the Pitcairn settlement',H,'confirmed',2,1789,['textual','archaeological'],
 "In 1789 sailors led by Fletcher Christian mutinied against Lieutenant William Bligh on HMS Bounty. Bligh and 18 loyalists crossed some 6,700 km in an open boat to Timor. The mutineers, with Tahitian companions, settled the uninhabited Pitcairn Island in 1790 and burned the ship. They were not found until 1808, when only one mutineer, John Adams, survived. Their descendants still live on Pitcairn and Norfolk Island. Pitcairn had earlier been settled by Polynesians, who left before Europeans arrived.",
 [('Christian\'s fate','Rumours persisted that Fletcher Christian escaped back to England; there is no reliable evidence.')],
 ['wiki:Mutiny_on_the_Bounty'],img='Mutiny_on_the_Bounty'),
X('moa-extinction','Moa: the giant birds of New Zealand',H,'confirmed',2,1400,['archaeological','radiocarbon','genetic'],
 "Moa were nine species of flightless birds in New Zealand, the largest standing up to about 3.6 m with neck extended. They were hunted to extinction within about 100-200 years of Polynesian settlement around 1300 CE, one of the fastest human-caused megafauna extinctions known. Their only predator had been Haast's eagle, which died out with them. Occasional claims of moa surviving into the 20th century are unsupported.",
 [('Surviving moa','Reports such as a 1993 photo of a supposed moa in the Craigieburn Range are treated as hoaxes or misidentifications.')],
 ['wiki:Moa'],img='Moa'),
]
