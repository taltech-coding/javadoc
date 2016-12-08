Staatilised meetodid, muutujad ja konstandid
=============================================

Esmalt on vaja aru saada, mida üldse staatiline tähendab. Inglise keeles on selle kohta öeldud nii: "Static keyword means that variable or method is shared between all instances of that class as it belongs to the type, not objects". Ehk eesti keeles võiks seda tõlgendada nii, et staatiline muutuja või meetod on jagatud kõikide klassi poolt loodud objektide vahel. Antud meetod või muutuja kuulub tüübile, mitte objektile.

Staatilised meetodid
----------------------

- Kuuluvad klassile, mitte objektile (isendile).
- Saab ligi ainult staatilistele andmetele. Ei saa ligi mitte-staatilistele andmetele.
- Saavad kutsuda välja ainult staatilisi meetodeid.
- Staatilistele meetoditele saab ligi otse läbi klassi nime.

 .. code-block:: java

    //Süntaks
    <class-name>.<method.name>

- Staatiline meetod ei saa kasutada *this* ja *super* võtmesõnu.

All on võimalik näha erinevust staatilise ja isendi meetodite väjakutsel.
 
 
.. code-block:: java

 class Difference {
 
  public static void main(String[] args) {
    display();  //calling without object
    Difference t = new Difference();
    t.show();  //calling using object
  }
 
  static void display() {
    System.out.println("Programming is amazing.");
  }
 
  void show(){
    System.out.println("Java is awesome.");
   }
 }

Staatilised väljad
-------------------

Kui väli on deklareeritud, kui staatiline, siis kuulub ta klassile. Kõik selle klassi poolt loodud isendid saavad kasutada ühte ja sama staatilist välja. Ligi saab otse klassist, ei ole vaja luua uut objekti.

- Kuuluvad klassile, mitte objekite (isendile).
- Initsialiseeritakse neid välju üks kord, programmi käivitamisel. Neid välju initsialiseeritakse kõige esimestena.
- Sama koopia on kõikide isendite (loodud objektide) käes.
- Staatilistele meetoditele saab ligi otse läbi klassi nime.

.. code-block:: java

    //Süntaks
    static int y = 0;
    //Kättesaamine
    <class-name>.<variable-name>
    
    
Väikseks näiteks staatilistest väljadest võib tuua tüüpilise probleemi, mida staalilise muutujaga muudetakse. Näiteks, kui me tahame lugeda kokku, mitu objekti oleme loonud.

.. code-block:: java

 public class Stuff {
    
    // Set count to zero initially.
    static int count = 0;
    
    public Stuff() {
        
        // Every time the constructor runs, increment count.
        count = count + 1;
        
        // Display count.
        System.out.println("Created object number: " + count);
    }
 } 
   


Meeldetuletus mitte-staatilistest väljadest
--------------------------------------------

Mitte-staatilised väljad kuuluvad klassi isenditele. Igal isendil (instance) on oma koopia sellest väljast.

Näite staatiliste ja mitte-staatiliste väljade kättesaamisest
-------------------------------------------------------------

 .. code-block:: java

    public class Example {

    public static boolean staticField;
    public boolean instanceField;

    public static void main(String[] args) {

        // Staatiline meetod saab staatilise väja kätte otse.
        staticField = true;

        // Staatiline meetod saab mitte-staatilise välja kätte läbi objekti.
        Example instance = new Example();
        instance.instanceField = true;
    }
    
Konstandid
------------

Tihti esinev põhjus, miks kasutatakse *static*, on konstantse välja loomine, mis on seotud klassiga. Selleks, et muuta staatiline väli konstantseks, peab lihtsalt lisama võtmesõna *final*. Konstante kirjutatakse java konventsioonis läbiva suure tähega.

 .. code-block:: java
 
   public class Stuff {
   
     public final static String NAME = "I'm a static variable";
   }
   
   public class Application {
   
     public static void main(String[] args) {
        System.out.println(Stuff.NAME);
     }
   }
   
   




