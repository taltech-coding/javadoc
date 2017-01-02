====================
Meetodi ülelaadimine
====================

Üldjuhul on meetodite nimed klassi piires unikaalsed. Sellegipoolest on võimalik luua ühes klassis mitu samanimelist meetodit. Sel juhul on tegu meetodi ülelaadimisega (*overloading*).

Ülelaadimise korral erinevad samanimelised meetodid parameetrite arvu ja/või tüüpide poolest. Samuti on erinevad need meetodid, mille parameetrite andmetüüpide järjekord on erinev. Meetodi väljakutsumisel eristatakse neid automaatselt selle põhjal, millised argumendid on antud.

.. code-block:: java

    class OverloadingExample {
        public void say(int a) {
            System.out.println("I will just say the number " + a);
        }

        public void say(String s) {
            System.out.println(s);
        }

        public void say(int a, float b) {
            System.out.format("I will say %d and then %f%n", a, b);
        }

        public void say(float b, int a) {
            System.out.format("I will say %d and then %f, but I received them in a different order%n", a, b);
        }
    }

    class MainClass {
        public static void main(String[] args) {
            OverloadingExample ex = new OverloadingExample();
            ex.say("Hello");
            ex.say(5);
            ex.say(7, 9.5f);
            ex.say(8.65f, 2);
        }
    }

Näite käivitamisel trükitakse konsooli selline väljund::

    Hello
    I will just say the number 5
    I will say 7 and then 9.500000
    I will say 2 and then 8.650000, but I received them in a different order

Kui muutujaid on sama palju ning nende tüübid on samad, siis ülelaadimine ei õnnestu, kuna kompilaator ei suuda neid eristada. Seetõttu ei piisa ka sellest, kui tagastatav andmetüüp on erinev.

Meetodi ülelaadimine: kas õnnestub?
====================================

Toodud on mõned näited meetodi ülelaadimise kohta. Kas selliste näidete puhul meetodi ülelaadimine õnnestub või tekib kompileerimisel viga?

**Näide 1**

.. code-block:: java

    String fullName(String firstName, String lastName) {}
    String fullname(String firstName, String lastName, String middleName) {}
    
Vastus: Õnnestub. Ülelaadimine on võimalik, kuna argumentide arv on erinev.

**Näide 2**

.. code-block:: java

    String fullName(String firstName, String lastName) {}
    String fullname(String lastName, String firstName) {}
    
Vastus: Ei õnnestu. Kuigi muutujate nimed on teises järjekorras, on argumentide nimekirjad identsed – vaadatakse vaid andmetüüpe (String, String).

**Näide 3**

.. code-block:: java

    double sum(int a, double b) {}
    double sum(int x, double y) {}
    
Vastus: Samuti ei toimi. Taaskord vaadatakse ainult andmetüüpe ning nende järjekorda (int, double).

**Näide 4**

.. code-block:: java

    double sum(double a, int b) {}
    double sum(int a, double b) {}
    
Vastus: Töötab! Andmetüüpide järjekord on erinev (double, int; int, double).

**Näide 5**

.. code-block:: java

    double sum(int a, int b) {}
    double sum(double a, double b) {}
    
Vastus: Samuti õige lahendus. Andmetüübid on erinevad.

**Näide 6**

.. code-block:: java

    double sum(int a, double b) {}
    float sum(int a, double b) {}

Vastus: Ei õnnestu. Tagastustüübi muutmisest ei piisa, vaid ka argumentide nimekirjad peavad erinema.

**Lisalugemist:** Joshua Bloch's Effective Java 2nd edition Item 41 (chapter 7).
