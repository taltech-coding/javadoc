=======
Javadoc
=======

Javadoc on Java dokumentatsiooni generaator, mida sisaldab iga JDK.
Javadoci kasutades saab automaatselt genereerida oma koodi kommentaaridest Java dokumentatsiooni HTML failidena. Selleks on vaja eelnevalt oma kood ära kommenteerida.

Java koodi kommenteerimine
--------------------------

Dokumentatsiooni on vaja kirjutada iga muutuja ja meetodi kirjeldamiseks. Dokumentatsioon näeb üldiselt välja selline:

.. code-block:: java

    /**
    * This is documentation.
    */

Iga muutuja ette tuleks panna Javadoci kommentaar, mis kirjeldab seda muutujat.

.. code-block:: java

    /**
    * Person's age in years.
    */
    private int ageInYears;

Samuti tuleb iga meetodi ette panna Javadoci kommentaar. Meetodi kommentaaris on vaja ära kirjeldada kõik parameetrid ning ka väljastatav väärtus, kui see on olemas. Selleks on olemas **@param** ja **@return** tagid.

.. code-block:: java

    /**
    * Add two numbers together.
    * @param a First number.
    * @param b Second number.
    * @return The sum of a and b.
    */
    public int add(int a, int b) {
        return a + b;
    }

Erinevaid tage on veel mitmeid, mida saab kasutada olenevalt vajadusele. (Näiteks @exception, @see, @version)
`Oracle'i dokumentatsioonis`_ on nimekiri kõikidest tagidest ning mis järjekorras neid kasutada.

.. _`Oracle'i dokumentatsioonis`: http://www.oracle.com/technetwork/articles/java/index-137868.html

IDE-des on enamasti võimalik kommentaare genereerida automaatselt.

**IntelliJ**

Kui meetodile või muutujale eelneval real kirjutada /** ja vajutada enter genereerib IntelliJ automaatselt vajalike tagidega kommentaaribloki.
Samuti on võimalik genereerida automaatselt kommentaare kogu projekti või valitud failide jaoks:
Tools -> Generate JavaDoc

**Eclipse**

Eclipse genereerib samuti /** ja enteri puhul kommentaaribloki.
Mugavamaks kommenteerimiseks saab alla laadida plugina JAutodoc.

Javadoci dokumentatsiooni genereerimine
---------------------------------------

Dokumentatsiooni genereerimiseks tuleb kasutada käsurida.
Kõigepealt tuleb liikuda õigesse kausta.

.. image:: /_images/cd.png

Siis saab Javadoci genereerida käsuga *javadoc*.

.. image:: /_images/javadoc.png

Javadoc genereerib samasse kausta vajalikud HTML, JavaScript ja CSS failid. Dokumentatsiooni saab vaadata, avades lehe index.html

.. image:: /_images/boarding_pass.png
