Massiiv
=======

Massiiv (*array*) on järjestatud andmete kogum. Javas saab massiiv koosneda ainult sama tüüpi elementidest. 

Iga element massiivis on nummerdatud. Esimese elemendi indeks on 0, teise elemendi indeks on 1 jne. Viimase elemendi indeks on pikkus - 1. Igale konkreetsele elemendile viitamiseks saab kasutada tema indeksit massiivis. Üldisemal juhul võib indekseid olla ka rohkem kui üks - sellisel juhul on tegemist mitmemõõtmelise massiiviga. Mitmemõõtmelise massivi juhul on massiivi elementideks omakorda massiivid.

.. image:: /_images/array.png

Massiivil on kindel pikkus, st kui mitu elementi massiivi maksimaalselt mahub. Massiivi pikkust ei saa muuta.

Massiivi loomine
----------------

Kui me soovime näiteks luua täisarvude massiivi *someNumbers*, siis saaksime selle deklareerida nii: 

.. code:: java
    
    int[] someNumbers = new int[10];

Sellisel juhul on massiivi elemendi tüüp int (täisarv). Lisaks määratakse ka massiivi pikkus, milleks on 10 elementi, st reserveeritakse mälu massiivile. Esimene element on :code:`someNumbers[0]`. Esimese elemendi saaks väärtustada nii: :code:`someNumbers[0] = 5;`

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
    String[] someWords = {"Hello", "new", "array"};
    
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

Massiivi pikkuse leidmiseks saab kasutada: :code:`int len = someNumbers.length;`

Massiiv on objekt, mille avalik *read-only* isendimuutuja nimega *length* sisaldab massiivi pikkust.

.. code:: java

    int[] otherNumbers = new int[5];
    otherNumbers[0] = 3;
    othernumbers[1] = 7;

Selle näite korral luuakse massiiv, milles on 5 elementi ning väärtustatakse ainult kaks elementi. Kui küsida, mis on massiivi pikkus, siis vastus on 5. Massiivi pikkus on alati fikseeritud selle numbriga, mis massiivi loomise hetkel määratud sai.

Mitmemõõtmeline massiiv
------------------------

Massiivid võivad hoida endas ka mitut tulpa, selliseid massiive nimetatakse mitmemõõtmelisteks. Näiteks kahemõõtmelist massiivi võib ette kujutada kui Exceli tabelit või maatriksit, milles on read ja veerud. 

Mitmemõõtmelist massiivi initsialiseerides peab määrama kõikide massiivide suurused.

**Kahemõõtmeline massiiv**

Kahemõõtmelise massiivi loomine:

.. code:: java

    int[][] numbers = new int[6][5];
    
See on nagu tabel, milles on 6 rida ning 5 tulpa. 

.. image:: /_images/multi_dimensional.png

Näiteks soovides lisada esimesse ritta väärtusi, saab seda teha nii:

.. code:: java

    numbers[0][0] = 10;
    numbers[0][1] = 12;
    numbers[0][2] = 43;
    numbers[0][3] = 11;
    numbers[0][4] = 22;

Esimene rida on rida 0. Kolumne on 5 (nullist neljani). Teise ritta saab väärtusi lisada nii:

.. code:: java

    numbers[1][0] = 20;
    numbers[1][1] = 45;
    numbers[1][2] = 56;
    numbers[1][3] = 1;
    numbers[1][4] = 33;

Tegelikult näiteks luues massiiv :code:`A = new int[3][4]`, siis A viitab massiivile, milles on 3 elementi ning iga element viitab massiivile, milles on 4 täisarvu (*int*).

.. image:: /_images/multiarray.png

**Kolmemõõtmeline massiiv**

Seda võib ette kujutada kui massiivi, mis koosneb kahemõõtmelistest massiividest. Initsialiseerimine:

.. code:: java

    int arr[][][];
    arr = new int[2][4][3];
  
Sellisel juhul luuakse massiiv, milles on kaks elementi. Mõlemad viitavad omakorda kahemõõtmelistele massiividele, milles on 4 rida ja 3 veergu.

-------

https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html
