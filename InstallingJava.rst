Java installeerimine
========

Enne kui saab luua ja muuta Java programme, tuleb endale installeerida JDK (Java Software Development Kit). Selle saab alla laadida leheküljelt: http://www.oracle.com/technetwork/java/javase/downloads/index.html 
Sealt lehelt tuleks valida "Download", mis asub "JDK" all. Järgmisena tuleks valida sobiv versioon oma arvutile (tuleks võtta viimane stabiilne versioon, sageli on rohkem kui üks versioon saadaval ja tuleks hoolikalt numbrit jälgida).
TODO

Windows
--------
Ava installeerimise aken ning luba sellel oma arvutis muudatusi teha.
Vajuta "Next" ja nõustu installeerimise seadetega. Kui installeerimine on lõpetatud, võid akna sulgeda.
Nüüd kui JDK on installeeritud, pead ütlema Windowsile, kuidas seda laadida.
Ava Control Panel -> System and Security -> System -> Advanced system settings. 
Ava sealt "Advanced" menüü, ning vajuta "Environment Variables".
Tee topeltklõps ... TODO


Mac OS X
--------
Tee topeltklõps alla laetud failil, et avada installeerimise aken.
Vajuta "Continue" ja seejärel "Install".
Sisesta administraatori kasutajanimi ja parool.
Vajuta "Install Software". Kui installeerimine on lõpetatud, võid akna sulgeda.
Peale installeerimist ava Terminal.
Kirjuta sinna javac -version ja vajuta Return.
Kui installeerimine oli edukas, peaksid nüüd nägema installeeritud JDK versiooni, näiteks "javac 1.8.0_112".


Mis on JRE ja JDK vahe?
--------
JRE: Java Runtime Environment. See on põhimõtteliselt Java Virtuaalmasin, kus peal jooksevad Java aplikatsioonid. See sisaldab ka brauseri pluginaid aplettide jooksutamiseks.
JDK: Java Software Development Kit. Sisaldab endas JRE-d, kompilaatorit ja vahendeid näiteks silumiseks, et luua ja kompileerida Java programme.

Kui on vaja Java programme ainult jooksutada, peaks piisama JRE-st. Kui aga soovitakse tegeleda arenduse ja programmide kompileerimisega, tuleks installeerida JDK. 

TODO
