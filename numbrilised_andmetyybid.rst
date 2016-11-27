========================================
Numbrilised andmetüübid ja operatsioonid
========================================

Javas on kasutusel 6 primitiivset numbrilist andmetüüpi:
- Täisarvud: byte, short, int, long
- Ujukomaarvud: float, double

(Üldisem lõik nende kohta. Võib lisada tabeli pikkuste, väärtuste ja näidetega)

Väärtustamine
=============

(Sissejuhatav tekst.)

Täisarvutüübid
--------------

(Seletav tekst)

.. code-block:: java

    int a;
    a = 26;      // numbrina
    a = 0x1a;    // kuueteistkümnendsüsteemis (hexadecimal)
    a = 0b11010; // kahendsüsteemis (binary)

Ujukomatüübid
-------------

(Seletav tekst)

.. code-block:: java

    double d;
    d = 123.4;
    d = 1.234e2; // teaduslikus notatsioonis (e2 -> *10^2)
    f = 123.4f

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
- Kuueteistkümnendarvu prefiksisse või numbri algusesse (0_x52, 0x_52)

Ületäide
========

Iga numbriline muutuja kasutab mälus kindlat arvu bitte. Bittide arv ei olene mitte väärtusest, mida ta sisaldab, vaid valitud andmetüübist. Seetõttu on oluline andmetüübi valimisel mõelda, kui suuri väärtusi plaanitakse muutujas hoida.

Juhul kui muutuja väärtustamisel antakse väärtus, mis on väljaspool andmetüübi lubatud piire, väljastab Java kompilaator vastava hoiatuse. Kui aritmeetiline ületäitumine tekib mõne operatsiooni käigus, ei ilmu selle kohta aga ühtegi teadet. Operatsioon justkui õnnestub, kuid väärtus on vale – kõige kõrgemat bitti ei arvestata ning jõutakse ringiga kõige väiksema (või suurema) väärtuse juurde tagasi.

.. code-block:: java

    byte b = 127; // Maksimaalne väärtus byte andmetüübi jaoks
    b++;          // Uus väärtus on -128 ehk minimaalne väärtus

Numbriklassid
=============
(Ümbrised? Numbriklassid? Pakendid?(e-Teatmik))

(Vastavate klasside nimekiri, parseInt, MAX_VALUE jms kasutamine)

Operatsioonid
=============

(-)
