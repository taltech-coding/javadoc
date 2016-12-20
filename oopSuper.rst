************************************************
Võtmesõna super
************************************************

Kui on selged sellised terminid nagu override ja overload, siis on paras liikuda *super* võtmesõna juurde.

Kuidas pääseda ligi ülemklassi meetoditele ja väljadele?
----------------------------------------------------------


Kui teie alamklassis asuv meetod kirjutab üle mõne ülemklassis oleva meetodi (override), on ikkagi võimalik pääseda ülekirjutatud meetodi juurde ülemklassis. Seda saab teha *super* võtmesõna abil. Ütleme, et meil on ülemklass **Superclass**.


.. code-block:: java

    public class Superclass {
    
        public void printMethod() {
            System.out.println("Printed in Superclass.");
        }
    }    

Samuti on meil olemas alamklass **Subclass**, mis laiendab ülemklassi ning kirjutab üle meetodi *printMethod()*

.. code-block:: java
    
        public class Subclass extends Superclass {
    
            @Override
            public void printMethod() {
                super.printMethod();
                System.out.println("Printed in Subclass");
            }
            
            public static void main(String[] args) {
                Subclass s = new Subclass();
                s.printMethod();    
             }
       }
    
Alamklassi meetod *printMethod()* kirjutab üle ülemklassi meetodi *printMethod()*. Samas, kui on soov kutsuda välja just ülemklassi meetod *printMethod()*, siis on tarvis kasutada võtmesõna **super**. Konsooli trükitakse:

.. code-block:: java
    
    Printed in Superclass.
    Printed in Subclass    


Ehk siis alguses käivitakase ülemklassi meetod **printMethod()** ning siis pöördutakse tagasi alamklassi System.out.println() poole, et trükkida *"Printed in Subclass"*.


- NB! Samamoodi on võimalik pääseda ülemklassi välja juurde.



.. code-block:: java
    
        class Vehicle {
        
            int speed = 50;

            void displaySpeed() {
                System.out.println("Vehicle speed is " + speed);
            }
        }    
        
        class Ferrari extends Vehicle {
        
            int speed = 100;

            void displaySuperSpeed() {
                System.out.println("The superlcass speed is " + super.speed);
            }

            void displaySpeed() {
                System.out.println("Ferrari speed is " + speed);
            }
            
            public static void main(String[] args) {

                Vehicle a = new Vehicle();

                a.displaySpeed();

                Ferrari b = new Ferrari();

                b.displaySuperSpeed();
                b.displaySpeed();
            }
        }




Ülaltoodud näites on meil kaks klassi. *Ferrari* laiendab *Vehicle* klassi. Mõlemal klassil on olemas väli *speed*, mida hakkame välja kutsuma. Alguses teeme *Vehicle* klassi objekti ning kutsume välja *displaySpeed()*, saame konsooli trükitud numbri **50**, kuna see on antud välja väärtus selles klassis. *Ferrari* klassis aga on oma *speed*, mis peidab ära *speed* välja ülemklassis. Seepärast, kui me kasutame **.super** võtmesõna, saame kätte ülemklassi *speed* väärtuse, aga tavajuhul saame kätte just *ferrari* klassis oleva välja *speed* väärtuse.

.. code-block:: java

       Vehicle speed is 50
       The superlcass speed is 50
       Ferrari speed is 100

    
Alamklassi konstruktor
----------------------

Ütleme, et meil on ülemklass **Bicycle** ning alamklass **MountainBike**. Jägmises näites on näha, kuidas alamklassi MountainBike konstruktoris kutsutakse välja ülemklassi konstruktor ning pärast seda seadistatakse veel alamklassile iseloomulik väli *seatHeight*.

.. code-block:: java

    public class Bicycle {

        // the Bicycle class has
        // three fields
        public int cadence;
        public int gear;
        public int speed;

        // the Bicycle class has
        // one constructor
        public Bicycle(int startCadence, int startSpeed, int startGear) {
            gear = startGear;
            cadence = startCadence;
            speed = startSpeed;
        }

        // the Bicycle class has
        // four methods
        public void setCadence(int newValue) {
            cadence = newValue;
        }

        public void setGear(int newValue) {
            gear = newValue;
        }

        public void applyBrake(int decrement) {
            speed -= decrement;
        }

        public void speedUp(int increment) {
            speed += increment;
        }

    }


    public class MountainBike extends Bicycle {

        // the MountainBike subclass has
        // one field
        public int seatHeight;

        // the MountainBike subclass has
        // one constructor
        public MountainBike(int startHeight, int startCadence,
                            int startSpeed, int startGear) {
            super(startCadence, startSpeed, startGear);
            seatHeight = startHeight;
        }   

        // the MountainBike subclass has
        // one method
        public void setHeight(int newValue) {
            seatHeight = newValue;
        }   
    }


Kui almaklassi konstruktoris kutsutakse välja meetod super(), siis käivitub ülemklassi argumendita konstruktor. Kui kutsutakse välja super(*argumentide list*), siis käivitub vastavate argumentidega ülemklassi konstruktor.

- NB! super() kutsutakse iga alamklassi konstruktori alguses Java poolt automaatselt välja nii, et seda polegi koodis näha (Kui seda ülemklassis pole, päritakse konstruktor Object klassilt). Kui ülemklassis on defineeritud ainult argumentidega konstruktor, tekib kompilatsiooniviga. Asi on selles, et alati seadistatakse enne ülemklass ning siis alamklassid, seetõttu on alati vaja ligipääsu igale ülemklassile. (Constructor chaining)

