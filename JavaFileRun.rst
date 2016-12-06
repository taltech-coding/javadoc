====================================================
Java-faili käivitamine (kompileerimine, käivitamine)
====================================================

Java programm kirjutatakse inimloetavas Java keeles ning salvestatakse java-failina.

Java-faili saab käivitada käsurealt (command line). Selleks tuleb fail kõigepealt kompileerida ning siis käivitada. IDE'd (nagu näiteks IntelliJ) teevad kogu selle töö ise ära, kui vajutada Run nuppu.

**Käsureal:** tuleb liikuda õigesse foldrisse ning siis saab Java-faili kompileerida käsuga
*javac failinimi.java*

Java-faili käivitades kompileeritakse see class-faili, mis koosneb baitkoodist ja on seetõttu platvormist sõltumatu.

Siis tuleb programm käivitada.

**Käsureal:** saab Java-faili käivitada käsuga 
*java failinimi*

Programm käivitatakse JVM (Java Virtual Machine) sees ning kuna fail koosneb baitkoodist saab igal platvormil (Windows, Linux, Mac) sama faili käivitades sama tulemuse.
