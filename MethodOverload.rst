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

Näite käivitamisel trükitakse konsooli selline väljund:

Output::

    Hello
    I will just say the number 5
    I will say 7 and then 9.500000
    I will say 2 and then 8.650000, but I received them in a different order

Kui muutujaid on sama palju ning nende tüübid on samad, siis ülelaadimine ei õnnestu, kuna kompilaator ei suuda neid eristada. Seetõttu ei piisa ka sellest, kui tagastatav andmetüüp on erinev.