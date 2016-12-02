Java objektorienteeritud programmeerimise kontsept
==================================================
Enne alustamist, on paras teha väike sissejuhatus OOP'i.

Protseduurilises programmeerimises - mis on programmeerimine, mida me oleme siiamaani õppinud, programm on jaotatud väiksemateks osadeks, meetoditeks. Meetod töötab, kui eraldiseisev programmi osa, mida saab välja kutsuda ükskõik kust kohast programmi sees. Kui meetod kutsutakse välja, siis programmi täitmine liigub meetodi algusesse. Kui meetod on täidetud, pöördub programm tagasi sinna kohta, kust meetod oli välja kutsutud.

OOP-is, nagu ka protseduurilises programmeerimises, me püüame lammutada programmi veel väiksemateks osadeks. OOPi väiksemad osad on objektid. Igal eraldiseisval objektil on individuaalsed kohutstused: iga objekti sees on kindel hulk informatsiooni ning funktsionaalsust. Objekt-orienteeritud programm koosneb mitmetest objektidest, mis ühekoos määravad, kuidas programm hakkab töötama.

Esimeseks päriselt OOP keeleks võib nimetada Smalltalk'i. (*circa* 1970)
 

*OOP süsteem* 
-----------------------

**Objekt** Javas on sama kontseptsiooniga, mis **objekt** päris elus. Näiteks auto, pliiats, laud, tudeng jne. Objekt orienteeritud programmeerimine on metodoloogia, kuidas saab disainida programm kasutades klasse ning objekte. Üldiselt aitab selline lähenemine tarkvara loomist, tänu mõningatele võtmesõnadele

- Objekt
- Klass
- Pärimine (inheritance)
- Polümorfism (polymorphism)
- Abstraheerimine (abstraction)
- Kapseldamine (encapsulation)

1. Objekt

Üksus, millel on kindel olek ning käitumine. Näiteks: mootorratas, tool, klaviatuur, koer. Koera olekuks on värv, nimi, karva pikkus. Käitumiseks võiks olla näiteks haukumine, peremehe tervitamine.

2. Klass

Klassiks on objektide loomise plaan või üldistus. (blueprint for creating objects)

3. Polümorfism

On siis, kui ühte ja sama tegevust saab mitut erinevat moodi teha. Näiteks kui loomad teevad häält, siis koer hakkab haukuma ning part hakkab prääksuma. Javas kasutatakse selle tarvis **@Override** ja **@Overload** kontseptsioone.

4. Abstraheerimine

Kui me teeme telefonikõnesid, siis ei tea me täpselt, kuidas kogu side süsteem töötab. Javas toimib sarnane kontseptsioon, kus me peidame seesmisi detaile ning näitame ainult funktsionaalsust. Selle tarvis on javas **abstract class** ja **interface**.

5. Kapseldamine

Kapseldamine on mehhanism, mille abil väljad ning meetodid seotakse ühte kohta kokku. Kapseldamise korral on klassi väljad peidetud teiste klasside eest, kuid samas klassis asuvate *public* meetodite abil saavad teised klassid selle info kätte. Selle tarvis on javas **getterid** ja **setterid**

*Mis on OOP'i eelised protseduurilise programmeerimise ees?* 
------------------------------------------------------------

1. OOP aitab nii arenduduses, kui ka haldamises, kuna protseduurilist koodi ei ole lihtne hallata, kui koodi maht kasvab.
2. OOP lubab infot peita, samas kui protseduurilises programmeerimises infot võib saada kätte igalt poolt.
3. OOP tegeleb objektidega, ning seetõttu on palju lihstam simuleerida pärismaailma probleeme.
