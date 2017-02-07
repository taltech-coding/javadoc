========================================
Numbrilised andmetüübid ja operatsioonid
========================================

Javas on kasutusel 6 primitiivset numbrilist andmetüüpi:

- Täisarvud: byte, short, int, long
- Ujukomaarvud: float, double

Üldjuhul on soovitatav murdarvude esitamiseks kasutada andmetüüpi **double**, kuna see on täpsem kui float. Ujukomaarvude hoidmine mälus ning nende võimalikud väärtused on veidi keerulisem teema ning seetõttu pole siin tabelis neid välja toodud. Soovi korral võib lugeda näiteks vastavat teemat `Java spetsifikatsioonis
<http://docs.oracle.com/javase/specs/jls/se8/html/jls-4.html#jls-4.2.3>`_.

==========  ====================  ==================  ==================
Tüübi nimi  Suurus                Väärtused           Näide
==========  ====================  ==================  ==================
byte        1 bait (8 bitti)      -128 ... 127        byte b = 42;
short       2 baiti (16 bitti)    -32768 ... 32767    short s = -12345;
int         4 baiti (32 bitti)    -2^31 ... 2^31 - 1  int i = 10;
long        8 baiti (64 bitti)    -2^63 ... 2^63 - 1  long l = -100;
float       32-bitine ujukomaarv  *                   float f = 3.14f;
double      64-bitine ujukomaarv  *                   double d = 1.2345;
==========  ====================  ==================  ==================

Väärtustamine
=============

Numbriliste väärtuste esitamiseks on Javas mitmeid erinevaid võimalusi.

Täisarvutüübid
--------------

Lisaks kümnendsüsteemile on võimaik täisarvude esitamiseks kasutada kahendsüsteemi ning kuueteistkümnendsüsteemi. Sel juhul kasutatakse eristamiseks vastavaid eesliiteid **0b** ning **0x**.

.. code-block:: java

    int a;
    a = 26;      // Decimal value
    a = 0x1a;    // Hexadecimal value
    a = 0b11010; // Binary value

Ujukomatüübid
-------------

Ujukomaarvude esitamisel tuleks kindlasti anda kaasa vähemalt üks komakoht, sest vastasel juhul tõlgendatakse neid algul täisarvuna ning programmi töö muutub aeglasemaks aja võrra, mis kulub teisenduste tegemisele.

.. code-block:: java

    double d1 = 55.0; // good
    double d2 = 55;   // bad

Float tüüpi arvude eristamiseks tuleb neile lisada täht **f** või **F** (pole oluline, kas suur või väike täht). Samamoodi on võimalik double arve tähistada d-tähega, kuid see pole kohustuslik – vaikimisi on komakohtadega arvu andmetüübiks double. Mõlemat tüüpi ujukomaarvude puhul saab kasutada ka teaduslikku notatsiooni, mis kasutab korrutamist kümne astmetega.

.. code-block:: java

    double d1 = 123.4;
    double d2 = 123.4d;  // Adding d or D is optional
    double d3 = 1.234e2; // Scientific notation (e2 -> *10^2)
    float f = 123.4f     // f or F must be added!

Erilised ujukomaarvud
---------------------

Kuigi üldiselt primitiivsete andmetüüpide puhul me saame neile anda vaid konkreetseid väärtusi vastavast andmetüübist, siis **double** võimaldab lisaks "tavalistele" väärtustele hoida ka järgmisi väärtusi:

- Not-a-Number. Sellega saab tähistada olukoda, kus **double** tüüpi muutujas salvestatakse mitte-arvulist väärtust.
- Lõpmatus. Java defineerib nii positiivse kui negatiivse lõpmatuse. Positiivne lõpmatus on kõikidest **double** tüüpi väärtustest suurem, negatiivne jälle kõikidest väiksem.

**Not-a-Number**

*Not-a-Number* väärtuse jaoks kasutatakse konstanti :code:`Double.NaN`. Täpsemalt on NaN defineeritud järgmiselt 

.. code-block:: java

    /** 
     * A constant holding a Not-a-Number (NaN) value of type
     * {@code double}. It is equivalent to the value returned by
     * {@code Double.longBitsToDouble(0x7ff8000000000000L)}.
     */
    public static final double NaN = 0.0d / 0.0;
    
Lisaks kehtib NaN väärtuse puhul järgmine tingimus (ainsana arvudest): :code:`x != x`, kus :code:`x` on NaN. 

Üldisemalt, kõik operatsioonid, milles osaleb vähemalt üks NaN väärtus, annavad tulemuseks NaN. Kui võrdluses osaleb üks või kaks NaN väärtust, siis tulemus on alati :code:`false`. Erandiks on :code:`!=` võrdlus, milles osaleb vähemalt üks NaN, mille tulemus on alati :code:`true`, seal hugas ülaltoodud :code:`x != x` näide, kus :code:`x` on NaN.

Selleks, et kontrollida, kas väärtus on NaN, tuleks kasutada järgmist meetodit:

.. code-block:: java

    if (Double.isNaN(x)) {
        // x value is NaN
    }

**Lõpmatus**

Lõpmatuse tähistamiseks saab kasutada konstante :code:`Double.POSITIVE_INFINITY` ja :code:`Double.NEGATIVE_INFINITY`. 

.. code-block:: java

    public static final double NEGATIVE_INFINITY = -1.0d / 0.0;
    public static final double POSITIVE_INFINITY = 1.0d / 0.0;
    
Lõpmatusega seotud tehteid vaata `IEEE 754 standardist <http://steve.hollasch.net/cgindex/coding/ieeefloat.html>`_. Näiteks järgmised read on kõik tõesed:

.. code-block:: java

    boolean b1 = Double.POSITIVE_INFINITY + 11 == Double.POSITIVE_INFINITY;
    boolean b2 = Double.POSITIVE_INFINITY * 2 == Double.POSITIVE_INFINITY;
    boolean b3 = Double.isNaN(Double.POSITIVE_INFINITY + Double.NEGATIVE_INFINITY);

Vaata lisaks:

`Java Language Specification, Floating-Point Types <https://docs.oracle.com/javase/specs/jls/se8/html/jls-4.html#jls-4.2.3>`_

`IEEE Standard 754 Floating Point Numbers <http://steve.hollasch.net/cgindex/coding/ieeefloat.html>`_

`IEEE Floating Point Standard Group <http://grouper.ieee.org/groups/754/>`_

Alakriipsude kasutamine
-----------------------

Numbreid võib lugemise lihtsustamiseks grupeerida, kasutades gruppide eraldamiseks alakriipse.

.. code-block:: java

    long creditCardNumber = 1234_5678_9012_3456L;
    long maxLong = 0x7fff_ffff_ffff_ffffL;
    float pi =  3.14_15F;
    int x = 3______1;

Alakriipse **ei tohi lisada**:

- Numbri algusesse või lõppu (_123, 55\_, 67889L\_, 0x52\_)
- Komakoha kõrvale (2._34, 2\_.34)
- Enne F- või L-lõppu (879_f)
- Teises arvusüsteemis arvu eesliitesse või numbri algusesse (0_x52, 0x_52)

Operatsioonid
=============

Aritmeetilised operatsioonid
----------------------------

Javas on põhiliste aritmeetiliste operatsioonide jaoks defineetitud järgnevad operaatorid:

+---+-------------+
|\+ | Liitmine    |
+---+-------------+
|\- | Lahutamine  |
+---+-------------+
|\* | Korrutamine |
+---+-------------+
| / | Jagamine    |
+---+-------------+
| % | Jääk        |
+---+-------------+

Näide:

.. code-block:: java

    int result = 5 + 2;
    System.out.println(result); // 7

    result = result + 3;
    System.out.println(result); // 10

Lisaks on olemas unaarsed operaatorid, mis kasutavad vaid ühte operandi. Operaatorit **+** üldjuhul ei kasutata, kuna numbrid on vaikimisi positiivsed.

+----+-------------------------------------+
| \+ | Positiivne väärtus                  |
+----+-------------------------------------+
| \- | Numbrilise väärtuse inverteerimine  |
+----+-------------------------------------+
| ++ | Suurendamine ühe võrra              |
+----+-------------------------------------+
| -- | Vähendamine ühe võrra               |
+----+-------------------------------------+
| !  | Loogikaväärtuse inverteerimine      |
+----+-------------------------------------+

Ühe võrra suurendamise või vähendamise korral on võimalik valida, kas soovime operatsiooni läbi viia enne või peale väärtuse kasutamist.

.. code-block:: java

    int result = 5;

    result++;
    System.out.println(result);   // 6

    System.out.println(result++); // Still 6, because value is read before incrementing
    System.out.println(result);   // Now it is 7

    System.out.println(++result); // 8, because value is incremented before reading
    System.out.println(result);   // Still 8, because nothing changed after reading


Võrdlemine
----------
+----+--------------------+
| == | võrdub             |
+----+--------------------+
| != | ei võrdu           |
+----+--------------------+
| >  | suurem kui         |
+----+--------------------+
| >= | suurem või võrdne  |
+----+--------------------+
| <  | väiksem kui        |
+----+--------------------+
| <= | väiksem või võrdne |
+----+--------------------+

Näide:

.. code-block:: java

    double first = 2.567;
    double second = 5.654;

    System.out.println(first > second); // false
    System.out.println(first < second); // true

Võrdlusi saab kasutada näiteks tingimuslausetes või tsüklites programmi töö juhtimiseks.

Operatsioonid bittidega
-----------------------

Järgnevaid operatsioone tehakse väärtuse iga bitiga eraldi. Neid kasutatakse harva, kuid sellegipoolest on oluline teada, et selline võimalus on olemas.

+-----+-----------------------+
| >>  | märgiga nihe paremale |
+-----+-----------------------+
| <<  | märgiga nihe vasakule |
+-----+-----------------------+
|\>>> | nihe paremale         |
+-----+-----------------------+
| <<< | nihe vasakule         |
+-----+-----------------------+
| ~   | inversioon (EI)       |
+-----+-----------------------+
| &   | konjunktsioon (JA)    |
+-----+-----------------------+
| \|  | disjunktsioon (VÕI)   |
+-----+-----------------------+
| ^   | välistav VÕI (XOR)    |
+-----+-----------------------+

Näide:

.. code-block:: java

    int a = 5;                  // 101
    int b = 6;                  // 110

    int result = a & b;         // 100
    System.out.println(result); // Printed as a decimal (4)

Ületäide
========

Iga numbriline muutuja kasutab mälus kindlat arvu bitte. Bittide arv ei olene mitte väärtusest, mida ta sisaldab, vaid valitud andmetüübist. Seetõttu on oluline andmetüübi valimisel mõelda, kui suuri väärtusi plaanitakse muutujas hoida.

Juhul kui muutuja väärtustamisel antakse väärtus, mis on väljaspool andmetüübi lubatud piire, väljastab Java kompilaator vastava hoiatuse. Arenduskeskkonnad nagu IntelliJ leiavad vea üles juba koodi kirjutamisel ning hoiatavad teid kohe. Kui aga aritmeetiline ületäitumine tekib mõne operatsiooni käigus, ei ilmu selle kohta ühtegi veateadet. Operatsioon justkui õnnestub, kuid väärtus on vale – kõige kõrgemat bitti ei arvestata ning minnakse ringiga kõige väiksema (või suurema) väärtuse juurde tagasi.

.. code-block:: java

    byte b = 127; // Largest possible byte value
    b++;          // New value -128 (smallest possible)

Numbriklassid
=============

Iga primitiivse andmetüübi jaoks on Javas olemas klass (ing k *Wrapper* ehk pakend), mis sisaldab erinevaid kasulikke meetodeid ja konstante. Toome siinkohal välja vaid paar sellist, mida teil kindlasti vaja läheb. Lisaks neile võib tutvuda vastavate osadega Java dokumentatsioonis, näiteks `Integer klassi väljad ja meetodid
<https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html>`_.

MAX_VALUE, MIN_VALUE
--------------------

Konstandid MAX_VALUE ja MIN_VALUE sisaldavad valitud andmetüübi maksimaalset ja minimaalset võimalikku väärtust. Ujukomaarvude puhul sisaldab MIN_VALUE vähimat positiivset väärtust ning MAX_VALUE kõige kõrgemat lõplikku väärtust.

.. code-block:: java

    int i = Integer.MAX_VALUE;
    System.out.println(i);     // 2147483647

    byte b = Byte.MIN_VALUE;
    System.out.println(b);     // -128

parseInt(), parseDouble() jt
----------------------------

Kasutatakse sõne numbriks teisendamisel. Integer klassi puhul on meetodi nimi parseInt, Float klassil parseFloat jne.

.. code-block:: java

    int i = 4;
    String number = "56";

    int j = Integer.parseInt(number);
    int sum = i + j;
    System.out.println(sum);          // 60

Tehted numbriklassidega
-----------------------

Numbriklasse saab kasutada primitiivsete andmetüüpide asendamiseks, kuid kuna luuakse objektid, tuleb operandide asemel kasutada neile vastavaid meetodeid. Väärtuse kättesaamiseks saab kasutada erinevaid meetodeid nagu intValue(), longValue(), toString() jne.

.. code-block:: java

    Integer i = new Integer(45);
    Integer j = new Integer(60);

    Integer sum = Integer.sum(i, j);
    System.out.println(sum.intValue());  // 105

BigInteger ja BigDecimal klassid
---------------------------------

Lisaks põhilistele numbriklassidele (Byte, Short, Long, Integer, Float, Double) on olemas ka klassid **BigInteger** ja **BigDecimal**. Neid saab kasutada väga suurte väärtuste hoidmiseks.

.. code-block:: java

    BigInteger i = BigInteger.valueOf(Integer.MAX_VALUE); // Largest int value (2147483647)
    BigInteger j = BigInteger.valueOf(1);
    BigInteger sum = i.add(j);
    System.out.println(sum.toString());                   // Result is 2147483648
