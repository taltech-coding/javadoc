Git kasutamine käsureal
=======================

Giti käivitamine käsureal. ``Start`` -> otsige "git", valige ``Git Bash``.

Kõigepealt tehke ära vajalik seadistus, et saaks gitlabiga ühendust:

``git config --global http.sslVerify "false"``

Salve kloonimiseks kohalikku arvutisse (``UNIID`` asendage edaspidi enda uniid-ga, näiteks ``eesnimi.perenimi`` või 6-kohaline kombinatsioon ees- ja perenime tähtedest):

``git clone https://UNIID@gitlab.cs.ttu.ee/UNIID/iti0202.git``

Seejärel liikuge loodud kausta (kausta nimi on sama mis ainekood):

``cd iti0202``

Nüüd kopeerige oma projekt giti kausta:

``cp -R /c/Users/UNIID/IdeaProjects/KT .``

(käsu lõpus on punkt, - märk R ees peab tavaline miinus olema, kopeerides võib sinna mingi sarnane muu sümbol tekkida)

Enne, kui faile saab Giti üles panna, on vaja teha kaks sammu. Esiteks tuleb muudetud failid lisada järgmisesse commiti:

``git add KT``

seejärel saab teha ``commit``i (commititakse vaid need failid, mis on eelnevalt lisatud):´

``git commit -m "lahendus v1"``

Eelneva käsuga lisatakse commitides kohe ka kommentaar.

Kui commit on tehtud, on failid pandud lokaalsesse salve (kohalikus arvutis). Selleks, et failid jõuaks serverisse ja meie neid hinnata saaks, tuleb nad üles laadida:

``git push origin master``
 


