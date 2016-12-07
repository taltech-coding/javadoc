************************************************
Võtmesõna super
************************************************

Kui on selged sellised terminid nagu override ja overload, siis on paras liikuda *super* võtmesõna juurde.

Kuidas saada ligi ülemklassis meetodite ja väljade juurde?
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
    
Alamklassi meetoid *printMethod()* kirjutab üle ülemklassi meetodi *printMethod()*. Samas, kui on soov kutsuda välja just ülemklassi meetod *printMethod()*, siis on tarvis kasutada võtmesõna **super**. Konsooli trükitakse:

 .. code-block:: java
    
    Printed in Superclass.
    Printed in Subclass    


Ehk siis alguses käivitakase ülemklassi meetod **printMethod()** ning siis pöördutakse tagasi alamklassi System.out.println() poole, et trükkida *"Printed in Subclass"*.




- NB! Samamoodi on võimalik pääseda ülemklassi välja juurde.

 .. code-block:: java
    
        class Vehicle {
            int speed=50;
        }
        
        class Ferrari extends Vehicle {
            int speed=100;
            
            void display(){
                System.out.println("The speed is " + super.speed);
            }

            public static void main(String args[]) {
                Ferrari b = new Ferrari();
                b.display();
            }
        }        


Kuna kasutatud oli **super.speed**, siis konsooli trükitakse:

 .. code-block:: java

        The speed is 50
    
Alamklassi konstruktor
----------------------

Ütleme, et meil on ülemklass **Bicycle** ning alamklass **MountainBike**. Jägmises näites on näha, kuidas alamklassi MountainBike konstruktoris kutsutakse välja ülemklassi konstruktor ning pärast seda seadistatakse veel alamklassile iseloomulik väli *seatHeight*.

 .. code-block:: java

        public MountainBike(int startHeight, int startCadence, int startSpeed,  int startGear) {    
            super(startCadence, startSpeed, startGear);
            seatHeight = startHeight;
        }       


Kui almaklassi konstruktoris kutsutakse välja meetod super(), siis käivitub ülemklassi argumendita konstruktor. Kui kutsutakse välja super(*argumentide list*), siis käivitub vastavate argumentidega ülemklassi konstruktor.

- NB! super() kutsutakse iga alamklassi konstruktori alguses Java poolt automaatselt välja nii, et seda polegi koodis näha. Kui ülemklassis on defineeritud ainult argumentidega konstruktor, tekib kompilatsiooniviga. Asi on selles, et alati seadistatakse enne ülemklass ning siis alamklassid, seetõttu on alati vaja ligipääsu igale ülemklassile. (Constructor chaining)

