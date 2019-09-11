=================
Objektide kogumid
=================

Objektide kogumite deklareerimine
---------------------------------

Kogumi deklareerimisel peab ära määrama, mis klassi objekte seal kogumis hoitakse.

Võtame näiteks klassid Shape, Circle, Rectangle ja Square.

.. code-block:: java

    public class Shape 

.. code-block:: java

    public class Circle extends Shape

.. code-block:: java
    
    public class Rectangle extends Shape 

.. code-block:: java

    public class Square extends Rectangle

Kogumis saab hoida objekte, mis on kas määratud klassi objektid või siis selle määratud klassi alamklassi (või alamklassi alamklassi jne) objektid.

Näiteks kui teha järjend listOfShapes:

.. code-block:: java

    ArrayList<Shape> listOfShapes = new ArrayList<>();

Antud listis saab hoida Shape, Circle, Rectangle või Square tüüpi objekte.

Kui teha järjend listOfRectangles:

.. code-block:: java

    ArrayList<Rectangle> listOfRectangles = new Arraylist<>();

Antud järjendis saab hoida kas Rectangle või Square tüüpi objekte, aga mitte Shape ega Circle.

Kui ei taha järjendile kindlat objektitüüpi määrata, saab selleks määrata lihtsalt Object, kuna kõik teised klassid on Object klassi alamklassid.

.. code-block:: java

    ArrayList<Object> listOfObjects = new ArrayList<>();

Analoogiliselt saab teha ka teisi objektide kogumeid.

Antud klassidel on selline hierarhia:

.. image:: /_images/class_hierarchy.png


Objekti tüübi tuvastamine
-------------------------

Kui hoiad kogumis erinevat tüüpi objekte, võib tekkida vajadus objektide tüüpe tuvastada. Selleks saab kasutada meetodit *getClass* või operaatorit *instanceof*.

*getClass* meetod tagastab antud objekti klassi.

*instanceof* kontrollib, kas objekt on mingit kindla klassi objekt, ja tagastab booleani.

*getClass* näide:

.. code-block:: java

    Rectangle rec = new Rectangle();
    System.out.println(rec.getClass());

Mis prindib konsooli

.. code-block:: java

    class Rectangle

*instanceof* näide:

.. code-block:: java

    Rectangle rec = new Rectangle();
    boolean numInstance1 = rec instanceof Rectangle;
    boolean numInstance2 = rec instanceof Shape;
    boolean numInstance3 = rec instanceof Circle;
    
    System.out.println(numIstance1);
    System.out.println(numIstance2);
    
    if (rec instanceof Rectangle) {
        System.out.println("rec is a rectangle");
    }

Mis prindib konsooli:

.. code-block:: java

    true
    true
    false
    rec is a rectangle
