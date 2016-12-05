Sõne
====
Sõned (ingl.k. *string*) on objektid, mis kuuluvad klassi *java.lang.String*. Sõne on sümbolite kogum. Sõnest võib mõelda kui tähtede (või üldisemalt sümbolite) massiivist. Sõne on Java keeles objekt, mis tähendab, et tema kohta kehtivad natuke teised reeglid kui primitiivsete andmetüüpide puhul.

Sõne-tüüpi muutuja loomine:

.. code-block:: java

    String greeting;
    
Sellisel juhul pole sõnel väärtust määratud. Vaikeväärtus on **null**. 
**null** tähendab objektide puhul seda, et antud objekt on väärtustamata. Kui me allpool vaatleme String'i meetodeid, siis kui meie vaadeldava objekti väärtus on null, siis ükski allpool toodud meetod ei tööta - käivitamisel antakse veateade.
		
Muutuja loomisel võib sellele ka sisu anda:

.. code-block:: java

  String greeting = "Hello world!";
  
Sellisel juhul loob kompilaator sõne-tüüpi objekti, mille väärtus on "Hello world!".

Lisaks tekstilisele väärtusele võib väärtuseks olla ka null:

.. code-block:: java

  String greeting = null;
  
Meetodid
--------

**length()**

Tagastab sõne pikkuse (mitu sümbolit on sõnes).

.. code-block:: java

  System.out.println("hello".length()); // prindib "5"
  System.out.println("".length()); // prindib "0"
  
**charAt**

Võimaldab sõnest leida ühe sümboli vastavalt ette antud indeksile. See töötab sarnaselt massiividega. Indeks hakkab 0-st, st esimese elemendi index on 0. Meetod tagastab andmetüübina char ehk ühe sümboli.

.. code-block:: java

  char c = "hello".charAt(0); // c = 'h'
  c = "hello".charAt(1); // c = 'e'
  
**substring**

Võimaldab sõnest alamosa võtta. Samanimelist meetodit on kaks: üks on ühe argumendiga, teine on kahe argumendiga.
Ühe argumendiga meetod tagastab alamsõne, mille algus on ette antud indeksiga positsioonist ning mille lõpp on algse sõne lõpp.

.. code-block:: java

  System.out.println("tere".substring(1)); // prindib "ere"
  System.out.println("tere".substring(3)); // prindib "e"
  
Kahe argumendiga meetod tagastab alamsõne, mille algus on esimese argumendiga määratud indeksiga positsioonist ning mille lõpp on teise argumendiga määratud indeksiga positsioonist eelmine positsioon. Ehk siis alguse positsioon on kaasa arvatud, lõpu oma ei ole kaasa arvatud.

.. code-block:: java
  System.out.println("tere".substring(1,3)); // prindib "er"
  System.out.println("tere".substring(3,4)); // prindib "e"
  
**indexOf**

Otsib sõnest etteantud (alam)sõne ja tagastab positsiooni, kust otsitav (alam)sõne leiti. Kui otsitavat (alam)sõne ei leita, tagastab -1.

.. code-block:: java

  System.out.println("hello".indexOf("h")); // prindib "0"
  System.out.println("hello".indexOf("he")); // prindib "0"
  System.out.println("hello".indexOf("llo")); // prindib "2"
  System.out.println("hello".indexOf("a")); // prindib "-1"
  
Kasutada on võimalik ka kahe argumendiga meetodit. Teine argument näitab ära, alates mis positsioonist otsima hakata.

.. code-block:: java

  System.out.println("hello".indexOf("h", 0)); // prindib "0"
  System.out.println("hello".indexOf("h", 1)); // prindib "-1", kuna "t" ei leidu, kui hakata otsima alates positsioonist 1 (ehk siis teisest tähest)
  System.out.println("hello".indexOf("e", 1)); // prindib "1"
  System.out.println("hello".indexOf("l", 2)); // prindib "3", kui hakata positsioonist 2 otsima, leidub esimene "l" positsioonil 3

Sõnede võrdlemine
-----------------
TODO

   
    
    
    
    

-------

Dokumentatsioon: https://docs.oracle.com/javase/tutorial/java/data/strings.html

Dokumentatsioon: https://docs.oracle.com/javase/8/docs/api/java/lang/String.html






