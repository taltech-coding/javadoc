Liides
======

Liides (*interface*) on abstraktne klassilaadne struktuur, mis võib sisaldada erinevaid meetode või konstantseid muutujaid. Liidest ennast otse kasutada ei saa, selle kasutamiseks tuleb mingis teises konkreetses klassis liidese poolt ette antud meetodid implementeerida. Algses liideses defineeritakse ainult meetodite nimed, parameetrid ja tagastustüübid, kuid meetodite sisu jäetakse tühjaks. Liidese eesmärk on kirjeldada mingit objekti ning määrata, milline üldine funktsionaalsus sellel peaks olema.

Üldiselt saab liidese luua järnevalt:

.. code-block:: java

    interface InterfaceNameHere {
       // Liidese sisu: muutujad, meetodid
    }

Näiteks erinevate sõidukite jaoks võib esmalt luua üldise liidese sõiduki jaoks.
    
.. code-block:: java

    public interface Vehicle { 
        void start();
        void increaseSpeed(int increaseAmount); 
    }

Edaspidi saavad konkreedsed seda liidest implementeerida, kasutades *implements* võtmesõna.

.. code-block:: java

    public class Car implements Vehicle { 
        
        int speed; 
        
        public void start() {
            System.out.println("Car is starting");
        }

        public void increaseSpeed(int increaseAmount){ 
            speed = speed + increaseAmount; 
        } 
    } 

    public class Bike implements Vehicle { 
        
        int speed; 
        
        public void start() {
            System.out.println("Bike is starting");
        }

        public void increaseSpeed(int increaseAmount){ 
            speed = speed + increaseAmount; 
        } 
    } 

.. note::
    Juhul kui liidest implementeeriv klass on abstraktne, siis ei pea kõiki liideses defineeritud meetodeid realiseerima.

Üks klass saab implementeerida mitu liidest korraga.

.. code-block:: java

    public class Plane implements Vehicle, SomeOtherInterface { 
        
        int speed; 
        
        public void start() {
            System.out.println("Plane is starting");
        }

        public void increaseSpeed(int increaseAmount){ 
            speed = speed + increaseAmount; 
        } 

        // Implement some other method from SomeOtherInterface
    } 

Liides saab ka teist liidest laiendada (*extends*).

.. code-block:: java

    public interface BaseVehicle {
        public void start();
    }

    public interface AirVehicle extends BaseVehicle {
        public void fly();
    }

    public class Helicopter implements Airvehicle {
        public void start() {
            System.out.println("Helicopter is starting");
        }

        public void fly() {
            System.out.println("Helicopter is taking off");
        }
    }

