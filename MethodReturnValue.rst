=======================
Meetodi tagastusväärtus
=======================

Kirjeldus
---------

Meetodi tagastustüüp määrab, millist tüüpi väärtuse meetod tagastab. 

Näide
-----

**1) int - tagastab integer-tüüpi väärtuse (kahe numbri summa)**

.. code-block:: java

        public int addTwoNumbers(int a, int b) {
            return a + b;
        }

**2) double - tagastab double-tüüpi väärtuse (kahe numbri vahe arvestades ka komakohti)**

.. code-block:: java

    public double subtractDoubles(double a, double b) {
        return a - b;
    }

**3) String - tagastab string-tüüpi väärtuse (kaotab ette antud sõnast ära esimese tähe)**

.. code-block:: java

    public String loseFirst(String word) {
        return word.substring(1, word.length());
    }


**4) boolean - tagastab boolean-tüüpi väärtuse (kas esimene arv on suurem kui teine)**

.. code-block:: java

    public boolean firstBigger(int a, int b) {
        return a > b;
    }

**5) array - tagastab integer array tüüpi väärtuse (paneb ette antud arvud massiivi)**

.. code-block:: java

    public int[] intToArray(int a, int b) {
        int[] intArray = new int[2];
        intArray[0] = a;
        intArray[1] = b;
        return intArray;
    }
