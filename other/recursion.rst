==========
Rekursioon
==========

Mõiste vms kirjeldamine kasutades mõistet ennast

Programmeerimises: probleemi lahendamiseks kutsub funktsioon ennast välja

Selleks, et programm saaks lõpetada, peab rekursiivsel funktsioonil/meetodil olema lõpetamistingimus. Kui see puudub, on tegemist sisuliselt lõputu tsükliga (kuigi käivitades saame vea, mitte programm ei jää lõputult käima).

Rekursiooni abil jagatakse suur ülesanne väiksemateks tükkideks. Rekursiooni üks samm lahendab ära mingi väikese osa probleemist. Kui seda sammu korduvalt rakendada, lahendatakse suurem probleem.

Kõiki rekursiivseid funktsioone/meetodeid saab kirjutada iteratiivselt (for/while tsüklitega) ja vastupidi. See tähendab, et meetodi, mis prindib välja arvud 1st 10ni kasutades for-tsüklit, saab kirjutada rekursiivselt. Rekursiivse lahenduse puhul for-tsüklit kasutama ei pea. Samamoodi, igasuguse rekursiivse meetodi saab kirjutada iteratiivseks.

Rekursioon võimaldab paljudes olukordades kirjutada lühemat ja tihti ka arusaadavamat (kergemini loetavamat) koodi. Java keel kahjuks ei oska rekursiooniga optimaalselt hakkama saada. Seega, rekursiivne väljakutse on tavaliselt natuke aeglasem kui iteratiivne. See vahe on minimaalne (või olematu). Pigem valitakse rekursiivne lahendus seetõttu, et see on lühem ja selgem.


Sabarekursioon (*tail recursion*)
---------------------------------

Sabarekursiooniks nimetatakse funktsiooni, kus rekursiivne väljakutse on viimane tegevus funktsioonis (funktsioon tagastab rekursiivse väljakutse tulemuse). 

Näide sabarekursiooniga meetodist:

.. code-block:: java
    
    public static void tail(int index) {
        if (index < 1) return; // B
        System.out.println(index); // D

        tail(index - 1); // C
    }
    
    public static void main(String[] args) {
        tail(10); // A
    }
    
Sellise meetodi saaks analoogselt kirjutada for-tsükliga:

.. code-block:: java

    for (int index = 10 /* A */; index >= 1 /* B */; index = index - 1 /* C */) {
        System.out.println(index); /* D */
    }
    
Kahes viimases näites on tähtedega A - D märgistatud koodiosad, mis sisuliselt kokku langevad.

Mõned näited
-------------

Minimaalne kood, mis kasutab rekursiivset väljakutset:

.. code-block:: java

    public class Example1 {
        public static void f() {
            f();
        }

        public static void main(String[] args) {
            f();
        }
    }
    
Kood sisaldab lõputut tsüklit - meetod f() kutsub ennast lõputult välja. Käivitades saame :code:`StackOverflowError`'i. See tuleneb sellest, et iga meetodi olek jäetakse meelde. Kui kõigepealt kutsutakse välja f(), siis jääb main() meetodi olek meelde. Esimene rekursiivne väljakutse jätab välimise f() meetodi oleku meelde jne. Kuigi antud näites olek on minimaalne (muutujaid jms ei sisalda), siis sellegipoolest saab mingi hetk pinu (*stack*) täis.

.. code-block:: java

    public class Example2 {
        public static void f(int n) {
            if (n < 1) {
                System.out.println("Takeoff!");
            } else {
                System.out.println("T:" + n);
                f(n - 1);
            }
        }

        public static void main(String[] args) {
            f(3);
        }
    }

Käivitamisel annab tulemuse:

.. code-block:: console

    T:3
    T:2
    T:1
    Takeoff!

Kui muudame koodis kahe rea asukoha omavahel (*else* lauses):

.. code-block:: java

    public class Example3 {
        public static void f(int n) {
            if (n < 1) {
                System.out.println("Takeoff!");
            } else {
                f(n - 1);
                System.out.println("T:" + n);
            }
        }

        public static void main(String[] args) {
            f(3);
        }
    }
    
Saame tulemuseks vastupidise:

.. code-block:: console

    Takeoff!
    T:1
    T:2
    T:3
    
    
Faktoriaali näide
-----------------

Faktoriaal mingist arvust on kõikide arvude korrutis alates 1-st kuni selle arvuni:

.. n! = 1            , kui n = 0
   n! = (n - 1)! x n , kui n > 0

.. math::

  n! =
  \begin{cases}
    1                 & \quad \text{if } n = 0\\
    (n - 1)! \times n & \quad \text{if } n > 0
  \end{cases}
  
Võttes arvesse eelnevat definitsiooni, proovime arvutada 4!. :code:`4! = (4-1)! * 4 = 3! * 4`. Selleks, et see tulemus välja arvutada, on meil vaja arvutada 3! väärtus. :code:`3! = 2! * 3`. Siin on omakorda vaja 2! tulemust. Pikalt võib lahti kirjutada:

.. code-block:: console

    4! =           3!     * 4 = 
       =       (2!  * 3)  * 4 = 
       =       2!     * 3 * 4 = 
       =   (1!  * 2)  * 3 * 4 = 
       =    1!    * 2 * 3 * 4 = 
       = (0! * 1) * 2 * 3 * 4 = 
       =  1  * 1  * 2 * 3 * 4 = 24
       
Koodinäide:

.. code-block:: java

    public class Factorial {
        public static int f(int n) {
            if (n == 0) return 1;
            return f(n - 1) * n;
        }

        public static void main(String[] args) {
            System.out.println(f(6));
        }
    }

Annab tulemuseks:

.. code-block:: console

    720
   
Fibonacci jada
--------------

.. math::

  F_1 = 1\\
  F_2 = 1\\
  F_n = F_{n-1} + F_{n-2}
  
Esimesed arvud: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Kasutatakse ka varianti, kus esimene element on 0 ja teine 1: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...


Rekursiivne lahendus
~~~~~~~~~~~~~~~~~~~~~~~~~~

Rekursiivne lahendus:
  
.. code-block:: java

    public class Fibo {
        static int cnt = 0;
        public static int fibo(int n) {
            cnt++;
            if (n < 3) return 1;
            return fibo(n - 1) + fibo(n - 2);
        }

        public static void main(String[] args) {
            System.out.println(fibo(11));
            System.out.println("call count: " + cnt);
        }
    }

Selle programmi käivitamine annab tulemuseks:

.. code-block:: console

    89
    call count: 177
    
Kui sama kood käivitada arvuga 40, saame tulmuseks:

.. code-block:: console

    102334155
    call count: 204 668 309

(call count arv on loetavuse mõttes suurusjärkudeks jagatud)

Selleks, et proovida leida 50. elementi, peame muutma andmetüübi long-iks:

.. code-block:: java

    public class Fibo {
        static long cnt = 0;
        public static long fibo(int n) {
            cnt++;
            if (n < 3) return 1;
            return fibo(n - 1) + fibo(n - 2);
        }

        public static void main(String[] args) {
            long start = System.currentTimeMillis();
            System.out.println(fibo(50));
            System.out.println("call count:" + cnt);
            System.out.println(String.format("time: %.2f s", (System.currentTimeMillis() - start) / 1_000.0));
        }
    }


.. code-block:: console

    12586269025
    call count: 25 172 538 049 
    time: 47.16 s
    
    
Iteratiivne lahendus
~~~~~~~~~~~~~~~~~~~~~~~~~~

Kui võrdleme iteratiivse lahendusega:

.. code-block:: java

    public class FiboIterative {
        public static long fibo(int n) {
            long fib = 1; // current
            long prev = 1; // previous
            for (int i = 0; i < n - 2; i++) {
                fib = fib + prev;
                prev = fib - prev;
            }
            return fib;
        }
        public static void main(String[] args) {
            long start = System.currentTimeMillis();
            System.out.println(fibo(50));
            System.out.println(String.format("time: %d ms", (System.currentTimeMillis() - start)));
            
        }
    }
    
Saame tulemuseks:

.. code-block:: console

    12586269025
    time: 0 ms
    
Tsüklite arv: 48
    
Efektiivsem rekursiivne lahendus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Kasutame sama loogikat mis iteratiivse lahenduse puhul.

.. code-block:: java

    public class FiboTail {
        public static long fibo(int n, long fib, long prev) {
            if (n == 1) return prev;
            return fibo(n - 1, fib + prev, fib);
        }

        public static void main(String[] args) {
            long start = System.currentTimeMillis();
            System.out.println(fibo(50, 1, 1));
            System.out.println(String.format("%d ms", (System.currentTimeMillis() - start)));
        }
    }
    
Selle käivitamisel saame:

.. code-block:: console

    12586269025
    time 1 ms

:code:`fibo` väljakutsete arv: 50 (vt järgnevat seletust).

Viimase koodinäidet täpsemalt vaadeldes võime mõelda nii:

* igas väljakutses me vähendame :code:`n` väärtust. Kui alustatakse 50-ga, siis järgmise väljakutsega on :code:`n` väärtus 49 jne. Seega :code:`fibo` meetodit kutsutakse välja 50 korda. See on sama, mida saavutame :code:`for` tsükliga (:code:`for (int n = 50; n >= 1; n--)`).
* iga sammu korral antakse meetodi väljakutsesse uued väärtused. Võime mõelda nii: :code:`fib = fib + prev` ja :code:`prev = fib`. Need on üldiselt samad mis iteratiivse väljakutse puhul. Iteratiivse väljakutse puhul :code:`prev` väärtustamisel on kood natuke erinev. Seda seetõttu, et eelnevalt on :code:`fib` väärtus juba ära muudetud (see on :code:`prev` võrra suurem). Siin rekursiivse väljakutse korral toimub väärtustamine samal hetkel, seetõttu ei pea :code:`prev` väärtust maha lahutama.

Linke
------

Neljast videost koosnev seeria rekursioonist: https://www.youtube.com/playlist?list=PLwr2mqyA0RjawBkQkTmRcWfcptMC8ywLS

Lisalugemist: http://freecontent.manning.com/stack-safe-recursion-in-java/
