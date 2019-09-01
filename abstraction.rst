===========
Abstraction
===========

Mis on abstraktsioon?
---------------------

Abstraktne meetod on meetod, mis on deklareeritud, kuid millel pole implementatsiooni, ehk see on olemas kuid ei tee midagi.
Abstraktne klass on klass, milles on vähemalt üks abstraktne meetod.

Abstraktsus on kasulik näiteks juhul, kui sul on meetod, mida kõik alamklassid peavad realiseerima, aga kõik realiseerivad seda erinevalt.

Võtame näiteks ülemklassi Animal:

.. code-block:: java

    public abstract class Animal {
        public void eat(Food food) {
            // eat food
        }

        public void sleep() {
            // sleep
        }

        public abstract void makeNoise();
    }

Kõik loomad söövad ja magavad ühtemoodi, järelikult need meetodid on ülemklassis implementeeritud. Kõik loomad samuti teevad häält, aga erinevad loomad teevad erinevat häält, nii et makeNoise meetodi peab igas alamklassis erinevalt implementeerima.

.. code-block:: java

    public Dog extends Animal {
        public void makeNoise() {
            System.out.println("Woof");
        }
    }
    
    public Cat extends Animal {
        public void makeNoise() {
            System.out.println("Meow");
        }
    }

Nii Dog kui Cat alamklassis on makeNoise meetod realiseeritud

Miks on abstraktsioon kasulik?
------------------------------

Abstraktne klass on ideeliselt segu tavalisest klassist ja liidesest(*interface*). Samamoodi saaks Animal klassi deklareerida liidesena ja lasta Dog ja Cat klassil seda implementeerida, aga siis peaks igas klassis ka eat ja sleep meetodid eraldi implementeerima. Abstraktse klassiga on võimalik osad meetodid ära implementeerida ning jätta osad meetodid abstraktseks ning siis saab abstraktset klassi saab kasutada samamoodi kui tavalist klassi.
