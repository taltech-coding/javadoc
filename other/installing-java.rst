Java installeerimine
====================

| Enne kui saab luua ja muuta Java programme, tuleb endale installeerida JDK (Java Software Development Kit). Selleks vaata: :doc:`java-versions` alapealkirja "Ajakohase Java (JDK) allalaadimise lingid".  
| *Linux Ubuntu operatsioonisüsteemiga saab OpenJDK installeerida käsitsi allalaadides või läbi Ubuntu Apt paketihalduri. Paketihalduri kaudu installeerides pole JDK-d eraldi vaja alla laadida.*

Windows
-------
Ava installeerimise aken ning luba sellel oma arvutis muudatusi teha.
Vajuta "Next" ja nõustu installeerimise seadetega. Kui installeerimine on lõpetatud, võid akna sulgeda.
Ava *Control Panel* -> *System and Security* -> *System* -> *Advanced system settings*. 
Ava sealt *Advanced* menüü, ning vajuta nuppu *Environment Variables*.
Tee topeltklõps *System Variables* all oleval *Path* real ja vajuta *New*. 
Lisa sinna C:\\Program Files\\Java\\jdkxxx\\bin asendades jdkxxx installeeritud Java versiooniga. Vajuta *Move up*, kuni sinu lisatud asukoht on listi eesotsas. (Windows 7 puhul saab lisada *Pathi* mitu variable'i, kui need eraldada semikooloniga.)

Sulge aken ja ava command prompt. 
Kirjuta sinna *path* ja vajuta Enter. Peaksid nägema installeeritud JDK asukohta, mille just lisasid.
Kirjuta seejärel *java -version* ja vajuta enter. Peaksid nägema installeeritud Java versiooni.

Linux (Ubuntu), Apt paketihalduri abil
--------------------------------------
Ubuntu 18.04-s on juba OpenJDK pakk installitud.
Seda saab kontrollida käsuga terminalis:

::

    javac -version

Kui JDK pole installitud kuvatakse midagi sarnast:

::

    Command 'javac' not found

Sellisel juhul on vaja JDK installida läbi käsurea. OpenJDK 11 puhul:

::

    sudo apt install openjdk-11-jdk

pärast installeerimist peaks javac käsk andma installitud versiooni info:

::

    javac 11.0.1

Mac OS X
--------
Tee topeltklõps alla laetud failil, et avada installeerimise aken.
Vajuta *Continue* ja seejärel *Install*.
Sisesta administraatori kasutajanimi ja parool.
Vajuta *Install Software*. Kui installeerimine on lõpetatud, võid akna sulgeda.
Peale installeerimist ava *Terminal*.
Kirjuta sinna *javac -version* ja vajuta Enter.
Kui installeerimine oli edukas, peaksid nüüd nägema installeeritud JDK versiooni, näiteks "javac 1.8.0_112".


Mis on JRE ja JDK vahe?
------------------------
JRE: Java Runtime Environment. See on Java virtuaalmasin, mille peal jooksevad Java aplikatsioonid. See sisaldab ka brauseri pluginaid aplettide jooksutamiseks.

JDK: Java Software Development Kit. Sisaldab endas JRE-d, kompilaatorit ja vahendeid näiteks silumiseks, et luua ja kompileerida Java programme.

Kui on vaja Java programme ainult jooksutada, peaks piisama JRE-st. Kui aga soovitakse tegeleda arenduse ja programmide kompileerimisega, tuleks installeerida JDK. 
