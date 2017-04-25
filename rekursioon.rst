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
   
Fibonacci jada
--------------

.. math::

  F_1 = 1
  F_2 = 1
  F_n = F_{n-1} + F_{n-2}
  
Linke
------

Neljast videost koosnev seeria rekursioonist: https://www.youtube.com/playlist?list=PLwr2mqyA0RjawBkQkTmRcWfcptMC8ywLS

Lisalugemist: http://freecontent.manning.com/stack-safe-recursion-in-java/