Tsükkel
========

Tsükkel (ik *loop*) võimaldab mingit koodiosa korduvalt jooksutada teatud reeglite alusel. Kui näiteks programm peab väljastama numbrid ühest viieni, võib seda teha 5 reaga. Samas kui programm peaks väljastama numbrid ühest tuhandeni, oleks 1000 rea kirjutamine väga ebapraktiline. 

Tsükli arhitektuur:

.. image:: /images/loop.png

Javas on kolme liiki tsükleid: eelkontrolliga tsükkel (*while*), järelkontrolliga tsükkel (*do-while*) ja kolmikpäisega tsükkel (*for*).

*While*-tsükkel
-------------

*While*-tsüklit saab kasutada, et mingit koodiosa korrata. Tsükli puhul on oluline määrata ära, kui kaua (ehk mis tingimusel) seda korrata tuleb. 

*While*-tsüklit on kahte liiki: eelkontrolliga ja järelkontrolliga. Eelkontrolliga tsüklis kontrollitakse esmalt, kas tingimus kehtib. Kui kehtib, siis täidetakse tsükli kood ja kontrollitakse tingimust uuesti. Kui tingimus ei kehti, siis väljutakse tsüklist. Järelkontrolliga tsüklis täidetakse kõigepealt kood, seejärel kontrollitakse tingimust. Kui tingimus kehtib, täidetakse kood uuesti, kui mitte, siis väljutakse tsüklist.

**Eelkontrolliga tsüklidirektiiv**

Tsükli sisu täidetakse juhul, kui antud tingimus (*condition*) on tõene.

Süntaks:

.. code-block:: java

    while (condition) {
        statement(s);
    }
    
Tühja kehaga *while*-tsükkel:  

.. code-block:: java

    while (condition);

Näide:

.. code-block:: java

    int i = 0;
    
    while (i < 5) {
        System.out.println(i);
        i++;
    }
    
Sellisel juhul on programmi väljundiks:

.. code-block::

    0
    1
    2
    3
    4
      
**Järelkontrolliga tsüklidirektiiv**

Tingimust kontrollitakse alles pärast tsükli sisu läbimist, seega tsükli sisu läbitakse alati vähemalt ühe korra.
 
Süntaks:

.. code-block:: java

    do {
        statement(s);
    } while (condition);
    
Näide:

.. code-block:: java

    int count = 1;
    
    do {
        System.out.println("Count is: " + count);
        count++;
    } while (count < 4);
    
Sellisel juhul on programmi väljundiks:

.. code-block::

    Count is: 1
    Count is: 2
    Count is: 3
    
*For*-tsükkel
------------

For-tsüklil on Javas kaks erinevat esitust - tavaline for-tsükkel ja for-each ehk for-in tsükkel. For-each tsüklit kasutatakse järjendite ja kollektsioonide korral. 

**Üldtsüklidirektiiv ehk kolmikpäisega tsükkel ehk for-tsükkel.**

Käsk *for* koosneb kolmest osast: 1) kood, mis täidetakse tsükli alguses, 2) tingimuslause, 3) kood, mis täidetakse igal tsükli sammul (iteratsioonil).

Süntaks:

.. code-block::

    for (initialization statement; condition check; increment) {
        statement(s);
    }
   
Tüüpiliselt on eeltegevusteks (*initialization statement*) mingitele muutujatele algväärtuste omistamised. Näiteks: :code:`int i = 0;`. Sellisel juhul kirjeldatakse täisarvutüüpi muutuja *i*, mis on selle tsükli lokaalne muutuja (st. muutuja *i* väärtus ei ole väljaspool tsüklit kasutatav) ja omistatakse sellele algväärtus 0.

Jätkamistingimus (*condition check*) tuleb seada nii, et tsüklit täidetaks täpselt vajalik arv kordi. Kuniks tingimus on tõene (*true*), jooksutatakse tsükli sisu.

.. code-block::

    for (int i = 0; i < 3; i++)

Näiteks soovides tsüklit täita kolm korda, võib tsükli lokaalmuutujale (tsükliloendajale) omistada algväärtuseks nulli ja igal sammul liita tsükliloendajale ühe. Pärast tsükli esimest sammu on tsükliloendaja väärtus siis 1, pärast teist sammu 2 ja pärast kolmandat sammu 3. Neljandat sammu me enam lubada ei tohi, seega peaks tsükli lõpetama niipea, kui tsükliloendaja saab võrdseks 3-ga või 3-st suuremaks. Jätkamistingimus on lõpetamistingimuse vastandtingimus, ehk antud juhul võib tsüklit jätkata nii kaua, kuni tsükliloendaja on veel väiksem kolmest. 

Tsükli sammu järeltegevuseks (*increment*) on sageli mingi muutuja väärtuse suurendamine või vähendamine teatud arvu võrra. Näiteks :code:`i = i + 2;` või :code:`k--;`

Näide:

.. code-block::

    for (int i = 0; i < 5; i++) {
        System.out.println("Hello!");
    }
    
Sellise näite puhul väljastab *for*-tsükkel viis korda teksti "Hello!".

*For*-tsüklit saab kasutada ka selliselt, et mõni (kasvõi kõik) nendest kolmest osast on täitmata. Näiteks:

.. code-block::
    
    int i = 0;
    
    for ( ; i < 10; i++) {
        System.out.println(i);
    }

Järgnevas näites on kõik kolm osa täitmata. Sellisel juhul on tegemist lõputu tsükliga:

.. code-block::

    for ( ; ; ) {
        // your code goes here
    }


**Tsükkel üle kogumi (for-each tsükkel)**

Seda kasutatakse järjendite ja kollektsioonide korral. Saab kasutada ainult siis, kui ei ole vaja järjendi elemente omavahel võrrelda (indeksid peidetakse programmeerija eest ära aga indeksita ei saa nt eelmist/järgmist elementi kätte), asendada ega eemaldada. Järjendit või kollektsiooni läbitakse ainult kindlas suunas.

Näide:

.. code-block::
    
    class EnhancedForDemo {
        public static void main(String[] args){
            int[] numbers = {1,2,3,4,5};
            
            for (int item : numbers) {
                System.out.println("Count is: " + item);
            }
        }
    }

Programmi väljund:

.. code-block::

    Count is: 1
    Count is: 2
    Count is: 3
    Count is: 4
    Count is: 5

--------------

https://docs.oracle.com/javase/tutorial/java/nutsandbolts/while.html

https://docs.oracle.com/javase/tutorial/java/nutsandbolts/for.html
