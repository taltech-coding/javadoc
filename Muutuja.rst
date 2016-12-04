=======
Muutuja
=======

Kirjeldus
---------

- Integer-tüüpi muutuja on täisarvuline number.
- Double-tüüpi muutuja on komakohaga.
- Byte-tüüpi muutuja minimaalne väärtus on -128 (-2^7) ning maksimaalne väärtus 127 (2^7-1).
- Character-tüüpi muutuja koosneb ühest Unicode tähest.
- String-tüüpi muutuja on kas täht, sõna või tekst.
- Boolean-tüüpi muutuja on kas "true" või "false".

Muutuja võib olla lokaalne või globaalne.

Näide
-----

**Muutujad:**

.. code-block:: java

    int a, b, c;         // Deklareerib 3 integeri: a, b ja c
    int d = 10, e = 10;  // Initsialiseerimine
    byte F = 22;
    double pi = 3.14159;
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
    
        public static void main(String args[]) {
            sum += addToSum(1, 2, 3);
            System.out.println(sum);
        }
    }
