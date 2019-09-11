Stiilivigade näitamine IntelliJ's
==================================

Lisame IntelliJ-sse Checkstyle-IDEA nimelise laienduse (*plugin*),
mis kontrollib koodi juba kirjutamise ajal.

Samm 1: Seaded
---------------

Avage seaded:

.. image:: /_images/intellij/checkstyle_1_file_settings.png

Samm 2: *Plugins* menüü
-------------------------

Avage vasakult *Plugins* menüü (punase noolega märgistatud):

.. image:: /_images/intellij/checkstyle_2_plugins.png

Klikkige all oleval "Browse repositories.." nuppu (punase noolega märgistatud)

Samm 3: Otsige õige *plugin* üles
---------------------------------

Avaneb laienduste valikuga aken:

.. image:: /_images/intellij/checkstyle_3_install.png

Joonisel märgistatud numbrid:

 1. kirjutage otsingulahtrisse "checkstyle"
 2. valige nimekirjast "Checkstyle-IDEA"
 3. klikkige "Install" nupul
 
Samm 4: IntelliJ restart
--------------------------

Vajutage "Restart IntelliJ IDEA" nuppu.

.. image:: /_images/intellij/checkstyle_4_restart.png

Samm 5: Checkstyle seaded
--------------------------

Avage uuesti seaded (File -> Settings).

Kirjutage vasakule üles otsingulahtrisse "checkstyle". Seejärel näidatakse teile vasakul vaid seda osa menüüst, mis sisaldab otsisõna.

.. image:: /_images/intellij/checkstyle_5_settings.png

Valige Other Settings -> Checkstyle.

Samm 6: Aine konfiguratsioon
------------------------------

Vaikimsi kaasas olev seadistus on liiga karm. Kasutame ITI0011 aines määratud seadistust.

.. image:: /_images/intellij/checkstyle_6_new_conf.png

Joonisel tähistatud numbrid:
 1. vajutage paremal rohelise "+" märgi peal, avaneb uus aken
 2. Uues aknas kirjutage uue seadistuse nimetus
 3. Vajutage "Browse" ja otsige üles ainega seotut XML-faili (saate ained.ttu.ee -> 1. nädal -> iti0011.xml alla laadida).
 
Vajutage "Next" ja sulgele aken. 

Samm 7: Aktiveerimine
----------------------

Peale konfiguratsiooni lisamist tuleb see ka aktiveerida.

.. image:: /_images/intellij/checkstyle_7_activate.png

Selleks märgistage valikuruut loodud seadistuse ees (joonisel punane ring ümber tehtud).

Samm 8: Näidis
-----------------

Näide koodist:

.. image:: /_images/intellij/checkstyle_8_example.png

*main* meetodil on *args* parameetri kirjeldus puudu. Seepärast on selle taust esile toodud teise värviga.

*hello* meetodil on kogu javadoc puudu. *public* võtmesõna on punase kirjaga. Kui sellele hiirega peale liikuda,
antakse ka vastav teade, et javadoc on puudu.

