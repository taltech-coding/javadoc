========================================
Java-faili kompileerimine ja käivitamine
========================================

Java programm kirjutatakse inimloetava Java koodina ning salvestatakse java-failina.
Java-faili kompileeritakse class-faili, mis koosneb Java baitkoodist ja on seetõttu platvormist sõltumatu.
Programm käivitatakse JVM (Java Virtual Machine) sees ning kuna fail koosneb baitkoodist saab igal platvormil (Windows, Linux, Mac) sama faili käivitades sama tulemuse.

**Koodinäide:**

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

**Käsureal:** tuleb liikuda õigesse kausta ning siis saab Java-faili kompileerida käsuga
*javac failinimi.java*

.. image :: /_images/javac.png

Alternatiivselt ei pea faili kompileerimiseks liikuma sinna kausta, vaid võib kasutada faili pathi. Sellisel juhul peab failis paki ära defineerima.
Näiteks kui faili path on *src/maths/mathsoperations/Add.java* peab faili algusesse kirjutama

.. code-block:: java

    package maths.mathsoperations;

Siis saab faili kompileerida

.. image :: /_images/javac_package.png

Siis tuleb programm käivitada.

**Käsureal:** saab Java-faili käivitada käsuga 
*java failinimi*

.. image :: /_images/java_add.png

Kui kompileerisid faili paki sees, pead faili käivitamisel kasutama failinimena *package1.package2.Main*.

Näiteks:

.. image :: /_images/java_add_package.png
