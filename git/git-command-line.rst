Git kasutamine käsureal
=======================

Giti käivitamine käsureal. ``Start`` -> otsige "git", valige ``Git Bash``.

Kõigepealt tehke ära vajalik seadistus, et saaks gitlabiga ühendust:

``git config --global http.sslVerify "false"``

Salve kloonimiseks kohalikku arvutisse (``UNIID`` asendage edaspidi enda uniid-ga, näiteks ``eesnimi.perenimi`` või 6-kohaline kombinatsioon ees- ja perenime tähtedest):

``git clone https://UNIID@gitlab.cs.ttu.ee/UNIID/iti0202.git``

Nüüd võib IntelliJ-ga avada loodud ``iti0202`` kausta ja sinna sisse luua uue mooduli. Vt: https://ained.ttu.ee/javadoc/intellij_git.html#samm-9-uue-mooduli-loomine-ulesande-jaoks

Seejärel liikuge loodud kausta (kausta nimi on sama mis ainekood):

``cd iti0202``

Nüüd kopeerige oma projekt giti kausta:

``cp -R /c/Users/UNIID/IdeaProjects/KT .``

(käsu lõpus on punkt, - märk R ees peab tavaline miinus olema, kopeerides võib sinna mingi sarnane muu sümbol tekkida)

Enne, kui faile saab Giti üles panna, on vaja teha kaks sammu. Esiteks tuleb muudetud failid lisada järgmisesse commiti:

``git add KT``

seejärel saab teha commiti (commititakse vaid need failid, mis on eelnevalt lisatud):

``git commit -m "lahendus v1"``

Eelneva käsuga lisatakse commitides kohe ka kommentaar.

Kui commit on tehtud, on failid pandud lokaalsesse salve (kohalikus arvutis). Selleks, et failid jõuaks serverisse ja meie neid hinnata saaks, tuleb nad üles laadida:

``git push origin master``
 
 
IntelliJ jaoks Java asukoht arvutiklassis: ``C:\Program Files\Java\jdk1.8.0_144``.
