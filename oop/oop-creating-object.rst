Objekti loomine
================================================
-----------------------------------------------------------------------------------------
*Objektide loomiseks kasutatakse võtmesõna "new"*
-----------------------------------------------------------------------------------------
*NB!* Klassi võib kujutada ette kui üldist juhist, mille järgi objekte luuakse. Javas kasutatakse objektide loomiseks võtmesõna **new**.

.. code-block:: java

        Student student1 = new Student(160000, "Markus");
        Car car1 = new Car("red", 100, 200);
        Dog bob = new Dog();

Esimeses näites luuakse objekt klassist *Student*, teises näites klassist *Car* ja kolmandas klassist *Dog*.
Iga ülaltoodud lause koosneb kolmest osast:

    1. Deklareerimine - Kirjeldatakse objekt selle tüübi järgi ning vabalt valitud muutuja nime järgi.
          
    2. Instantsi loomine - Kasutatakse **new** võtmesõna, et luua objekt.
    
    3. Initsialiseerimine - Pärast **new** võtmesõna kutsutakse välja konstruktor, kuhu antakse soovi korral sobivad parameetrid.


*Deklareerimine* 
-----------------------

Tavaliselt oleme harjunud looma muutujat nii:

.. code-block:: java

        //Type and name
        type name;
        
        //Example
        int randomNumber;

Kui tegemist on primitiivse tüübiga, näiteks *int*, siis koos deklareerimisega reserveeritakse muutujale kindel hulk mälu.
Järgmises näites on näha objekti viida deklareerimist, aga mitte veel objekti loomist!

.. code-block:: java

        Student student1;

Objekti veel ei looda, kuna objekti loomine käib **new** operaatori abil. Kui proovida kasutada muutuja nime *student1* programmis, siis kood ei kompileeru, sest mällu ei ole objekti veel loodud.

*Instantsi loomine* 
-----------------------

**new** operaatori abil luuakse uus objekt ning antakse äsjaloodud objektile koht mälus. **new** operaator tagastab viite objektile, mille ta lõi. 


.. code-block:: java

        Point originOne = new Point(23, 94);
        
Antud näites LUUAKSE objekt võtmesõna **new** abil.

*Initsialiseerimine* 
-----------------------

Pärast võtmesõna **new** kutsutakse välja konstruktor, kuhu antakse soovi korral parameetrid. Seda illustreerib järgnev näide:

.. code-block:: java

    public class Puppy {
       public Puppy(String name) {
          // This constructor has one parameter, name.
          System.out.println("Puppy's name is: " + name);
       }
    
       public static void main(String []args) {
          // Following statement would create an object myPuppy
          Puppy myPuppy = new Puppy("Tommy");
       }
    }

Antud näites me tekitame klassi *Puppy*, mis saab konstruktorisse kaasa argumendi, mis on antud juhul *String name*. Nüüd objekti loomisel *public static void main(String []args)* plokis deklareerime, et loodud objekt on klassist *Puppy*, mille nimeks valime *myPuppy*. 
Seejärel kasutades **new** võtmesõna loome objekti, mille konstruktor saab sisse parameetri *"Tommy"*, mis on parajasti koera nimi. Nüüd objekti loomisel käivitub ka konstruktor, mis automaatselt käivitab konstruktori kehas oleva koodijupi *System.out.println("Passed Name is: " + name );*. Konsooli prinditakse:

.. code-block:: console

    Puppy's name is: Tommy
    
 
 
 
*Ülevaade mälus toimuvast objektide loomisel* 
-----------------------------------------------------

.. code-block:: java

        class Student {

            public String name;  // Student's name.
            public double test1, test2, test3;   // Grades on three tests.

            public double getAverage() {  // compute average test grade
                return (test1 + test2 + test3) / 3;
            }
        }

        public class StudentExample {
            public static void main(String[] args) {
                Student std, std1,       // Declare four variables of
                          std2, std3;    //   type Student.

                std = new Student();     // Create a new object belonging
                                         //   to the class Student, and
                                         //   store a reference to that
                                         //   object in the variable std.

                std1 = new Student();    // Create a second Student object
                                         //   and store a reference to
                                         //   it in the variable std1.

                std2 = std1;             // Copy the reference value in std1
                                         //   into the variable std2.

                std3 = null;             // Store a null reference in the
                                         //   variable std3.

                std.name = "John Smith";  // Set values of some instance variables.
                std1.name = "Mary Jones";

                // (Other instance variables have default
                //    initial values of zero.)
            }
        }
        
Arvuti mälus tomuvat vastavalt näitele illustreerib allolev pilt. Siin on näha, et kaks muutujat viitavad samale objektile.    

.. image:: /_images/creating_object.png

Kui muuta :code:`std1.test1 = 100.0`, siis muutub mälus vastav objekt. Kuna *std2* viitab ka samale objektile, siis :code:`std2.test1` väärtus on ka :code:`100.0`.

Sarnaseks visualiseerimiseks võid kasutada: http://www.pythontutor.com/java.html

Kopeeri ülalolev kood koodiaknasse ja vajuta "Visualize Execution". Järgneval lehel saad liikuda nuppudega edasi-tagasi, et näha, milline on seis mälus (muutujate väärtused, objektide olek).
