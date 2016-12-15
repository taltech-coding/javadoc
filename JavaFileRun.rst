========================================
Java-faili kompileerimine ja käivitamine
========================================

Java programm kirjutatakse inimloetavas Java keeles ning salvestatakse java-failina.

Koodinäide:

.. code-block:: java

    /**
     * Add two numbers.
     *
     * @author Britta
     */
    public class Add {
        /**
         * Main entry point.
         * @param args Command line arguments.
         */
        public static void main(String[] args) {
            System.out.println(add(5, 2));
        }

        /**
         * Add two numbers.
         * @param a First number.
         * @param b Second number.
         * @return The sum of a and b.
         */
        private static int add(int a, int b) {
            return a + b;
        }
    }

Java-faili saab käivitada käsurealt (command line). Selleks tuleb fail kõigepealt kompileerida ning siis käivitada. IDE'd (nagu näiteks IntelliJ) teevad kogu selle töö ise ära, kui vajutada Run nuppu.

**Käsureal:** tuleb liikuda õigesse foldrisse ning siis saab Java-faili kompileerida käsuga
*javac failinimi.java*

.. image :: images/Javac.PNG

Java-faili kompileeritakse class-faili, mis koosneb Java baitkoodist ja on seetõttu platvormist sõltumatu.

Siis tuleb programm käivitada.

**Käsureal:** saab Java-faili käivitada käsuga 
*java failinimi*

.. image :: images/JavaAdd.PNG

Programm käivitatakse JVM (Java Virtual Machine) sees ning kuna fail koosneb baitkoodist saab igal platvormil (Windows, Linux, Mac) sama faili käivitades sama tulemuse.
