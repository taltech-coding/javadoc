==========
Rekursioon
==========

vaata :doc:`rekursioon`.

.. image:: images/recursion_picture.jpg

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
       =   1!     * 2 * 3 * 4 = 
       = (0! * 1) * 2 * 3 * 4 = 
       = 1 * 1 * 2 * 3 * 4 = 24
       


   
Fibonacci jada
--------------

.. math::

  F_1 = 1\\
  F_2 = 1\\
  F_n = F_{n-1} + F_{n-2}
  
Esimesed arvud: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Kasutatakse ka varianti, kus esimene element on 0 ja teine 1: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

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


    


Linke
------

Neljast videost koosnev seeria rekursioonist: https://www.youtube.com/playlist?list=PLwr2mqyA0RjawBkQkTmRcWfcptMC8ywLS

Lisalugemist: http://freecontent.manning.com/stack-safe-recursion-in-java/