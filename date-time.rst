======================
Kuupäevad ja kellaajad
======================

Java 8 puhul tuleks kasutada kuupäevade ja kellaaegade säilitamiseks paketti **java.time**, mille klasside kohta tasub lähemalt uurida `Oracle Java juhendist <https://docs.oracle.com/javase/tutorial/datetime/iso/index.html>`_.

Lisaks eelpoolnimetatule on olemas java.util klassid, näiteks *Calendar*, *Time* ja *Date*. Nii mõnigi meetod neis pole enam kasutusel, millele viitab ka märgistus *(deprecated)*. Java varasemates versioonides olid olemas ainult need klassid ning seetõttu leiab internetist väga palju näiteid nende kohta. Järgnevates näidetes kasutame kaasaegsemat java.time paketti ning ka enda töös oleks mõistlik eelistada seal paiknevaid klasse.

Kasulikud näited
================

Juhul kui meile on olulised ainult kuu ja aasta number, võime kasutata **YearMonth** objekte.

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
    
Kuupäeva objekti saamine tekstist ja selle vormindamine:

.. code-block:: java

    import java.time.LocalDate;
    import java.time.format.DateTimeFormatter;

    /**
     * LocalDate parsing and formatting example.
     */
    public class LocalDateExamples {
        public static void main(String[] args) {

            String inputDate = "2016/07/13";
            DateTimeFormatter dtfin = DateTimeFormatter.ofPattern("yyyy/MM/dd");
            LocalDate localDate = LocalDate.parse(inputDate, dtfin);
            System.out.println(localDate); // 2016-07-13
            localDate = localDate.plusDays(20); // add 20 days

            DateTimeFormatter dtfout = DateTimeFormatter.ofPattern("dd.MM.yyyy");
            System.out.println(localDate.format(dtfout)); // 08.08.2016
        }

    }


DateTimeFormatter dokumentatsioon: https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html

Huvitav video ajatsoonidest ja programmeerimisest: https://www.youtube.com/watch?v=-5wpm-gesOY

