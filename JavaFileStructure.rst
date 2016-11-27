=====================
Java-faili ülesehitus
=====================

Kirjeldus
---------

Kõige lihtsam Java klass sisaldab funktsioone ning main-meetodit, mida kasutatakse koodi jooksutamiseks.
Näitena toodud koodis on vaid üks funktsioon ning see liidab kokku 2 ette antud numbrit.
Main meetodis kutsume välja funktsioone, mida soovime käima panna (antud juhul addNumbers). 

Kui main-meetod koodist välja jätta, siis koodi jooksutada ei õnnestu. Samas, kui main-meetod teha, kuid see tühjaks jätta, siis läheb kood tööle, kuid konsooli midagi ei väljasta. Põhjuseks on see, et koodi tööle pannes kasutatakse vaid main-meetodis välja kutsutud funktsioone välja kutsumise järjekorras.

Näide
-----

.. code-block:: java

    /**
     * @author L33tH4x0r.
     */
    public class Example {
        /**
         * Add two given numbers.
         * @param firstNumber number given.
         * @param secondNumber number given.
         * @return sum of two given numbers.
         */
        public static int addNumbers(int firstNumber, int secondNumber) {
            return firstNumber + secondNumber;
        }
    
        /**
         * Main method.
         * @param args collection of Strings, separated by a space, which can be typed into the program in the terminal.
         */
        public static void main(String[] args) {
            System.out.println(addNumbers(1, 2));
        }
    }
