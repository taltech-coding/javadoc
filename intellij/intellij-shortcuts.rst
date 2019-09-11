IntelliJ kiirklahvid
=======================

Vaikimisi kiirklahve (*keyboard shortcut*) saab vaadata menüüst Help -> Keymap Reference (avaneb PDF, milles on vaikeseadistuses määratud kiirkahvid). Kui mõni kiirklahv ära muuta, siis see seal ei kajastu.

Koodikirjutamine
------------------

:code:`alt` + :code:`shift` + :code:`üles/alla` - märgistatud ridade (või kui midagi märgistatud pole, siis aktiivse rea) liigutamine üles/alla.

:code:`ctrl` + :code:`shift` + :code:`üles/alla` - märgistatud ridade kontekstitundlik liigutamine üles/alla. Liigutamisel võetakse arvesse, millisel tasandil liigutatav kood on. Näiteks ei saa liigutada koodi meetodist välja. Samuti lisatakse vajalik taane.

:code:`ctrl` + :code:`D` - märgistatud koodi kopeerimine allpoole. Kui koodi märgistatud ei ole, kopeerib aktiivse rea allapoole.

:code:`ctrl` + :code:`Y` - märgistatud ridade kustutamine. Kui midagi märgistatud pole, kustutatakse aktiivne rida.

:code:`shift` + :code:`F6` - muutuja/meetodi nime muutmine. Nimi muudetakse ära terve koodi ulatuses. Näiteks kui koodis on muutuja :code:`a`, saab selle klahvikombinatsiooniga muuta selle muutuja igal pool näiteks :code:`minNumber` vastu.

:code:`alt` + :code:`shift` + :code:`klikk` - lisab tekstikursori (*caret*) klikitud positsioonile. Mitme tekstikursoriga saab sama teksti kirjutada mitmesse kohta korraga.

:code:`ctrl` + :code:`tühik` - koodisoovitus: esimesel korral pakub kättesaadavaid klasse ja meetodeid, teisel korral pakub lisaks hetkel mitte kättesaadavaid klasse ja meetodeid.

Koodis ringi liikumine
--------------------------

:code:`ctrl` + :code:`hiire vasak klikk` või :code:`ctrl` + :code:`B` - avab meetodi või muutuja deklaratsiooni.

:code:`ctrl` + :code:`N` - saab otsida klasse nime järgi.

:code:`ctrl` + :code:`shift` + :code:`N` - saab otsida faili nime järgi. Kui otsingus kirjutada nime järgi "/", otsitakse kaustu. Näiteks saab otsida moodulit EX10, kui kirjutada "EX10/". Samamoodi pakette, näiteks "EX10/src/".

:code:`shift`, :code:`shift` (kaks korda) - avab otsingu, mis otsib kõikjalt. Lisaks klassidele otsitakse faili nimedest, muutujaid jms.

:code:`alt` + :code:`F7` - leiab koodist kõik muutuja/meetodi/klassi kasutuskohad.

Abi
----------

:code:`ctrl` + :code:`Q` - avab väikese dialoogiakna, milles antakse aktiivse klassi/meetodi/muutuja kohta abi. See avab javadoci. Üldiselt iga Java standardteegis oleva meetodi kohta on javadoc piisavalt informatiivne, et sealt vajalik info kätte saada. Abitekstis olevaid linke (näiteks mõne klassi nime juures) saab klikkida ja seejärel avaneb dialoogis vastava klassi informatsioon jne. Kui dialoogiakna avanemise korral uuesti :code:`ctrl` + :code:`Q` vajutada, avaneb sama dialoog suuremalt.

IntelliJ saab seadistada selliselt, et hiirega meetodi peale liikudes näidatakse abiteksti. Seda saab seadistada: File -> Settings -> Editor -> General -> "Show quick documentation on mouse move". Vaikimisi on see maas, kui see ära märgistada, näidatakse abiteksti vastavalt seadistatud aja pärast (näiteks 500 ms).



