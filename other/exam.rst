Eksamiga seonduv informatsioon
==============================

Tehke allpool oleva testüleanne läbi!

Viited ja info
--------------

Javadoc: https://ained.ttu.ee/javadoc/

JDK 11 dokumentatsioon: https://ained.ttu.ee/javadoc/jdk/api/

OOP vihjeid: https://ained.ttu.ee/javadoc/MostFrequentErrors.html

IntelliJ käivitamisel võita valida "Licence server" ja vajutada "discover server". Ta peaks automaatselt laadima aadressi jms.

Java 11 asukoht arvutiklassis: ``C:\OpenJDK11``. (Java 8 asukoht arvutiklassis: ``C:\Program Files\Java\jdk1.8.0_202``).

Git kasutamine käsureal
-----------------------

Giti käivitamine käsureal. ``Start`` -> otsige "git", valige ``Git Bash``.

Kõigepealt tehke ära vajalik seadistus, et saaks gitlabiga ühendust:

``git config --global http.sslVerify "false"``

Salve kloonimiseks kohalikku arvutisse (``UNIID`` asendage edaspidi enda uniid-ga, näiteks 6-kohaline kombinatsioon ees- ja perenime tähtedest):

``git clone https://gitlab.cs.ttu.ee/iti0202-2019/eksamid/exam1-UNIID.git``

**NB!** Kui UNIID sisaldab punkti, siis tuleb see asendada ``-`` märgiga. Näiteks ``ago.luberg`` asemel tuleb kasutada ``ago-luberg``. Kasutage väikeseid tähti.

Nüüd võib IntelliJ-ga avada loodud kausta ja sinna sisse luua uue mooduli. Vt: https://ained.ttu.ee/javadoc/intellij_git.html#samm-9-uue-mooduli-loomine-ulesande-jaoks

Testülesanne
-------------

Selleks, et kontrollida, kas IntelliJ ja Git toimivad, lahenda testülesanne: kirjuta programm, mis trükib ekraanile ``Hello world!``.

Kaust Gitis: ``TEST``

Klass: ``ee.taltech.iti0202.exam.hello.HelloWorld``.

Lahendus peab olema ``main`` meetodis (ehk kui programm käima panna, trükitakse tekst ja programm lõpetab).

ained.ttu.ee lehel peaksid nägema tulemuse TEST ülesande juures. Paremal ääres peak olema sektsioon "Submissions". Selle all näete oma tulemusi.
Klikkides ühe submissioni ääres oleva silma peal, avaneb dialoog, kus näete täpsemat tulemust (kaasa arvatud testi tulemust).

Selle ülesande eest peaks saama ühe testi läbitud ja teine kukub läbi (see peabki läbi kukkuma). Te peaks nägema sellist tulemust:

::

    Compilation succeeded.


     ---
    HelloTest (TestNG)
    datetime
     ---

    Passed unit tests: 1/2
    Failed unit tests: 1
    Skipped unit tests: 0
    Grade: 50.0%

    Overall grade: 50.0%


Koodi üleslaadimiseks
---------------------

Liikuge git bash'is loodud kausta (kausta nimes on teie uniid):

``cd exam1-UNIID``

Enne, kui faile saab Giti üles panna, on vaja teha kaks sammu. Esiteks tuleb muudetud failid lisada järgmisesse commiti:

``git add EXAM1``

seejärel saab teha commiti (commititakse vaid need failid, mis on eelnevalt lisatud): 

``git commit -m "lahendus v1"``

Eelneva käsuga lisatakse commitides kohe ka kommentaar.

Kui commit on tehtud, on failid pandud lokaalsesse salve (kohalikus arvutis). Selleks, et failid jõuaks serverisse ja meie neid hinnata saaks, tuleb nad üles laadida:

``git push origin master``
