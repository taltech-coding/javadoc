==================
Meetodi argumendid
==================

Kirjeldus
---------

Meetodi argumendid on parameetrid, mis meetodile ette antakse. Neid parameetreid saab meetod oma töös kasutada.

Näide
-----

**Siin on meetodi argumentideks 2 integer-tüüpi väärtust:**

.. code-block:: java

        public int addTwoNumbers(int a, int b) {
            return a + b;
        }
        
**Seda meetodit kutsume välja niimoodi:**

.. code-block:: java

        public static void main(String[] args) {
                addTwoNumbers(1, 2); // -> 3
                addTwoNumbers(5, 7); // -> 12
                addTwoNumbers("a", 2.5); // -> error, kuna meetodis on sisendväärtused deklareeritud int-tüübina, aga üritame ette anda String ning double tüüpi väärtuseid.

**Siin on meetodi argumendiks string-tüüpi väärtus:**

.. code-block:: java

    public String loseFirst(String word) {
        return word.substring(1, word.length());
    }

**Selles meetodis ei anta ette argumenti:**

.. code-block:: java

    private int a = 1;
    
    public int getA() {
        return a;
    }
