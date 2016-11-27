=======
Javadoc
=======

Javadoc'i kasutatakse Java failides enamasti selgitamiseks (muutujad, meetodid, klassid, autor jne).

Javadoc näide
-------------

**Klassi javadoc:**

.. code-block:: java

    // import statements

    /**
     * @author      Autori andmed
     * @version     1.6 (praegune versioon <- pole vist vaja??)
     * @since       1.2 (versioon, kus antud fail lisati <- pole vist vaja??)
     */
    public class Test {
        // class body
    }

**Muutuja javadoc:**

.. code-block:: java

    /**
     * The number of days in one week. (muutuja kirjeldus)
     */
    private int daysInWeek = 7;

**Meetodi Javadoc:**

.. code-block:: java

    /**
     * Lühike üherealine kirjeldus meetodi töö kohta.
     * 
     * Pikem kirjeldus meetodi töö kohta.
     *
     * @param firstNumber first number given by the user. (muutuja kirjeldus)
     * @param secondNumber first number given by the user. (muutuja kirjeldus)
     * @return sum of two given numbers. (tagastatava väärtuse kirjeldus)
     */
    public int addNumbers(int firstNumber, int secondNumber) {
        return firstNumber + secondNumber;
    }
