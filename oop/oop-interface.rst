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

Edaspidi saavad konkreetsed seda liidest implementeerida, kasutades *implements* võtmesõna.

.. note::
    Hea tava kohaselt tasub kasutada @Override annotatsiooni meetodi kohal mis implementeerib liidese meetodit.

.. code-block:: java

    public class Car implements Vehicle { 
        
        int speed; 
        
        @Override
        public void start() {
            System.out.println("Car is starting");
        }

        @Override
        public void increaseSpeed(int increaseAmount){ 
            speed = speed + increaseAmount; 
        } 
    } 

    public class Bike implements Vehicle { 
        
        int speed; 
        
        @Override
        public void start() {
            System.out.println("Bike is starting");
        }

        @Override
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
        
        @Override
        public void start() {
            System.out.println("Plane is starting");
        }

        @Override
        public void increaseSpeed(int increaseAmount){ 
            speed = speed + increaseAmount; 
        } 

        // Implement some other method from SomeOtherInterface
    } 

Liides saab ka teist liidest laiendada (*extends*).

.. code-block:: java

    interface BaseVehicle {
        public void start();
    }

    interface AirVehicle extends BaseVehicle {
        public void fly();
    }

    public class Helicopter implements AirVehicle {
        @Override
        public void start() {
            System.out.println("Helicopter is starting");
        }

        @Override
        public void fly() {
            System.out.println("Helicopter is taking off");
        }
    }

Liides võib sisaldada *default* ja *static* meetodeid.

.. code-block:: java

    interface TestInterface {
    
      // abstract method (must be overridden)
      void calculateSum(int value1, int value2);
    
      // default method (can be overridden)
      default void defaultPrint() {
        System.out.println("Default method executed");
      }
    
      static void staticPrint() {
        System.out.println("Static method executed");
      }
    }
    
    public class TestClass implements TestInterface {
    
      @Override
      public void calculateSum(int value1, int value2) {
        System.out.println(value1 + value2);
      }
    
      public static void main(String[] args) {
        TestClass testClass = new TestClass();
        testClass.calculateSum(4, 2);
        testClass.defaultPrint();
        TestInterface.staticPrint();
      }
    }
