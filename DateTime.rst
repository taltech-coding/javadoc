======================
Kuupäevad ja kellaajad
======================

Java 8 puhul tuleks kasutada kuupäevade ja kellaaegade säilitamiseks klasse paketist **java.time**, mille kohta oleks mõistlik lähemalt uurida `oracle Java juhendist <https://docs.oracle.com/javase/tutorial/datetime/iso/index.html>`_.

Lisaks java.time klassidele on olemas hulk klasse nagu *Calendar*, *Time* ja *Date*. Nii mõnigi meetod nendes klassides pole enam kasutusel, millele viitab märgistus *(deprecated)*. Neid kasutati java varasemates versioonides ning seetõttu leiab internetist väga palju näiteid nende kohta. Järgnevates näidetes neid ei kasutata ning ka enda töös oleks mõistlik neid vältida.

Kasulikud näited
================

Juhul kui meile on olulised ainult kuu ja aasta number, võime kasutata klassi **YearMonth**.

.. code-block:: java

    YearMonth rightNow = YearMonth.now();
    YearMonth nextDecember = YearMonth.of(2018, 12);

YearMonth objekt on muutmatu *(immutable)*, mis tähendab et kuu või aasta numbri muutmiseks tuleb sisuliselt luua uus objekt. Selle lihtsustamiseks on olemas mitmeid erinevaid meetodeid.

.. code-block:: java

    YearMonth y = YearMonth.of(2017, 4); // March 2017
    YearMonth y1 = y.plusYears(2);       // March 2019
    YearMonth y2 = y.minusMonths(1);     // February 2017
    YearMonth y3 = y.withMonth(9);       // September 2017

Selleks, et saada kuupäev soovitud formaati, saab kasutada meetodit **format**, millele antakse kaasa soovitud vormingu muster.

.. code-block:: java

    DateTimeFormatter dtf = DateTimeFormatter.ofPattern("MM.yyyy");
    String nextDecemberFormatted = nextDecember.format(dtf);
    System.out.println(nextDecemberFormatted);  // 12.2018

DateTimeFormatter dokumentatsioon: https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html

(Leht on täiendamisel)