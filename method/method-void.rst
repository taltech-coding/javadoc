======================
Meetod tagastustüübita
======================

Kirjeldus
---------

Tagastustüübita meetod on *void* tüüpi. See tähendab, et meetod küll teeb midagi, kuid ei tagasta.

Näide
-----

Void-tüüpi meetodit kasutame näiteks selleks, et globaalseid muutujaid muuta/määrata. Kasutame ka juhul, kui soovime lihtsalt trükkida midagi konsooli vastavalt argumendile, nagu ka alljärgnevas näites:


.. code-block:: java

    public class ExampleVoid {
        public static void examGrade(double points) {
            if (points >= 91) {
                System.out.println("Grade is 5.");
            } else if (points >= 81) {
                System.out.println("Grade is 4.");
            } else {
                System.out.println("Grade is 3 or lower."); 
            }
        }

        public static void main(String[] args) {
            examGrade(83);
        }
    }
