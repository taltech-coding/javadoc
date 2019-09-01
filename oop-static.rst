Staatilised meetodid, muutujad ja konstandid
=============================================

Esmalt on vaja aru saada, mida üldse sõna staatiline tähendab. Inglise keeles on selle kohta öeldud nii: "Static keyword means that a variable or a method is shared between all instances of that class as it belongs to the type, not the objects". Ehk eesti keeles võiks seda tõlgendada nii, et staatiline muutuja või meetod on jagatud kõikide klassi poolt loodud objektide vahel. Antud meetod või muutuja kuulub tüübile (klassile), mitte objektidele.

Staatilised meetodid
----------------------

- Kuuluvad klassile, mitte objektile (isendile).
- Saab ligi ainult staatilistele andmetele. Ei saa ligi mitte-staatilistele andmetele.
- Saavad kutsuda välja ainult staatilisi meetodeid.
- Staatilistele meetoditele saab ligi otse läbi klassi nime.

.. code-block:: java

    //Syntax
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

Staatilise meetodi seest teise staatilise meetodi väljakutsmisel pole vaja kassinime kirjutada, seepärast *main* meetodi esimene rida *display()* kutsub välja sama klassi staatilise meetodi *display()*. Samaväärne oleks kirjutada *Difference.display()*.

Staatilised väljad
-------------------

Kui väli on deklareeritud kui staatiline, siis kuulub ta klassile. Kõik selle klassi poolt loodud isendid saavad kasutada ühte ja sama staatilist välja. Ligi saab otse klassist, ei ole vaja luua uut objekti.

- Kuuluvad klassile, mitte objekite (isendile).
- Selliseid välju initsialiseeritakse ainult ühel korral, programmi käivitamisel. Need väljad initsialiseeritakse esimesena.
- Sama koopia on kõikide isendite (loodud objektide) käes.
- Staatilistele meetoditele saab ligi otse läbi klassi nime.

.. code-block:: java

    //Syntax
    static int y = 0;
    //Accessing
    <class-name>.<variable-name>
    //Example
    ExampleClass.y
    
Järgnev näide illustreerib seda, kuidas staatilist välja kasutades saab kokku lugeda, mitu objekti oleme loonud.

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
 
 
Nüüd, kui tahame olla ikka kindlad selles koodis, tekitame uue klassi, kus on *Main()* meetod.


.. code-block:: java

 public class Main {

  public static void main(String[] args){
    
    Stuff testingObjectCreationCount1 = new Stuff();
    Stuff testingObjectCreationCount2 = new Stuff();
    Stuff testingObjectCreationCount3 = new Stuff();
  }
 }


Konsooli ilmub:


.. code-block:: java

 Created object number: 1
 Created object number: 2
 Created object number: 3



   


Meeldetuletus mitte-staatilistest väljadest
--------------------------------------------

Mitte-staatilised väljad kuuluvad klassi isenditele. Igal isendil (*instance*) on oma koopia sellest väljast.

Näide staatiliste ja mitte-staatiliste väljade kättesaamisest
-------------------------------------------------------------

.. code-block:: java

    public class Example {

    public static boolean staticField;
    public boolean instanceField;

    public static void main(String[] args) {

        // Static method can access static field directly.
        staticField = true;
        // Is same thing as above.
        Example.staticField = true;

        //Static method can access non-static method by object reference.
        Example instance = new Example();
        instance.instanceField = true;
    }
    
Konstandid ja Magic number
--------------------------

Tihti kasutatakse *static*'ut, et luua konstantne väli, mis on seotud klassiga. Selleks, et muuta staatiline väli konstandiks, peab lisama võtmesõna *final*. Konstante kirjutatakse java konventsioonis läbiva suurtähega.

.. code-block:: java
 
   public class Stuff {
   
     public final static String NAME = "I'm a static variable";
   }
   
   public class Application {
   
     public static void main(String[] args) {
        System.out.println(Stuff.NAME);
     }
   }
   
   
Samuti puutute kokku sellise mõistega nagu magic number. Magic number on numbrite otsene kasutamine koodis. Näiteks:
 
.. code-block:: java

 public class Foo {
    public void setPassword(String password) {
         // don't do this
         if (password.length() > 7) {
              throw new InvalidArgumentException("password");
         }
    }
 }
 
Sellist koodi oleks tarvis refaktoreerida:

.. code-block:: java

 public class Foo {
    public static final int MAX_PASSWORD_SIZE = 7;

    public void setPassword(String password) {
         if (password.length() > MAX_PASSWORD_SIZE) {
              throw new InvalidArgumentException("password");
         }
    }
 }
 
Sellisel juhul on palju lihtsam aru saada, mis koodis toimub ning sellist koodi on lihtsam hallata, juhul, kui numbrilisi väärtusi tekib üha rohkem. Samuti on hiljem lihtsam koodi muuta, kui vaja on, kuna piisab numbri vahetamisest ainult *public static final int MAX_PASSWORD_SIZE = 7;* väljal.
 
 
   
   




