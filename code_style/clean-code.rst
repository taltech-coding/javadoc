Puhas kood (Clean code)
=======================

| Kood on puhas kui see on lihtsasti mõistetav mitte ainult autori, vaid ka teiste arendajate poolt. 
| Seega puhast koodi on lihtsam täiendada ja tõenäosus vigade tekkimiseks on väiksem lihtsasti mõistetavuse tõttu.

| Allpool on toodud välja mõned reeglid tuntud "Clean Code" by Robert C. Martin raamatust.

Üldised reeglid
----------------

* Järgi tavasid ja standarde, mis on varasemalt paika pandud.
* Lihtsam on parem. Vähendada keerukust niipalju kui võimalik.
* *Boy scout rule* - Tehes muudatusi koodibaasis, tuleb omapoolseid muudatusi teha korrapäraselt ja võimalusel/vajadusel korrastada olemasolevat koodi.
* Probleemi lahendades tuleb leida selle juurpõhjus, mis väldib ebakindlate *hack*-ide loomist.

Disaini reeglid
---------------

* Konfigureeritavad andmed peaksid olema lihtsasti leitavad (konfiguratsiooni failides), samas ei tasu konfigureeritavusega minna liiale.
* Eelistada polümorfismi ``if/else`` või ``switch/case``-dele.
* Kasutada *dependency injection*-i. Suurendab paindlikust vähendades koodi sidusust erinevate komponentide vahel.
* Klass peaks olema teadlik ainult temale vajalikest sõltuvustest.

Arusaadavuse parandamise reeglid
--------------------------------

* Ole järjepidev, kui teed midagi kindlat stiili järgides, siis tuleb seda teha lõpuni ühte moodi.
* Väldi eitavaid tingimusi.
* Väldi loogilisi sõltuvusi. Loogiliselt sõltuvad on meetodid, mis omakorda sõltuvad millegist muust samas klassis.

Nimetamise reeglid
------------------

* Nimed peavad olema arusaadavad. (halb: ``int d; // elapsed time in days``, parem: ``int elapsedTimeInDays;``)
* Nimed ei tohiks olla kaheti mõistetavad.
* *magic number*-id peaks olema asendatud konstantitega, mis ütlevad millega tegu.
* Kasuta otsitavaid nimesid.
* Kasuta hääldatavaid nimesid.
* Väldi nimede kodeerimist. (halb, I-Interface: ``IAnimal dog = new Dog();``, parem: ``Animal dog = new Dog();``)

Fuktsioonide reeglid
--------------------

* Väiksed.
* Teevad ühte asja.
* Funktsioonide nimed selgelt väljendavad, mida antud funktsioon teeb.
* Eelistada vähem argumente. Aitab hoida koodi rohkem loetavana.
* Funktsiooni väljakutse ei tohi tekitada kõrvalmõjusid.
* Ära kasuta lippe (*flag*), selle asemel tükelda funktsioonid mitmeks väiksemaks eraldi funktsiooniks.

Kommentaaride reeglid
---------------------

* Kommentaare tasub lisada ainult olukordades, kus need annavad reaalselt väärtust. Kasutute kommentaaride lisamine on müra, mis teeb koodi lugemise raskemaks. (halb: ``int elapsedTimeInDays; // elapsed time in days``, parem: ``int elapsedTimeInDays;``)
* Ära jäta alles väljakommeneeritud koodi, pigem eemalda. Hiljem ei mäleta keegi, milleks väljakomeneeritud read vajalikud olid.

Koodi struktuuri reeglid
------------------------

* Muutujad on deklareeritud lähedale nende kasutusele.
* Omavahel seotud kood peaks vertikaalselt asuma lähestikku.
* Read ei tohiks olla liiga pikad.

Testid
------

* Üks väide (*assert*) testi kohta. Võimaldab lihtsasti leida probleemse kohta.
* Testi sisu peab olema kiiresti mõistetav.
* Testid ei tohi üksteisest sõltuda.
* Testide tulemused peavad olema korratavad ehk ei sõltu keskkonnast, kus neid käivitatakse.
* Testid peavad jooksma kiiresti, et neid saaks tihedalt käivitada ja tänu sellele varakult vigu tuvastada.

Koodi hais (probleemsed kohad koodis)
-------------------------------------

* Jäik kood: koodi on keeruline muuta. Ühe väikse muudatuse tegemisega peab tegema omakorda järgmise muudatuse kuskil mujal.
* Habras kood: ühe muudatusega läheb suur osa ülejäänud koodist katki.
* Asjatu koodi kordamine. 
* Koodi on keeruline mõista.
