Tõeväärtus-andmetüübid
=======================

Tõeväärtus (*boolean*) on primitiivne andmetüüp, millel saab olla vaid kaks väärtust: tõene (*true*) ja väär (*false*).

Väärtustamine
--------------

Väärtustada võib lihtsalt andes muutujale väärtuse:

.. code-block:: java

  boolean isHappy = true;

Keerukam väärtustamine:
  
.. code-block:: java
  
  boolean isWetAndCold = temperature > 0 && temperature < 10; // returns true if temperature is between 0 and 10 

Ahvatlev on kirjutada näiteks "boolean a = 10 < x < 20", et näha, kas x on 10 ja 20 vahel. See aga ei tööta, sest iga < operaator peab saama enda kaks väärtust. Õige on kirjutada "boolean a = 10 < x && x < 20"

Põhioperatsioonid
------------------

&& - AND (tõene ainult, kui mõlemad pooled on tõesed)

|| - OR (tõene, kui vähemalt üks pooltest on tõene)

! - NOT (inversioon)

+---+---+--------+--------+----+
| P | Q | P && Q | P || Q | !P |
+===+===+========+========+====+
| T | T |    T   |    T   |  F |
+---+---+--------+--------+----+
| T | F |    F   |    T   |  F |
+---+---+--------+--------+----+
| F | T |    F   |    T   |  T |
+---+---+--------+--------+----+
| F | F |    F   |    F   |  T |
+---+---+--------+--------+----+

Stiil 
-----

Kehv stiil on võrrelda tingimust *false* või *true*'ga:

+----------------------------------------------------+-----------------------------------------------------+
|          Kehv stiil                                |                 Parem stiil                         |
+====================================================+=====================================================+
| .. code-block:: java                               | .. code-block:: java                                |
|                                                    |                                                     |
|   if (isHappy == true) {                           |   if (isHappy) {                                    |
|       System.out.println("This is poor style.");   |       System.out.println("This is better style.");  |
|   }                                                |   }                                                 |
+----------------------------------------------------+-----------------------------------------------------+
| .. code-block:: java                               | .. code-block:: java                                |
|                                                    |                                                     |
|   if (isHappy == false) {                          |   if (!isHappy) {                                   |
|       System.out.println("This is poor style.");   |       System.out.println("This is better style.");  |
|   }                                                |   }                                                 |
+----------------------------------------------------+-----------------------------------------------------+

Tingimuslaused
---------------
*if/while/for* jne konstruktsioonid kasutavad boolean väärtust, et otsustada, kas käivitada mingit koodiosa. Seal kasutatav kontroll võib olla kas lihtne boolean muutuja väärtuse kontroll või mingi keerukam avaldis (aga selle tulemus peab ikka olema kas true või false).

.. code-block:: java

 if (score < 0 || score > 100) {
     System.out.println("Score has an illegal value.");
 } 
  
Meetodid
---------

*Boolean* on primitiivse andmetüübi *boolean* wrapper. *Boolean* (suure algustähega) on objekt, väikese algustähega *boolean* on aga primitiivne andmetüüp. Esimesega kaasneb rohkem meetodeid, teine aga hoiab mälu kokku. 

Booleani väärtus võib olla true, false või null, booleani väärtus ainult kas true või false.

Näiteks:

.. code-block:: java

  boolean result = Boolean.TRUE;
  Boolean result = true;
  
Sisuliselt kompilaator teeb:

.. code-block:: java

  Boolean result = Boolean.valueOf(true);

  
**compare(boolean x, boolean y)**
  
Võrdleb kahte tõeväärtust (*boolean*) teineteisega. Tagastusväärtus on täisarv (*integer*). Tagastatakse:

- 0 kui x == y
- -1 kui !x && y
- 1 kui x && !y
  
**logicalAnd(boolean a, boolean b)**

Tagastusväärtus on *boolean*. Tagastab *true* ainult siis, kui mõlemad argumendid on tõesed.
  
**logicalOr(boolean a, boolean b)**

Tagastusväärtus on *boolean*. Tagastab *true* siis, kui vähemalt üks argumentidest on tõene.
  
**logicalXor(boolean a, boolean b)**

Tagastusväärtus on *boolean*. Tagastab *false* ainult siis, kui mõlemad argumendid on kas tõesed või väärad. Muul juhul tagastab *true*.

**valueOf(boolean b)**

Tagastab Boolean instantsi, mis väljendab booleani väärtust. Kui boolean on *true*, siis tagastatakse sõne "true", muul juhul "false".

.. code-block:: java

  Boolean b = true;
  String str = String.valueOf(b);
  
  System.out.println(str); // prints "true" 

**toString(boolean b)**

Muudab tõeväärtuse sõneks. Tuleks kasutada siis, kui ollakse kindel, et booleani väärtus ei ole *null*. Vastasel juhul viskab *NullPointerException*'i. Tagastab sõne objekti, mis väljendab booleani väärtust.

.. code-block:: java

  Boolean b = true;
  String str = Boolean.toString(b);
  
  System.out.println(str); // prints "true" 
  
-------
  
Dokumentatsioon: https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html
