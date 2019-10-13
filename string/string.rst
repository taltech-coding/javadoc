Sõne
====
Sõned (ingl.k. *string*) on objektid, mis kuuluvad klassi *java.lang.String*. Sõne on sümbolite kogum. Sõnest võib mõelda kui tähtede (või üldisemalt sümbolite) massiivist. 
Sõne on Java keeles objekt, mis tähendab, et tema kohta kehtivad natuke teised reeglid kui primitiivsete andmetüüpide puhul.
		
Sõne-tüüpi muutuja loomine:

.. code-block:: java

  String greeting = "Hello world!";
  
Sellisel juhul loob kompilaator sõne-tüüpi objekti, mille väärtus on "Hello world!".

Lisaks tekstilisele väärtusele võib väärtuseks olla ka null:

.. code-block:: java

  String greeting = null;
  
null tähendab objektide puhul seda, et antud objekt on väärtustamata. Kui meie vaadeldava objekti väärtus on null, siis ei ole võimalik tema meetodeid välja kutsuda.  
  
Võimalik on luua ka initsialiseerimata muutuja:

.. code-block:: java

    String greeting;
    
Sellisel juhul pole sõnel väärtust määratud ja ta on initsialiseerimata. Vaikeväärtus on **null**. 
Kui seda teha lokaalselt (meetodi sees), siis sama muutuja kasutamisel enne sellele väärtuse määramist annab kompilaator vea, näiteks:  

.. code-block:: console

	Error:(4, 23) java: variable greeting might not have been initialized

Meetodid
--------

**length()**

Tagastab sõne pikkuse (mitu sümbolit on sõnes). Tagastatav väärtus on täisarv.

.. code-block:: java

  System.out.println("hello".length()); // prints "5"
  System.out.println("".length()); // prints "0"
  
**charAt**

Võimaldab sõnest leida ühe sümboli vastavalt ette antud indeksile. See töötab sarnaselt massiividega. Indeks hakkab 0-st, st esimese elemendi indeks on 0. Meetod tagastab andmetüübina char ehk ühe sümboli.

.. code-block:: java

  char c = "hello".charAt(0); // c = 'h'
  c = "hello".charAt(1); // c = 'e'
  
**substring**

Võimaldab sõnest alamosa võtta. Samanimelist meetodit on kaks: üks on ühe argumendiga, teine on kahe argumendiga.
Ühe argumendiga meetod tagastab alamsõne, mille algus on ette antud indeksiga positsioonist ning mille lõpp on algse sõne lõpp.

.. code-block:: java

  System.out.println("hello".substring(1)); // prints "ello"
  System.out.println("hello".substring(3)); // prints "lo"
  
Kahe argumendiga meetod tagastab alamsõne, mille algus on esimese argumendiga määratud indeksiga positsioonist ning mille lõpp on teise argumendiga määratud indeksiga positsioonist eelmine positsioon. Ehk siis alguse positsioon on kaasa arvatud, lõpu oma ei ole kaasa arvatud.

.. code-block:: java

  System.out.println("hello".substring(1,3)); // prints "el"
  System.out.println("hello".substring(3,4)); // prints "l"
  
**indexOf**

Otsib sõnest etteantud (alam)sõne ja tagastab positsiooni, kust otsitav (alam)sõne leiti. Kui otsitavat (alam)sõne ei leita, tagastab -1.

.. code-block:: java

  System.out.println("hello".indexOf("h")); // prints "0"
  System.out.println("hello".indexOf("he")); // prints "0"
  System.out.println("hello".indexOf("llo")); // prints "2"
  System.out.println("hello".indexOf("a")); // prints "-1"
  
Kasutada on võimalik ka kahe argumendiga meetodit. Teine argument näitab ära mis positsioonist alates otsima hakata.

.. code-block:: java

  System.out.println("hello".indexOf("h", 0)); // prints "0"
  System.out.println("hello".indexOf("h", 1)); // prints "-1", because there is no "h" found when you start looking from position 1 (from second letter)
  System.out.println("hello".indexOf("e", 1)); // prints "1"
  System.out.println("hello".indexOf("l", 2)); // prints "2"

**replace**

Sellel meetodil on kaks argumenti, millest esimene on vana sümbol ja teine uus sümbol. Tagastab **uue** sõne, kus on kõik vana sümboli instantsid asendatud uue sümboliga.

.. code-block:: java

  System.out.println("abc".replace('a', 'b')); // prints "bba"
  
**trim()**

Tagastab **uue** sõne, millelt on eemaldatud eelnevad ja järgnevad tühikud.

**toUpperCase()**

Tagastab **uue** sõne, kus kõik tähemärgid on muudetud suurtähtedeks.

**toLowerCase()**

Tagastab **uue** sõne, kus kõik tähemärgid on muudetud väiketähtedeks.

Sõnede võrdlemine
-----------------
Sõnede puhul ei saa kasutada == võrdlust. See võrdleb objektide puhul seda, kas nad on täpselt sama instants. Meid huvitab aga, kas sisu (ehk väärtus) on sama. Selleks kasutatakse meetodit *equals*. Tagastusväärtus on true/false.

.. code-block:: java
  
  if (s.equals("hello")) {
      // do something
  }
  
null väärtus
------------

Objektide (ka sõne) puhul on **null** eriline "väärtus". Sisuliselt tähendab see seda, et väärtus on määramata. Kui muidu objekti andmetüüp viitab lihtsustatult mäluaadressile, kus objekti sisu/väärtus salvestatud, siis null tähendab seda, et mälus pole selle objekti kohta (veel) andmeid.
null "väärtusega" objekti puhul ei saa ühtegi meetodit kasutada. Ehk siis määramata sõne puhul :code:`s.length();` tuleks viga "NullPointerException". Kuna s on null, siis meil objekti (sõne) ennast polegi. Seega, kõik pöördumised s poole annavad tulemuseks 'null'.
Kui kirjutada selline kontroll:

.. code-block:: java

	if (s.equals("yes")) {
     	    // do something if user entered "yes"
	}
	
Kui mingil põhjusel s on null, annab programm veateate. Eelnevalt tuleks kontrollida kas s on väärtustatud:

.. code-block:: java

	if (s == null) {
    	    // here s is null
	} else {
    	    // here s is not null, we can use string methods
    	    System.out.println(s.length());
	}
	
Teine võimalus juhul kui meid huvitab, kas kaks sõne on võrdsed, saab kirjutada nii:

.. code-block:: java

	if ("yes".equals(s)) {
    	    // checks if s value is "yes"
	}
	
"yes" on eelmise näite puhul samamoodi sõne ehk objekt. Kuna see objekt ei ole null, võib seda kasutada kontrollimise puhul esimesel kohal. Kui kaks sõne on sama sisuga, siis ei ole vahet, kumba kummaga kontrollime - mõlemal juhul peaks *equals* meetod tagastama *true*.
Järelikult selle näite puhul, isegi kui s on null, ei teki viga sest ei kutsuta selle muutuja kaudu meetodeid välja.

Sõne muutmine
--------------

Sõne on Javas muutumatu - tema sisu ei saa muuta.

Näiteks:	

.. code-block:: java

	String myString = "Apple";
	myString = "Orange";


Sellisel juhul ei muudeta sõne :code:`myString` sisu. Esimene rida loob objekti, mille sisuks on "Apple" ja omistab selle viida myString'ile. Teine rida loob uue objekti, mille sisuks on "Orange" ja omistab selle viida myString'ile. 

Kui nüüd teha näiteks:

.. code-block:: java

	myString += " juice"
	
Selle asemel, et "Orange" muutuks, luuakse täiesti uus sõne objekt sisuga "Orange juice", millel on uus viit.	

Sõne vormindamine
-----------------

Javas on sõne klassis olemas staatiline avalik meetod *format* mis võimaldab konverteerida sisendit soovitud sõne kujule.

Üldine süntaks: **%[argumendiIndeks$][lipud][laius][.täpsus]konverteerimiseKarakter** *([] sees pole kohustuslikud)*

Mõned levinumad konverteerimise karakterid on järgmised:

- s – sõnede vormindamiseks
- d – täisarvude vormindamiseks
- f – ujukomaarvude vormindamiseks
- t – kuupäevade vormindamiseks


Näited koodis:

.. code-block:: java

  String.format("%d", 145); // 145
  String.format("%c", 'a'); // a
  String.format("%f", 11.6455555); // 11.645556

  String.format("Index: %2$s, %1$s", "first", "second"); // Index: second, first
  String.format("Flag: %+f", 234.5); // Flag: +234.500000
  String.format("Width: %5s", "abc"); // Width:   abc
  String.format("Precision: %.2f", 11.6455555); // Precision: 11.65
  
  String.format("name: %s", "John Pineapple"); // name: John Pineapple
  String.format("25 in hexadecimal: %x", 25); // 25 in hexadecimal: 19
  String.format("boolean %B", true); // boolean TRUE
  String.format("boolean %b", true); // boolean true
  String.format("%s%n%s", "onFirstLine", "onSecondLine"); // onFirstLine
                                                          // onSecondLine

-------

Dokumentatsioon: 

https://docs.oracle.com/javase/tutorial/java/data/strings.html

https://docs.oracle.com/javase/8/docs/api/java/lang/String.html
