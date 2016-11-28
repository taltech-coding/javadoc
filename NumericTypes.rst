========================================
Numbrilised andmetüübid ja operatsioonid
========================================

Javas on kasutusel 6 primitiivset numbrilist andmetüüpi:

- Täisarvud: byte, short, int, long
- Ujukomaarvud: float, double

Üldjuhul on soovitatav murdarvude esitamiseks kasutada andmetüüpi **double**, kuna see on täpsem kui float. Ujukomaarvude hoidmine mälus ning nende võimalikud väärtused on üleüldse veidi keerulisem teema, millega tuleks iseseisvalt põhjalikumalt tutvuda. (lisada paar linki)

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



Täisarvutüübid
--------------

Lisaks kümnendsüsteemile on võimaik täisarvude esitamiseks kasutada kahendsüsteemi
 ning kuueteistkümnendsüsteemi. Sel juhul kasutatakse eristamiseks vastavaid eesliiteid **0b** ning **0x**.

.. code-block:: java

    int a;
    a = 26;      // numbrina
    a = 0x1a;    // kuueteistkümnendsüsteemis (hexadecimal)
    a = 0b11010; // kahendsüsteemis (binary)

Ujukomatüübid
-------------

Ujukomaarvude esitamisel tuleks kindlasti anda kaasa vähemalt üks komakoht, sest vastasel juhul tõlgendatakse neid algul täisarvuna ning programm tööle lisandub teisendamise aeg.

.. code-block:: java

    double d1 = 55.0; // hea
    double d2 = 55; // halb

Float tüüpi arvude eristamiseks tuleb neile lisada täht **f** (pole oluline, kas suur või väike täht). Samamoodi on võimalik double arve tähistada d-tähega, kuid see pole kohustuslik – vaikimisi on komakohtadega arvu andmetüübiks double. Mõlemat tüüpi ujukomaarvude puhul saab kasutada ka teaduslikku notatsiooni, mis kasutab korrutamist kümne astmetega.

.. code-block:: java

    double d1 = 123.4;
    double d2 = 123.4d;  // d või D pole kohustuslik
    double d3 = 1.234e2; // teaduslikus notatsioonis (e2 -> *10^2)
    float f = 123.4f     // f või F on kohustuslik!!!

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

(-)

Ületäide
========

Iga numbriline muutuja kasutab mälus kindlat arvu bitte. Bittide arv ei olene mitte väärtusest, mida ta sisaldab, vaid valitud andmetüübist. Seetõttu on oluline andmetüübi valimisel mõelda, kui suuri väärtusi plaanitakse muutujas hoida.

Juhul kui muutuja väärtustamisel antakse väärtus, mis on väljaspool andmetüübi lubatud piire, väljastab Java kompilaator vastava hoiatuse. Arenduskeskkonnad nagu IntelliJ leiavad vea üles juba koodi kirjutamisel ning hoiatavad teid kohe. Kui aga aritmeetiline ületäitumine tekib mõne operatsiooni käigus, ei ilmu selle kohta ühtegi veateadet. Operatsioon justkui õnnestub, kuid väärtus on vale – kõige kõrgemat bitti ei arvestata ning minnakse ringiga kõige väiksema (või suurema) väärtuse juurde tagasi.

.. code-block:: java

    byte b = 127; // Maksimaalne väärtus byte andmetüübi jaoks
    b++;          // Uus väärtus on -128 ehk minimaalne väärtus

Numbriklassid
=============

Iga primitiivse andmetüübi jaoks on Javas olemas klass (ing k *Wrapper* ehk pakend), mis sisaldavad erinevaid kasulikke meetodeid ja konstante. Toome siinkohal välja vaid paar sellist, mida teil kindlasti vaja läheb. Lisaks neile võib tutvuda vastavate osadega Java dokumentatsioonist, näiteks `Integer klassi väljad ja meetodid
<https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html>`_.

MAX_VALUE, MIN_VALUE
--------------------

Konstandid MAX_VALUE ja MIN_VALUE sisaldavad valitud andmetüübi maksimaalset ja minimaalset võimalikku väärtust. Ujukomaarvude puhul sisaldab MIN_VALUE vähimat positiivset väärtust ning MAX_VALUE kõige kõrgemat lõplikku väärtust.

.. code-block:: java

    int i = Integer.MAX_VALUE;
    System.out.println(i); // 2147483647
    byte b = Byte.MIN_VALUE;
    System.out.println(b); // -128

parseInt(), parseDouble(), ...
------------------------------

Kasutatakse sõne numbriks teisendamisel.

.. code-block:: java

    int i = 4;
    String number = "56";
    int j = Integer.parseInt(number);
    int sum = i + j;
    System.out.println(sum); // 60

Tehted numbriklassidega
-----------------------

Numbriklasse saab kasutada primitiivsete andmetüüpide asendamiseks, kuid kuna luuakse objektid, tuleb operandide asemel kasutada neile vastavaid funktsioone. Väärtuse kättesaamiseks saab kasutada funktsioone intValue() ja toString().

.. code-block:: java

    Integer i = new Integer(45);
    Integer j = new Integer(60);
    Integer sum = Integer.sum(i, j);
    System.out.println(sum.intValue()); // 105

BigInteger ja BigDecimal klassid
-------------------------------

Lisaks tavalistele klassidele (Byte, Short, Long, Integer, Float, Double) on olemas ka klassid **BigInteger** ja **BigDecimal**. Neid saab kasutada väga suurte väärtuste hoidmiseks.

.. code-block:: java

    BigInteger i = new BigInteger(Integer.MAX_VALUE);     // suurim võimalik int väärtus
    BigInteger j = new BigInteger(Integer.MAX_VALUE - 1); // eelmisest ühe võrra väiksem väärtus
    BigInteger sum = i.add(j);                            // liidame need kokku...
    System.out.println(sum.toString());                   // tulemus on (TULEMUS SIIA)
