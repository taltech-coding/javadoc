*JavaFX*
=======

*JavaFX* on graafika- ning meediapakettide *library*, mis võimaldab arendajatel luua erinevaid desktoprakendusi või
*rich internet application*'e (RIA) ehk installeeritavaid internetirakendusi, milleks võivad olla näiteks brauseri *plugin*'id.
*JavaFX* on Java API, mis tähendab, et *JavaFX* rakenduse koodis võib kasutada ka tesi API'sid ükskõik millistest Java *library*'test.

*JavaFX*'i kasutamiseks on mitemeid erinevaid võimalusi, näiteks saab rakenduse kujunduse loomiseks kasutada CSS faile,
samuti on võimalik eraldi luua rakenduse *backend* kasutades Java koodi ning *frontend* kasutades spetsiaalset FXML skriptimiskeelt.
*JavaFX* kasutajaliideseid saab luua ka koodi kirjutamata, selle jaoks on loodud eraldi rakendus *SceneBuilder*, 
mis aitab lihtsalt luua kujundust ja rakenduse visuaalset ülesehitust,
ning aitab kergelt siduda Javas kirjutatud rakenduse loogika (meetodid)
ning kujunduselemendid (erinavad *JavaFX* objektid). *SeneBuilder* loob ise FXML faili sisu,
rakenduse loojal tuleb ainult vajalikud elemendid ekraanil õigesse kohta panna.

Kust saada *JavaFX*?
------------------

*JavaFX* API on *Java Runtime Environment*'i (JRE) ning *Java Development Kit*'i (JDK) osaks,
seega pole seda tarvis eraldi alla tõmmata.

Kust saada *SceneBuilder*?
-------------------------

Nagu eelnevalt mainitud, pole *SceneBuilder*'it otseselt tarvis, et luua *JavaFX* rakendusi,
kuid alustuseks on seda märksa mugavam (ning võib-olla ka lõbusam) kasutada.
IntelliJ pakub ka võimalust, mis laseb *SceneBuilder*'it kasutada otse koodikirjutamiseks mõeldud aknaga analoogses aknas. 

*SceneBuilder*'i saab alla laadida järgnevalt lingilt:
http://gluonhq.com/labs/scene-builder/

.. image:: https://github.com/tutjava/materjalid/blob/master/images/JavaFXSceneBuilder.png

Kuidas luua *JavaFX* projekti?
------------------------------

IntelliJ's saab *JavaFX* rakenduse luua järgmiselt:

- Vali *File* -> *new Project*
- Avanenud akna vasakus ääres olevast nimekirjast valida *Java FX* ning seejärel vajutada *next*
- Vali asukoht projektile ning anna sellele nimi
- IntelliJ loob automaatselt FXML faili nimega *sample.fxml*
- Seda faili saab avada *SceneBuilder*'is, selleks tee paremklikk faili nimel ning vali menüüst *Open in SceneBuilder*

Abiks on ka:
http://docs.oracle.com/javafx/scenebuilder/1/use_java_ides/sb-with-intellij.htm

Eclipse'is projekti loomise juures on abiks:
http://docs.oracle.com/javafx/scenebuilder/1/use_java_ides/sb-with-eclipse.htm





