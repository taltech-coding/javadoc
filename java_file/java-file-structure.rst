=====================
Java-faili ülesehitus
=====================

Kirjeldus
---------

Kõige lihtsam Java fail koosneb paketi deklaratsioonist (valikuline), import lausetest (kui neid on vaja), klassi definitsioonist, funktsioonidest ning main-meetodist, mida kasutatakse koodi jooksutamiseks.

Näites on klassi definitsioon *public class Example*. Faili nimi tuleneb klassi nimest. Kui klassi nimi on *Example*, siis faili nimi peab olema *Example.java*.

.. image:: /_images/file_structure.gif

Näitena toodud koodis on vaid üks funktsioon ning see liidab kokku 2 ette antud numbrit.
Main meetodis kutsume välja funktsioone, mida soovime käima panna (antud juhul addNumbers). 

Kui main-meetod koodist välja jätta, siis koodi jooksutada ei õnnestu. Samas, kui main-meetod teha, kuid see tühjaks jätta, siis läheb kood tööle, kuid konsooli midagi ei väljasta. Põhjuseks on see, et koodi tööle pannes kasutatakse vaid main-meetodis välja kutsutud funktsioone välja kutsumise järjekorras.

Näide
-----

.. code-block:: java

    // Here are the imports, if there are any.
    
    // Class definition.
    public class Example {
        
        // Function.
        public static int addNumbers(int firstNumber, int secondNumber) {
            return firstNumber + secondNumber;
        }
    
        // Main method used to run the code.
        public static void main(String[] args) {
            System.out.println(addNumbers(1, 2));
        }
    }
