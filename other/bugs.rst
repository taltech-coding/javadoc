Vead
====

Java on kompileeritud keel, mis võimaldab kompilaatoril suure osa probleemidest tuvastada enne programmi käivitamist, sest kompileerimisvigadega programmi ei saa käivitada.

Koodi kirjutades tuleks programmeerijal arvestada erinevate eriolukordadega, mis võivad programmi käivitamisel või kompileerimisel tekkida. Töökindel programm suudab erinevate olukordadega toime tulla ilma, et jookseks kokku.

Näiteks:

.. code:: java

    int[] numbers = {0, 1, 2, 3};
    System.out.println(numbers[6]); // java.lang.ArrayIndexOutOfBoundsException
    System.out.println(numbers[-6]); // java.lang.ArrayIndexOutOfBoundsException
  
    int n = Integer.parseInt("Some text"); // java.lang.NumberFormatException
  
    String noValue = null;
    noValue.length(); // java.lang.NullPointerException

Tekkinud tõrked jagunevad kaheks: 

- Vigadeks (:code:`java.lang.Error`), mis tähistavad üldiselt tõsiseid probleeme, mille tekkimisel programm tööd jätkata ei saa.
- Erinditeks (:code:`java.lang.Exception`), mis tekivad enamasti loogikavigade tõttu. Kõik ülaltoodud näited on erindid. Erindeid on võimalik ka ise tekitada, näiteks kui soovitakse mõnd veasituatsiooni parandada.


Põhjused
---------

- Koodi või andmete viga - nt. vale tüübiteisendus, massiivi sobimatu indeksi kasutamine, avaldises nulliga jagamine jpm.
- Vead standardmeetodite kasutamisel - nt. kui kasutada :code:`substring()` meetodit sõne töötlemisel, võime saada vea (erindiklassi) *StringIndexOutOfBoundsException*.
- Ise tekitades - Mittesobiva olukorra avastamisel programmi töö käigus, näiteks soovitakse arvelt rohkem raha välja võtta kui seal on.
- Java vead - Tekivad JVM-s, mis käivitab kasutaja kompileeritud programmi.


Ennetamine
------------

Mõni koodilõik vajab teatud tingimuste täitmist selleks, et korrektselt töötada.

.. code:: java

    int[] numbers = {0, 1, 2, 3};
    int i = 4;

    if (i < 0 || i >= numbers.length) {
        // Do something to handle the out-of-range index
        System.out.println("Bad index");
    } else {
        System.out.println(numbers[i]);
    }
    
Sellisel juhul on käsu :code:`System.out.println(numbers[i]);` eeltingimuseks :code:`(i < 0 || i >= numbers.length)`


Stack trace
-------------

Tavaliselt programmi tööle pannes jooksutab Java virtuaalmasin järjest meetodeid, alustades *main* meetodist. Meetodit jooksutades lisatakse see nö kuhja (ik *stack*). Juhul kui terve meetod on jooksutatud, eemaldatakse see kuhjast, et lisada sinna järjekorras järgmine meetod.

Näiteks:

.. code:: java

    public class Main {
    
        public static void main(String[] args) {
            System.out.println("Starting main method")
            m1();
            System.out.println("End main method");
        }

        static void m1() {
            System.out.println("Method One - m1");
            m2();
        }

        static void m2() {
            System.out.println("Method Two - m2");
        }
    }

Meil on nüüd *main* meetod ja kaks teist meetodit - *m1* ja *m2*. Kui programm oma tööd alustab, siis *main* meetod on kuhjas kõige kõrgemal. *main* meetodi sees kutsutakse aga välja *m1* meetod. Kui see meetod välja kutsutakse, läheb ta kuhja tippu. *m1* meetod kutsub välja *m2* meetodi, mis läheb omakorda kuhja tippu. Siis kui *m2* lõpetab töö, annab ta kontrolli tagasi *m1* meetodile ja eemaldatakse kuhjast. Kui *m1* lõpetab töö, siis annab ta kontrolli tagasi *main* meetodile ja omakorda eemaldatakse kuhjast.

Programmi väljund:

:: 

  Starting main method
  Method One - m1
  Method Two - m2
  End main method

Kui meetod *m2* sees peaks tekkima viga, siis otsib Java virtuaalmasin veatöötlust, näiteks *try ... catch* blokki. Kui selles meetodis veatöötlus puudub, siis otsitakse seda *m1* meetodist. Kuna aga *m1* blokis see puudub, siis otsitakse omakorda *main* meetodist. Kui aga lõpuks ka *main* meetodis puudub veatöötlus, visatakse veateade.

Näiteks muutes meetodit *m2*:

.. code:: java

    public class Main {

        public static void main(String[] args) {
            System.out.println("Starting main method");
            m1();
            System.out.println("End main method");
        }

        static void m1() {
            System.out.println("Method One - m1");
            m2();
        }

        static void m2() {
            int x = 10;
            int y = 0;
            double z = x / y;

            System.out.println(z);
            System.out.println("Method Two - m2");
        }
    }

Sellisel juhul on meetodis *m2* nulliga jagamise viga. Programmi käivitades saame väljundiks:

::

  Starting main method
  Method One - m1
  Exception in thread "main" java.lang.ArithmeticException: / by zero
	    at Main.m2(Main.java:17)
	    at Main.m1(Main.java:11)
	    at Main.main(Main.java:5)
  Process finished with exit code 1

      
Seda kutsutakse kui *stack trace*. Read 4-6 osutavad meetoditele ning näitavad ridu kust neid leida võib. Kõige ülemine neist näitab, kus esmalt viga tekkis (meie näites meetod *m2*). Teised read näitavad ülejäänud kuhja, üldiselt lõpetades *main* meetodiga.

------

http://www.javacoffeebreak.com/articles/toptenerrors.html

http://www.homeandlearn.co.uk/java/java_stack_trace.html


