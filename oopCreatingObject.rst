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

        //Tüüp ja nimi
        type name;
        
        //Näiteks
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

 .. code-block:: Java

    Puppy's name is: Tommy
    
 
 
 
*Ülevaade mälus toimuvast objektide loomisel* 
-----------------------------------------------------

.. code-block:: Java

        Student std, std1,       // Deklareerime 4 muutujat
          std2, std3;            // Student tüüpi.

        std = new Student();     // Loome uue objeki, mis kuulub
                                 // Student klassile ning viitame
                                 // sellele objektile muutuja "std" abil.

        std1 = new Student();    // Loome teise Student objekti
                                 // ning viitame sellele objektile
                                 // muutja "std1" abil.

        std2 = std1;             // Kopeerime "std1" viite vääruse
                                 // "std2" vääruseks.

        std3 = null;             // "std3" viiteks seame tühja väärtuse.
 
                  
        std.name = "John Smith";  // Deklareerime mõned välja väärtused.
        std1.name = "Mary Jones";
        
Arvuti mälus tomuvat vastavalt näitele illustreerib allolev pilt. Siin on näha, et kaks muutujat viitavad samale objektile.    

.. image:: http://math.hws.edu/javanotes/c5/objects-in-heap.png


