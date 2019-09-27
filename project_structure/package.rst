=============
Pakid, teegid
=============

Mooduli loomine
---------------

Pärast Git-iga ühendamist luuakse automaatselt kaust iti0202.
*Clickides* parema hiireklõpsuga selle peale, tuleb valida **New**, mille alt **Module**.

.. image:: /_images/module1.png

Pärast seda avaneb aken, kus saab valida erinevaid Java *framework*-e, aga soovitatav on alguses
neid mitte muuta. Pärast valiku tegemist vajutada **Next** nuppu.

.. image:: /_images/module2.png

Kõige ülemine lahter on mooduli nime jaoks, kuhu tuleb sisestada ülesande kausta nimi.
NB! Ülesande kirjenduses on Kaust Gitis, see on sama asi! 

.. image:: /_images/module3.png

Pärast selle valmis saamist luuakse uus moodul, mille sees on kaust **src**.

Package loomine
----------------

Edasti tuleb teha parem *click* kausta *src* peal, et luua uus *package*.

.. image:: /_images/module4.png

Sellega avaneb uus aken, kuhu tuleb sisestada *package* nimi. Pannes punkti kausta nimede vahele, luuakse
automaatselt alamkaust.
NB! Ülesande kirjelduses on Pakk Gitis, see on jällegi sama asi!

.. image:: /_images/module5.png

Klassi loomine
--------------

Pärast seda tuleb luua Java klass. Jällegi parema hiire *click*-iga valida **NEW** ja siis **Java Class**.

.. image:: /_images/module6.png

Sellega avaneb uus aken, kuhu tuleb panna klassi nimi ja vajutada **OK** nuppu.

.. image:: /_images/module7.png

Sellega luuakse uus klass ja sinna saab kopeerida malli.

Kasulik nõuanne
----------------

Kui Te ei soovi, et Teie tühjad kasutad oleksid trepina, siis saab ülevalt
*setting*-ute alt valida, *Flatten packages* ja *Hide Empty Middle Packages*.

.. image:: /_images/module8.png


Näide klassist
---------------

.. image:: /_images/package.png

Kuna klass kuulub paketti "*example*", siis deklareerime selle kohe klassi alguses.

.. code-block:: java

    package example;
    
    public class Example {
        
        public static int addNumbers(int firstNumber, int secondNumber) {
            return firstNumber + secondNumber;
        }
    
        public static void main(String[] args) {
            System.out.println(addNumbers(1, 2));
        }
    }
