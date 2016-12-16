==================
Meetodi argumendid
==================

Kirjeldus
---------

Meetodi argumendid on parameetrid, mis meetodile ette antakse. Neid parameetreid saab meetod oma töös kasutada.

Näide
-----
    
.. code-block:: java
    
    public class Example {

        // The arguments given to the method are 2 int-type values (a & b).
        public static int addTwoNumbers(int a, int b) {
            return a + b;
        }

        // Argument given to the method is a String-type value (word).
        public static String loseFirst(String word) {
            return word.substring(1);
        }

        private static int a = 1;

        // This method doesn't need an arguments, it uses the variable 'a'.
        public static int getA() {
            return a;
        }

        // Here we call the methods.
        public static void main(String[] args) {
            System.out.println(addTwoNumbers(1, 2)); // -> 3
            System.out.println(addTwoNumbers(5, 7)); // -> 12
            addTwoNumbers("a", 2.5); // -> error, because we're giving a 
                                     //    different type of value then set in the method declaration.
            System.out.println(addTwoNumbers(4 * 2, 2 * 3)); // -> 14

            System.out.println(loseFirst("Word")); // -> "ord"

            System.out.println(getA()); // -> 1
        }
    }
