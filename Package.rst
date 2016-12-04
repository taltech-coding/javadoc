=============
Pakid, teegid
=============

Kirjeldus
---------

Pakk (ehk package) deklareerib, kuhu paketti klass kuulub.

Näide
-----

Kuna klass kuulub paketti "example", siis deklareerime selle kohe klassi alguses.

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
