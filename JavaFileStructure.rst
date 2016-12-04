=====================
Java-faili ülesehitus
=====================

Kirjeldus
---------

Kõige lihtsam Java klass koosneb paketi deklaratsioonist (valikuline), import lausetest (kui neid on vaja), klassi definitsioonist (näites "Example". Panna tähele, et see peab vastama klassi nimele. Antud juhul peaks olema faili nimi Example.java), funktsioonidest ning main-meetodist, mida kasutatakse koodi jooksutamiseks.
Näitena toodud koodis on vaid üks funktsioon ning see liidab kokku 2 ette antud numbrit.
Main meetodis kutsume välja funktsioone, mida soovime käima panna (antud juhul addNumbers). 

Kui main-meetod koodist välja jätta, siis koodi jooksutada ei õnnestu. Samas, kui main-meetod teha, kuid see tühjaks jätta, siis läheb kood tööle, kuid konsooli midagi ei väljasta. Põhjuseks on see, et koodi tööle pannes kasutatakse vaid main-meetodis välja kutsutud funktsioone välja kutsumise järjekorras.

Näide
-----

.. code-block:: java

    public class Example {
        
        public static int addNumbers(int firstNumber, int secondNumber) {
            return firstNumber + secondNumber;
        }
    
        public static void main(String[] args) {
            System.out.println(addNumbers(1, 2));
        }
    }
