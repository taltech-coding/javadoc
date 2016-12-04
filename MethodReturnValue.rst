=======================
Meetodi tagastusväärtus
=======================

Kirjeldus
---------

Meetodi tagastustüüp määrab, millist tüüpi väärtuse meetod tagastab. 

Näide
-----

**1) Integer - tagastab integer-tüüpi väärtuse (kahe numbri summa)**

.. code-block:: java

        public int addTwoNumbers(int a, int b) {
            return a + b;
        }

**2) Double - tagastab double-tüüpi väärtuse (kahe numbri vahe arvestades ka komakohti)**

.. code-block:: java

    public double subtractDoubles(double a, double b) {
        return a - b;
    }

**3) String - tagastab string-tüüpi väärtuse (kaotab ette antud ssõnast ära esimese tähe)**

.. code-block:: java

    public String loseFirst(String word) {
        return word.substring(1, word.length());
    }


**4) Boolean - tagastab boolean-tüüpi väärtuse (kas esimene arv on suurem kui teine)**

.. code-block:: java

    public boolean firstBigger(int a, int b) {
        return a > b;
    }

**5) List - tagastab integer list tüüpi väärtuse (paneb ette antud arvud listi)**

.. code-block:: java

    public int[] intToList(int a, int b) {
        int[] intList = new int[2];
        intList[0] = a;
        intList[1] = b;
        return intList;
    }
