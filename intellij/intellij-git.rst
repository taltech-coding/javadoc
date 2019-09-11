Git'i kasutamine IntelliJ'ga
=============================

Kui soovite git'i kasutada läbi IntelliJ, käituge järgmiselt

Samm 1: *Checkout from git*
----------------------------

.. image:: /_images/intellij/git_1_checkout.png

Samm 2: Salve aadress
----------------------

.. image:: /_images/intellij/gitlab_2_clone.png

Samm 3: Testime salve aadressi
-------------------------------

Veenduge, et salv on kättesaadav. Sisestage oma uniid ja parool:

.. image:: /_images/intellij/gitlab_3_1_login.png

Kui kõik õnnestub, peaksite nägema sellist teadet:

.. image:: /_images/intellij/gitlab_3_2_test.png

Seejärel kloonime projekti:

.. image:: /_images/intellij/gitlab_3_3_clone.png

Samm 4: Uus projekt
-------------------

.. image:: /_images/intellij/gitlab_4_new_project.png

Samm 5: Projekti importimine, 1. samm
----------------------------------------

.. image:: /_images/intellij/git_5_import.png

Samm 6: Projekti nimi
------------------------------

.. image:: /_images/intellij/gitlab_6_project_location.png

Samm 7: Lähtefailide asukoht
------------------------------

.. image:: /_images/intellij/gitlab_7_import_projects.png

Samm 8: Info raamistike kohta
------------------------------
.. image:: /_images/intellij/git_8_no_frameworks.png

Samm 9: Uue mooduli loomine ülesande jaoks
----------------------------------------------

Kui salv on kloonitud, loome ülesande jaoks uue mooduli.
Sarnaselt tuleks käituda iga ülesande puhul.

Parem klikk projekti nimel, sealt valida New -> Module.

.. image:: /_images/intellij/gitlab_9_new_module.png

Samm 10: Uue mooduli aken
---------------------------

Kui teil on seadistamata JDK (Java Development Kit), tasub see siin kohe ära teha.
Võite selle läbi teha ka hiljem.

.. image:: /_images/intellij/module_1_new.png

JDK seadistamine seadete kaudu
---------------------------------

Kui te pole veel JDK asukohta määranud, saate seda teha projekti struktuuri juurest.
File -> Project Structure. Avaneb selline vaade:

.. image:: /_images/intellij/jdk_1_settings.png

Kui Project SDK on määramata, lisage uus JDK.

Samm 11: JDK seadistamine
--------------------------

Otsige oma arvutist üles installeeritud Java Development Kit (jdk kaust).

.. image:: /_images/intellij/jdk_2_path.png

Kui teil "Project language level" ei ole juba "8 - Lambdas, ...", siis määrake see:

.. image:: /_images/intellij/jdk_3_language_level.png

Mooduli nimi
-------------

Jätkame mooduli seadistamisega. Kui olete jõudnud teise sammu, määrake mooduli nimi. Kasutage ülesande koodi. Sisuliselt teeb see selle nimega kausta teie salve.

.. image:: /_images/intellij/module_2_name.png

Uus pakk (*package*)
--------------------

Lisage uus pakk uue mooduli alla:

.. image:: /_images/intellij/module_3_new_package.png

Määrage pakile nimi:

.. image:: /_images/intellij/module_4_package_name.png

Punkt paki nimes tähistab hierarhiat. Ehk siis ``ee`` paki all on pakk ``ttu`` jne. Tegelikult luuakse vastavad kaustad failisüsteemi (``src/ee/ttu/iti0202/hello/``).

Uus klass
-----------

Looge uus vajalik klass:

.. image:: /_images/intellij/module_5_new_class.png

Määrake klassi nimi (vaadake ülesande tekstist):

.. image:: /_images/intellij/module_6_class_name.png

Faili lisamine (*git add*)
--------------------------------

Peale mooduli/klassi jms loomist võib IntelliJ ise küsida, kas loodav fail panna Giti. Võite kohe ``yes`` valida.

.. image:: /_images/intellij/module_7_add_file_to_git.png

Mõistlik oleks ka .iml failid Giti panna. Seal failis on projekti ja mooduli struktuur. Kui avate sama salve mõnes teises arvutis, on teil automaatselt ka moodulite seaidstused paigas.

Saate ka hiljem lisada: parem klikk failil/kaustas -> ``Git`` -> ``Add``.

Failide lisamine giti (*git commit*)
---------------------------------------

Faili lisamiseks git'i (*git commit*) tehke parem klikk faili nimel -> ``Git`` -> ``Commit File ...``:

.. image:: /_images/intellij/git_11_commit.png

Saate lisada ka terve kausta. Parem klikk kausta nimel -> ``Git`` -> ``Commit Directory ...``:

.. image:: /_images/intellij/git_11b_commit_directory.png

Avaneb järgnev vaade. Mõistlik oleks lisada autori informatsioon. Kui te seda ei lisa, võib IntelliJ teilt seda järgmises sammus küsida. Sisestage mingi kommentaar. Seejärel valige alt ``Commit`` nupu kõrval oleva noole abil ``Commit and Push ...``:

.. image:: /_images/intellij/git_12_commit_window.png

Seejärel arvatavasti küsib IntelliJ teilt koodi vigade kohta. Erinevad probleemid (stiil jms) annavad vastava teate, kus mainitakse, et failides esineb probleeme. Te võite ``Review`` nupu abil need üle vaadata. Aga üldised piisab ``Commit`` nupust:

.. image:: /_images/intellij/git_13_code_analysis.png

Failide üleslaadimine (*git push*)
-----------------------------------

Failide üleslaadimiseks serverisse vajutage ``Push``:

.. image:: /_images/intellij/git_14_push.png
