Tõeväärtus-andmetüübid
=======================

Tõeväärtus (*boolean*) on primitiivne andmetüüp, millel saab olla vaid kaks väärtust: tõene (*true*) ja väär (*false*).

Väärtustamine
--------------

.. code-block:: java

  boolean a = True;
  
Meetodid
---------
  
**compare(boolean x, boolean y)**
  
Võrdleb kahte tõeväärtust (boolean) teineteisega. Tagastusväärtus on täisarv (*integer*). Tagastatakse:

  - 0 kui x == y
  - -1 kui !x && y
  - 1 kui x && !y
  
**logicalAnd(boolean a, boolean b)**

Tagastusväärtus on boolean. Tagastab *true* ainult siis, kui mõlemad argumendid on tõesed.
  
**logicalOr(boolean a, boolean b)**

Tagastusväärtus on boolean. Tagastab *true* siis, kui vähemalt üks argumentidest on tõene.
  
**logicalXor(boolean a, boolean b)**

Tagastusväärtus on boolean. Tagastab *false* ainult siis, kui mõlemad argumendid on kas tõesed või väärad. Muul juhul tagastab *true*.

**valueOf(boolean b)**

Tagastab sõne, mis väljendab booleani väärtust. Kui boolean on *true*, siis tagastatakse sõne "true", muul juhul "false".


.. code-block:: java

  Boolean b = true;
  String str = String.valueOf(b);
  
  System.out.println(str); // prindib konsooli "true"

**toString(boolean b)**

Muudab tõeväärtuse sõneks. Tuleks kasutada siis, kui ollakse kindel, et booleani väärtus ei ole *null*. Vastasel juhul viskab *NullPointerException*'i.

.. code-block:: java

  Boolean b = true;
  String str = Boolean.toString(b);
  
  System.out.println(str); // prindib konsooli "true"
  
-------
  
Dokumentatsioon: https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html
