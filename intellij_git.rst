Git'i kasutamine IntelliJ'ga
=============================

Kui soovite git'i kasutada läbi IntelliJ, käituge järgmiselt

Samm 1: *Checkout from git*
----------------------------

.. image:: /images/intellij/git_1_checkout.png

Samm 2: Salve aadress
----------------------

.. image:: /images/intellij/git_2_clone.png

Samm 3: Testime salve aadressi
-------------------------------

Veenduge, et salv on kättesaadav (peaks nägema umbes sellist teadet):

.. image:: /images/intellij/git_3_test.png

Samm 4: Uus projekt
-------------------

.. image:: /images/intellij/git_4_new_project.png

Samm 5: Projekti importimine, 1. samm
----------------------------------------

.. image:: /images/intellij/git_5_import.png

Samm 6: Projekti nimi
------------------------------

.. image:: /images/intellij/git_6_project_location.png

Samm 7: Lähtefailide asukoht
------------------------------

.. image:: /images/intellij/git_7_import_projects.png

Samm 8: Info raamistike kohta
------------------------------
.. image:: /images/intellij/git_8_no_frameworks.png

Samm 9: Uue mooduli loomine ülesande jaoks
----------------------------------------------

Kui salv on kloonitud, loome ülesande jaoks uue mooduli.
Sarnaselt tuleks käituda iga ülesande puhul.

Parem klikk projekti nimel, sealt valida New -> Module.

.. image:: /images/intellij/git_9_new_module.png

Samm 10: Uue mooduli aken
---------------------------

Kui teil on seadistamata JDK (Java Development Kit), tasub see siin kohe ära teha.
Võite selle läbi teha ka hiljem.

.. image:: /images/intellij/module_1_new.png

JDK seadistamine seadete kaudu
---------------------------------

Kui te pole veel JDK asukohta määranud, saate seda teha projekti struktuuri juurest.
File -> Project Structure. Avaneb selline vaade:

.. image:: /images/intellij/jdk_1_settings.png

Kui Project SDK on määramata, lisage uus JDK.

Samm 11: JDK seadistamine
--------------------------

Otsige oma arvutist üles installeeritud Java Development Kit (jdk kaust).

.. image:: /images/intellij/jdk_2_path.png

Kui teil "Project language level" ei ole juba "8 - Lambdas, ...", siis määrake see:

.. image:: /images/intellij/jdk_3_language_level.png

Mooduli nimi
-------------

Jätkame mooduli seadistamisega. Kui olete jõudnud teise sammu, määrake mooduli nimi. Kasutage ülesande koodi. Sisuliselt teeb see selle nimega kausta teie salve.

.. image:: /images/intellij/module_2_name.png

Uus klass
-----------

Looge uus vajalik klass:

.. image:: /images/intellij/module_3_new_class.png

Faili lisamine (*git add*)
--------------------------------

Peale mooduli/klassi jms loomist võib IntelliJ ise küsida, kas loodav fail panna git'i. Võite kohe "yes" valida.

.. image:: /images/intellij/module_4_add_file_to_git.png

Mõistlik oleks ka .iml failid git'i panna. Seal failis on projekti ja mooduli struktuur. Kui avate sama salve mõnes teises arvutis, on teil automaatselt ka moodulite seaidstused paigas.

.. image:: /images/intellij/git_10_add_file_to_git.png

Saate ka hiljem lisada: parem klikk failil/kaustas -> Git -> Add.

Failide lisamine giti (*git commit*)
---------------------------------------

Faili lisamiseks git'i (*git commit*) tehke parem klikk failil -> Git -> Commit File ...:

.. image:: /images/intellij/git_11_commit.png

Saate lisada ka terve kausta. Parem klikk kaustas -> Git -> Commit Directory ...:

.. image:: /images/intellij/git_11b_commit_directory.png

Avaneb järgnev vaade. Mõistlik oleks lisada autori informatsioon. Kui te seda ei lisa, võib IntelliJ teilt seda järgmises sammus küsida. Sisestage mingi kommentaar. Seejärel valige alt "commit" nupu kõrval oleva noole abil "Commit and Push ...":

.. image:: /images/intellij/git_12_commit_window.png

Seejärel arvatavasti küsib IntelliJ teilt koodi vigade kohta. Erinevad probleemid (stiil jms) annavad vastava teate, kus mainitakse, et failides esineb probleeme. Te võite Review nupu abil need üle vaadata. Aga üldised piisab "Commit" nupust:

.. image:: /images/intellij/git_13_code_analysis.png

Failide üleslaadimine (*git push*)
-----------------------------------

Failide üleslaadimiseks serverisse vajutage "Push":

.. image:: /images/intellij/git_14_push.png