Error: Output path is not specified
===================================

Kui te näete järgmist viga koodi käivitamisel

.. image:: /_images/intellij/project_output_1_error.png

toimige järgnevalt.

Samm 1: Project structure
---------------------------

Kui vajutate veateate "OK" nupul, avaneb projekti struktuuri seaded (sama asi avaneb File -> Project Structure ...).

Valige vasakult "Project". Peaksite nägema umbes sellist pilti:

.. image:: /_images/intellij/project_output_2_settings.png

Kõigepealt võite üle kontrollida, kas teil "Project language level" (joonisel sinise noolega) on määratud "8 - Lambdas, type annotations etc.).

"Project compiler output" lahter on teil tõenäoliselt tühi (nagu joonisel). Klikkige lahtri järel oleval "..." nupul (joonisel punase noolega). 

Samm 2: Projekti kausta valimine
---------------------------------

Avaneb umbes selline aken:

.. image:: /_images/intellij/project_output_3_project_home.png

Sealt peaksite oma projekti kausta üles otsima. Õnneks on sealsamas (punase ringiga tähistatud) nupp projekti kausta liikumiseks. Kui sellel klikkida,
tehakse projekti kaust aktiivseks. Sellest meile piisab, vajutame "OK".

Samm 3: määrame *output* kausta
---------------------------------

Seejärel kirjutage "Project compiler output" lahtrisse juurde "/out". Ehk siis me määrame IntelliJ-le kausta, kus ta hakkab kompileerimisega seonduvaid faile hoidma.

.. image:: /_images/intellij/project_output_4_set_out.png

Kui vastav väli on määratud, vajutada "OK". Nüüd peaks seadistused korrektsed olema ja koodi saab käivitada.

Kui programm endiselt ei käivitu
-----------------------------------

Vaata, et ühegi mooduli all ei oleks mingit imelikku seadistust. Kõige mõistlikum oleks teha nii, et iga mooduli juures oleks märgitud, et ta kasutab projekti üldisi seaditusi. Selleks võta moodul ja *paths* saki alt määra "Inherit project compile output path":

.. image:: /_images/intellij/project_output_5_module_paths.png
