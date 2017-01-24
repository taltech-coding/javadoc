Java installeerimine
====================

Enne kui saab luua ja muuta Java programme, tuleb endale installeerida JDK (Java Software Development Kit). Selle saab alla laadida leheküljelt: http://www.oracle.com/technetwork/java/javase/downloads/index.html.
Sealt lehelt tuleks valida *Download*, mis asub *JDK* all. Järgmisena tuleks valida sobiv versioon oma arvutile (tuleks võtta viimane stabiilne versioon, sageli on saadaval rohkem kui üks versioon).

Windows
--------
Ava installeerimise aken ning luba sellel oma arvutis muudatusi teha.
Vajuta "Next" ja nõustu installeerimise seadetega. Kui installeerimine on lõpetatud, võid akna sulgeda.
Ava *Control Panel* -> *System and Security* -> *System* -> *Advanced system settings*. 
Ava sealt *Advanced* menüü, ning vajuta nuppu *Environment Variables*.
Tee topeltklõps *System Variables* all oleval *Path* real ja vajuta *New*. 
Lisa sinna C:\\Program Files\\Java\\jdk1.8.0_xx\\bin asendades *8.0_xx* installeeritud Java versiooni numbriga. Vajuta *Move up*, kuni sinu lisatud asukoht on listi eesotsas. (Windows 7 puhul saab lisada *Pathi* mitu variable'i, kui need eraldada semikooloniga.)

Sulge aken ja ava command prompt. 
Kirjuta sinna *path* ja vajuta Enter. Peaksid nägema installeeritud JDK asukohta, mille just lisasid.
Kirjuta seejärel *java -version* ja vajuta enter. Peaksid nägema installeeritud Java versiooni.

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
