JAR-faili koostamine
=========================

JAR - Java Archive võimaldab projekti kokku panna ühe faili. JAR-faili käivitamiseks pole JDK (Java Development Kit) olemasolu vajalik, piisab JRE-st (Java Runtime Environment). Sisuliselt on tegemist zip-formaadis kokku pakitud failidest, faili laiend on jar. JAR-faili sisu vaatamiseks võib selle avada mõne zip-formaati toetavad rakendusega. Võib ka faililaiendi muuta zip-iks, seejärel saab avada või lahti pakkida.

Näide, kuidas JavaFX-rakendusest saab koostada JAR-faili:
https://www.youtube.com/watch?v=An3WNgTtpR0

Ühe lihtsa näidisrakenduse kood on näidatud siin: https://gitlab.cs.ttu.ee/iti0011/materjalid/blob/master/javafx_jar/

Selle näite puhul on kõik failid pandud eraldi kausta "resources". IntelliJ-s on Project Structure -> Modules -> vastav moodul vaates määratud "resources" kaust eraldi kui "Resource Folder". Selleks saab kausta valida ja klikkida "Resources" nuppu. Kuigi see samm ei ole tingimata vajalik.

Selleks, et faile (pildid, helifailid, tekstifailid jms) õigesti lugeda, tuleb lugemiseks kasutada getResource() ja getRsourcesAsStream() meetodeid. Aga tuleb arvestada, et JAR-faili sisse faili kirjutada ei saa. Seega, kõik failid, kuhu midagi on vaja kirjutada, peavad olema JAR-failist väljaspool. Toodud näidisrakenduses on selline funktsionaalsus, et JAR-failis on seadete fail settings.txt. Kui kasutaja tahab seadeid muuta, siis ei saa seda faili JAR-faili tagasi kirjutada. See on lahendatud sedasi, et luuakse kohalikku arvuti kausta fail settings.txt. Edaspidi, kui selline fail on olemas, siis kasutatakse kasutaja seadeid. Kui sellist faili pole, siis loetakse JAR-failist vaikeseaded.

JAR-käivitamine käsurealt
----------------------------

Üldiselt peaks jar-faili saama käivitada selliselt nagu muid programme. Näiteks Windowsis topeltklikk jar-failil. Kui aga faili käivitamine ei õnnestu, siis tavaliselt mingit veateadet ei näidata. Selleks, et näha veateadet, tuleks jar-fail käivitada käsurealt.

Windowsis saate näiteks avada Exploreris jar-faili asukoha (kausta, kuhu IntelliJ genereerib jar-faili). Shift + parem hiire klikk avab menüü, kus on valik "Open command window here". See avab käsurea kohe vastavas kaustas.

Käsureal tuleks kirjutada nii:

.. code-block:: console

    java -jar Game.jar
    
Kus siis Game.jar on teie programmifaili nimi.
