Objekti loomine
================================================
-----------------------------------------------------------------------------------------
*Objektide loomiseks kasutatakse võtmesõna "new"*
-----------------------------------------------------------------------------------------
Klassi võib kujutada ette, kui üldist juhist, mille järgi objekte luuakse. Javas kasutatakse objektide loomiseks võtmesõna **new**.

.. code-block:: java

        Student student1 = new Student(160000, "Markus");
        Car car1 = new Car("red", 100, 200);
        Dog bob = new Dog();

Esimeses näites luuakse objekt klassist *Student*, teises näites klassist *Car* ja kolmandas klassist *Dog*.
Iga ülaltoodud lause koosneb kolmest osast:

    1. Deklareerimine - Kirjeldatakse objekt selle tüübi järgi ning vabalt valitud muutuja nime järgi.
          
    2. Instantsi loomine - Kasutatakse **new** võtmesõna, et luua objekt.
    
    3. Initsialiseerimine - Pärast **new** võtmesõna kutsutakse välja konstruktor, kuhu antakse soovi korral parameetrid.


*Deklareerimine* 
-----------------------

Tavaliselt oleme harjunud looma muutujat nii:

.. code-block:: java

        type name;

Kui tegemist on primitiivse tüübiga, näiteks *int*, siis koos deklareerimisega reserveeritakse muutujale kindel hulk mälu.

.. code-block:: java

        Student student1;

Siin on tegemist lihtsalt viite loomisega, objekti veel ei looda, kuna objekti loomine käib **new** operaatori abil. Kui proovida kasutada muutuja nime *student1* programmis, siis kood ei kompileeru, sest mällu ei ole objekt veel loodud.

*Instantsi loomine* 
-----------------------

**new** operaatori abil luuakse objekt ning antakse äsjaloodud objektile koha mälus.

**N.B!** Instantsi loomine on sama asi, mis objekti loomine. Kui luuakse objekt, siis on see sama, kui klassi instantsi loomine.

**new** operaator tagastab viite objektile, mida ta on loonud. 


.. code-block:: java

        Point originOne = new Point(23, 94);

*Initsialiseerimine* 
-----------------------

Pärast **new** võtmesõna kutsutakse välja konstruktor, kuhu antakse soovi korral parameetrid. See tuleb välja järgmises näites

 .. code-block:: java

    public class Puppy {
       public Puppy(String name) {
          // This constructor has one parameter, name.
          System.out.println("Passed Name is :" + name );
       }
    
       public static void main(String []args) {
          // Following statement would create an object myPuppy
          Puppy myPuppy = new Puppy( "tommy" );
       }
    }

Antud näites me tekitame klassi *Puppy*, mis saab konstruktorisse kaasa argumendi, mis on antud juhul *String name*. Nüüd objekti loomisel *public static void main(String []args)* plokis deklareerime, et loodud objekt on klassist *Puppy*, mille nimeks valime *myPuppy*. 
Seejärel kasutades **new** võtmesõna loome objekti, mille konstruktor saab sisse parameetri *"tommy"*, mis on parajasti koera nimi. Nüüd objekti loomisel käivitub ka konstruktor, mis automaatselt käivitab konstruktori kehas olevat koodijuppi *System.out.println("Passed Name is :" + name );*. Seepärast konsooli ilmub.

 .. code-block:: Java

    Passed Name is :tommy
