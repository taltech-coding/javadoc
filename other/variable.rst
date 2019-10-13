=======
Muutuja
=======

Java on tüübikindel keel, mis tähendab, et iga muutuja ees peab olema deklareeritud andmetüüp (näiteks int, double jne).
Muutujaid kasutatakse erinevate vajalike väärtuste hoidmiseks. Näiteks :code:`int MAX_WIDTH = 10;` hoiab endas soovitud asja maksimaalset laiust.
Muutujanimed kirjutatakse jälgides **camelCase** tehnikat (s.t algab väikese tähega ning iga järgmine sõna algab suure algustähega).

Samuti on Javas *primitiivsed* andmetüübid ning *objekti* muutujad. Erinevus on hästi kirjeldatud siin_.

.. _siin: http://stackoverflow.com/questions/8660691/what-is-the-difference-between-integer-and-int-in-java


Kirjeldus
---------

- *int*-tüüpi muutuja on täisarvuline number.
- *float*-tüüpi muutuja on komakohaga arv (4 baidine).
- *double*-tüüpi muutuja on komakohaga arv (8 baidine).
- *byte*-tüüpi muutuja minimaalne väärtus on -128 (-2^7) ning maksimaalne väärtus 127 (2^7-1).
- *char*-tüüpi muutuja koosneb ühest Unicode sümbolist.
- *String*-tüüpi muutuja on kas täht, sõna või tekst.
- *boolean*-tüüpi muutuja on kas "true" või "false".

Muutuja võib olla lokaalne või globaalne.

Näited
------

**Muutujad:**

.. code-block:: java

    int a, b, c;         // declare 3 integers: a, b and c
    int d = 10, e = 10;  // initializing
    float pi = 3.14159f;
    double pi2 = 3.14159;
    byte f = 22;
    char g = 'g';
    String word = "word or text";
    boolean illuminatiConfirmed = true;

**Lokaalsed ja globaalsed muutujad:**

.. code-block:: java

    public class Example {
        private static int sum; // global variable
    
        private static int addToSum(int a, int b, int c) {
            int sum = a + b + c; // local variable
            return sum;
        }
    
        public static void main(String[] args) {
            sum += addToSum(1, 2, 3);
            System.out.println(sum);
        }
    }
