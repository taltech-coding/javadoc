Tsükkel
========

Javas on kahte liiki tsükleid: *while*-tsükkel ja *for*-tsükkel.

Tsükkel (ik *loop*) võimaldab mingit koodiosa korrata teatud reeglite alusel. Kui näiteks programm peab väljastama numbrid ühest viieni, võib seda teha 5 reaga. Samas kui programm peaks väljastama numbrid ühest tuhandeni, oleks 1000 rea kirjutamine väga ebapraktiline. Selle jaoks ongi kasutusele võetud tsüklid, et korrata mingit koodiosa.


*While* tsükkel
-------------

*While*-tsüklit saab kasutada, et mingit koodiosa korrata. Tsükli puhul on oluline määrata ära, kui kaua (ehk mis tingimusel) seda korrata tuleb. 

*While*-tsüklit on kahte liiki: eelkontrolliga ja järelkontrolliga. Nende erinevus seisneb selles, et järelkontrolliga tsükkel kontrollib tingimust alles peale 

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
    
    
*For* tsükkel
------------




--------------

https://docs.oracle.com/javase/tutorial/java/nutsandbolts/while.html
