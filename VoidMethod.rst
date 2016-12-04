=======================
Meetod tagastustüübita
=======================

Kirjeldus
---------

Tagastustüübita meetod on void tüüpi. See tähendab, et meetod küll teeb midagi, kuid ei tagasta.

Näide
-----

Void-tüüpi meetodit kasutame näiteks selleks, et globaalseid muutujaid muuta/määrata.

.. code-block:: java

    public class Example {
        private String name;
    
        private void setName(String name) {
            this.name = name;
        }
    
        public static void main(String[] args) {
            Example example = new Example();
            example.setName("Example");
        }
    }
