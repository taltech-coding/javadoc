===================
Intellij kasutamine
===================

Intellij on JetBrains-i poolt loodud Java IDE.

Kasutamine
----------

**Uue projekti loomine:**

- Intellij avades valida "Create New Project".
- Vasakul asuvast listis valida soovitud projektitüüp. (tavaliselt - kui ei öelda teisiti, siis "Java")
- Projekti SDK - otsida üles Java JDK kaust (Windowsil nt Program Files -> Java -> jdk1.8.0_77, OS X puhul tavaliselt /Library/Java/JavaVirtualMachines/jdk1.8.0_112.jdk/Contents/Home), valida see ning vajutada "OK".
- "Additional Libraries and Frameworks" alt pole vaja midagi valida. Vajutada "Next".
- "Create project from template" kasti panna linnuke ainult siis, kui on soov, et Intellij ise koostaks klassi Main meetodiga. Vajutada "Next".
- Järgmiseks valida projektile soovitud asukoht. Seejärel panna projektile nimi (kausta nimi). Vajutada "Finish".

**Projekti pakettide ning klasside loomine:**

- Vasakul pool on lahter, kus sees tehtud projekt ning lisaks "External Libraries". Laiendada tehtud projekti.
- Avaneb paar asja, kuid oluline on kaust nimega "src". Seal peaksid paiknema tehtavad paketid ning klassid. Parem klikk ning New -> Java Class või New -> Package.
- Paketti saab klasse teha samamoodi: parem klikk ning New -> Java Class.

**Koodi jooksutamine:**

Üleval paremal nurgas asub roheline play-nupp. Seda vajutades üritab Intellij koodi kompileerida ning selle õnnestudes paneb koodi tööle. 
Samuti saab selle nupu kõrvalt valida, millist klassi tööle panna. Kui soovitud faili nimekirjas pole, siis saab selle avada, 
ning ülevalt avatud failide ribalt teha vastava faili peal parem klikk ning valida "Run".
https://www.jetbrains.com/help/idea/2016.3/running-applications.html <- saab täpsemalt lugeda

Kasulikke linke
---------------

https://www.jetbrains.com/student/ <- info IntelliJ Ultimate litsentsi kohta

https://www.jetbrains.com/help/idea/2016.3/keyboard-shortcuts-you-cannot-miss.html <- mõningaid kasulikke keyboard shortcut'e

https://www.jetbrains.com/help/idea/2016.3/guided-tour-around-the-user-interface.html <- saab kasutajaliidese kohta lähemalt lugeda
