Konstruktorid
================================================
-----------------------------------------------------------------------------------------
*Konstruktorite abil luuakse klassi isendeid*
-----------------------------------------------------------------------------------------
Konstruktor on koodi plokk, mis võimaldab tekitada klassidest objekte. Konstruktor meenutab kujult meetodit, kui päriselt ei ole ta meetod. Konstruktor erineb meetodist seepärast, et 

1. Konstruktori nimi peab olema **sama**, mis klassi nimi.

2. Konstruktoritel ei ole tagastustüüpi, isegi mitte *void*.

3. Konstruktor kutsutakse välja **new** operaatori abil, objekti loomise ajal. Konstruktorite roll on luua objekt.

*Konstruktorite tüübid* 
-----------------------

1. **Default konstruktor**

Kui klassis ei ole eraldi deklareeritud konstruktorit, siis java deklareerib ise automaatselt sellise *default* konstruktori, mida ei ole füüsiliselt koodis näha. Igal klassil on seega olemas konstruktor.

.. code-block:: java

    class Demo {
         public Demo() {
         }
    }

**NB!** Nii näeb välja *default* konstruktor klassis *Demo*, kuid kuna me oleme selle ise kirja pannud, siis ei loeta seda enam *default* konstruktoriks. *Default* on siis, kui seda ei kirjutata välja!
 

2. **Argumendita konstruktor**

.. code-block:: java

    class Demo {
         public Demo() {
            System.out.println("This is a constructor without parameters!")
         }
    } 

Argumendita konstruktor sarnaneb signatuurilt *default* konstuktoriga, kuid koodi keha võib teha ükskõik mida. Antud juhul objekti loomisel trükitakse konsooli: "This is a constructor without parameters!".

3. **Argumentidega konstruktor**

Sel juhul antakse konstuktorisse veel eraldi argumendid. Neid võib olla ükskõik kui palju.

.. code-block:: java

    class Demo {
          public Demo(int num, String str) {
               System.out.println("This is a parameterized constructor");
          }
    }



*Konstruktorite roll objektide loomises* 
-----------------------------------------

Konstruktor võimaldab anda klassi väljadele algväärtusi, kui objekt luuakse. Ütleme, et meil on klass *Actor*, millel on väljad *fistName* ja *lastName*. 

.. code-block:: java

    public class Actor {
        String firstName;
        String lastName;

        public String getFirstName() {
            return firstName;
        }

        public void setFirstName(String firstName) {
            this.firstName = firstName;
        }

        public String getLastName() {
            return lastName;
        }

        public void setLastName(String lastName) {
            this.lastName = lastName;
        }
    }

Kui tahame luua uue objekti, siis saame seda teha nii:

.. code-block:: java

       public static void main(String args[]) {
           Actor actor = new Actor();
           actor.setFirstName("Arnold");
           actor.setLastName("Schwarzenegger");
       }

Eelnevas koodis *new Actor()* kutsub välja Actor klassi konstruktori. Kuna me seda eraldi defineerinud ei ole, siis kasutatakse *default* konstruktorit. Sellisel kujul on objekte tüütu luua. Kuna arvatavasti igal objektil on eesnimi ja perenimi, loome mugavama konstruktori (*getter* ja *setter* meetodid on koodist välja jäätud).

.. code-block:: java

    public class Actor {
   
        public Actor(String first, String last) {
            this.firstName = first;
            this.lastName = last;
        }
        
        // getters and setters follow
        // ...
    }

Nüüd loome antud klassi jaoks objekti.
    
.. code-block:: java

       public static void main(String args[]) {
           Actor arnold = new Actor("Arnold", " Schwarzenegger");
       }


Seega on loodud uus klassi Actor objekt, mille viiteks on *arnold*, ning mille väljad *firstName = "Arnold"*, *lastName = "Schwarzenegger"*.

Tuleb tähele panna, et kui klassile kirjeldatakse ära konstruktor, siis *default* konstruktor enam ei tööta. Ehk siis antud juhul me ei saa enam luua *Actor* objekti ilma argumentideta. Kui see vajadus on olemas, tuleb selline konstruktor eraldi kirjeldada (*public Actor() {}*).


*Konstruktorite ülelaadimine* 
-----------------------------

Ühel klassil võib olla mitu konstruktorit, juhul kui igal konstruktoril on unikaalne signatuur. Tekitame uue konstruktori klassi *Actor*

.. code-block:: java

   public class Actor {
        String firstName;
        String lastName;
        boolean goodActor = true;

        public Actor(String first, String last, boolean good) {
            firstName = first;
            lastName = last;
            goodActor = good;
        }
        
        public Actor(String first, String last) {
            this.firstName = first;
            this.lastName = last;
        }
        
        // getters and setters follow
        // ...
   }

Ning loome vastava objekti
    
.. code-block:: java

        public static void main(String args[]) {
            Actor a = new Actor("Arnold", "Schwarzenegger", false);
        }

Töötab ka konstruktor kahe argumendiga (ees- ja perenimi). Sellisel juhul *goodActor* muutuja väärtust ei muudeta ja see jääb loodud objektil väärtusega *true*.


Veel üks näide 
-----------------------------

Mis on antud koodi väljundiks?

.. code-block:: java

        class ExampleTwo {
            private int var;
            
            public ExampleTwo() {
                //code for constructor without parameters!
                var = 10;
            }
            
            public ExampleTwo(int num) {
                //code for parameterized one
                var = num;
            }
            
            public int getValue() {
                return var;
            }
            
            public static void main(String args[]) {
                ExampleTwo obj2 = new ExampleTwo();
                System.out.println("var is: " + obj2.getValue());
            }
        } 

Konsooli väljundiks on:

.. code-block:: java

        var is: 10

Aga nüüd kasutame main-meetodis hoopis sellist koodi:

.. code-block:: java

         ExampleTwo obj2 = new ExampleTwo(77);
         System.out.println("var is: " + obj2.getValue());

Konsooli väljundiks on nüüd:

.. code-block:: java

        var is: 77


Teisel juhul andsime me konstruktorisse parameetri 77 ning seetõttu käima läks just argumendiga konstruktor. 

*this. kasutamine väljal* 
-----------------------------

Kõige tihedamini kasutatakse *this* võtmesõna, kuna väli on varjatud meetodi või konstruktori argumendi poolt. 

.. code-block:: java

      public class Student {
          public int code = 0;
          public int age = 0;
            
          //constructor
          public Student(int a, int b) {
              code = a;
              age = b;
          }
      }

Samas võib seda koodi kirjutada nii

.. code-block:: java

    public class Student {
        public int code = 0;
        public int age = 0;
            
        //constructor
        public Student(int code, int age) {
            this.code = code;
            this.age = age;
        }
    }

Nüüd seatakse objekti väljade *code* ja *name* väärtuseks konstruktorisse antud argumentide väärtused.
