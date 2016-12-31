Massiiv
=======

Massiiv (*array*) on järjestatud andmete kogum. Javas saab massiiv koosneda ainult sama tüüpi elementidest. 

Iga element massiivis on nummerdatud. Esimese elemendi indeks on 0, teise elemendi indeks on 1 jne. Viimase elemendi indeks on pikkus - 1. Igale konkreetsele elemendile viitamiseks saab kasutada tema indeksit massiivis. Üldisemal juhul võib indekseid olla ka rohkem kui üks - sellisel juhul on tegemist mitmemõõtmelise massiiviga. Mitmemõõtmelise massivi juhul on massiivi elementideks omakorda massiivid.

.. image:: /images/array.png

Massiivil on kindel pikkus, st kui mitu elementi massiivi maksimaalselt mahub. Massiivi pikkust ei saa muuta.

Massiivi loomine
---------------

Kui me soovime näiteks luua täisarvude massiivi *someNumbers*, siis saaksime selle deklareerida nii: 

.. code:: java
    
    int[] someNumbers = new int[10];

Sellisel juhul on massiivi elemendi tüüp int (täisarv). Lisaks määratakse ka massiivi pikkus, milleks on 10 elementi, st reserveeritakse mälu massiivile. Esimene element on :code:`someNumbers[0]`. Esimese elemendi saaks väärtustada nii: :code:`someNumbers[0] = 5;`.

Peale täisarvude (*int*) massiivi on võimalik on deklareerida ka teisi tüüpi massiive:

.. code:: java

    byte[] anArrayOfBytes;
    short[] anArrayOfShorts;
    long[] anArrayOfLongs;
    float[] anArrayOfFloats;
    double[] anArrayOfDoubles;
    boolean[] anArrayOfBooleans;
    char[] anArrayOfChars;
    String[] anArrayOfStrings;
    
Massiivi on võimalik luua ka algväärtustatult:

.. code:: java
    
    int[] someNumbers = {10, 20, 33, 47, 99, 101};
    
Sellisel juhul luuakse uus massiiv, mille pikkus on 6. See on samaväärne sellega:

.. code:: java
    
    int[] someNumbers = new int[7];
    someNumbers[0] = 10;
    someNumbers[1] = 20;
    someNumbers[2] = 33;
    someNumbers[3] = 47;
    someNumbers[4] = 99;
    someNumbers[5] = 101;

Massiivi pikkus
----------------

Massiivi pikkuse leidmiseks saab kasutada: :code:`int len = someNumbers.length;`.

.. code:: java

    int[] otherNumbers = new int[5];
    otherNumbers[0] = 3;
    othernumbers[1] = 7;

Selle näite korral luuakse massiiv, milles on 5 elementi ning väärtustatakse ainult kaks elementi. Kui küsida, mis on massiivi pikkus, siis vastus on 5. Massiivi pikkus on alati fikseeritud selle numbriga, mis massiivi loomise hetkel määratud sai.

Mitmemõõtmeline massiiv
------------------------
    
-------

https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html
