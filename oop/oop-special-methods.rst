=================
Erilised meetodid
=================

Kõik objektid pärivad automaatselt **Object** klassilt hulga meetodeid, mida võib soovi korral kasutada või üle kirjutada (*override*). **Object** klassist otse pärituna need meetodid midagi huvitavat ei tee, kuid paljudel klassidel nagu HashMap ja ArrayList on sobivad implementatsioonid olemas. Enda klasside jaoks tuleb need ise kirjutada.

Implementatsiooni näidetes kasutame klassi **Point**, mille täielik kood on leitav peatükis *Objekt muutujana*.

toString
========

**toString** meetod tagastab sõne, mis peaks võimalikult efektiivselt esitama olulist informatsiooni objekti kohta. Printimisel kutsutakse see meetod välja automaatselt.

.. code-block:: java

    ArrayList<String> names = new ArrayList<>();
    names.add("John");
    names.add("Jane");

    System.out.println(names);                           // toString() is called automatically...

    HashMap<String,Integer> grades = new HashMap<>();
    grades.put("John", 5);
    grades.put("Jane", 3);

    String gradesString = "Grades:" + grades.toString(); // ..but if we wish, we can call it ourselves too
    System.out.println(gradesString);

Implementeerimine
-----------------

Kui me loome ise mõne klassi ning ei kirjuta üle toString meetodit, pole tulemus printimisel kuigi informatiivne.

.. code-block:: java

    Point p = new Point(5, 9);
    System.out.println(p);

Konsooli trükitakse selle tulemusena midagi taolist:

    examples.Point@2a139a55

Tegemist on sõnega, mis koosneb klassi nimest, @-märgist ning objekti hashCode (vt allpool) väärtusest kuueteistkümnendarvuna. Nagu näha, ei ole sellest informatsioonist palju kasu, ning võiksime kirjutada sobivama toString meetodi.

.. code-block:: java

    @Override
    public String toString() {
        return "Point(" + x + ", " + y + ')';
    }

Antud koodi lisamisel Point klassi on tulemus järgmine::

    Point(5, 9)
    
**Lisalugemist:** Joshua Bloch's Effective Java 2nd edition Item 10 (chapter 3)

equals ja hashCode
==================

**equals** ja **hashCode** on kaks meetodit, mis on omavahel tihedalt seotud, ning seetõttu räägitakse neist tihti koos. **equals** meetodit kasutatakse kahe objekti sisuliseks võrdlemiseks ning **hashCode** arvutab objekti andmete põhjal räsiväärtuse, mida kasutatakse näiteks HashSetis või HashMapis objektide paigutamiseks ja kiireks leidmiseks.

**NB!** Võrdne räsiväärtus ei tähenda, et objektid on võrdsed. Seega ei saa seda kasutada unikaalse võtmena.

Järgnevas näites eeldame, et Point klassis on juba kirjeldatud korrektne equals ja hashCode paar.

.. code-block:: java

    Point p1 = new Point(1, 0);
    Point p2 = new Point(0, 0);
    Point p3 = new Point(0, 0);

    System.out.println(p1 == p2);      // false
    System.out.println(p1.equals(p2)); // false
    System.out.println(p2.equals(p3)); // true

Implementeerimine
-----------------

Meetodid tuleks realiseerida, järgides teatud põhimõtteid.

- võrdsetel objektidel peavad olema ühe protsessi piires võrdsed räsiväärtused
- realiseerida tuleb mõlemad meetodid korraga, kuna vastasel juhul pole eelmine punkt tagatud ning objekti käitumine teatud andmestruktuurides on vigane
- räsiväärtuse arvutamisel tuleb võtta arvesse kõiki välju, mida kasutatakse **equals** meetodis võrdumise kontrollimiseks.

Levinumates IDE-des on olemas võimalus neid meetodeid automaatselt genereerida. IntelliJ's saab seda teha nii:

1. Vali menüüst **Code** -> **Generate** -> **equals() and hashCode()** või vajuta Alt+Insert
2. Vali sobiv mall, näiteks IntelliJ Default
3. Vali väljad, mida tuleks arvutamisel kasutada.

Üks rida tuleks meie näite puhul välja kommenteerida. See rida on mõeldud klassidele, mis laiendavad mõnda muud klassi. Antud juhul on ülemklassiks Object, mille equals meetod kontrollib, kas tegu on täpselt sama objektiga, ning seetõttu saaksime selle rea kasutamisel vale tulemuse.

Samuti tuleks hashCode'is samal põhjusel esimene rida ära muuta: super.hashCode() tuleks asendada mingi täisarvulise väärtusega. Esialgne arv ei tohi kindlasti olla 0, kuid muud täisarvud sobivad. Valime näiteks arvu 17.

.. code-block:: java

    if (!super.equals(object)) return false; // should comment out
    
    // ...
    
    int result = super.hashCode();          // should replace

Tulemus:

.. code-block:: java

    public boolean equals(Object object) {
            if (this == object) return true;
            if (object == null || getClass() != object.getClass()) return false;
            // if (!super.equals(object)) return false;

            Point point = (Point) object;

            if (x != point.x) return false;
            if (y != point.y) return false;

            return true;
        }

    public int hashCode() {
        int result = 17;
        result = 31 * result + x;
        result = 31 * result + y;
        return result;
    }

Kui soovite hiljem näiteks equals meetodit muuta, tuleks sellega koos luua ka uus hashCode.

Kuid mis siis ikkagi juhtub, kui jätame näiteks hashCode'i implementeerimata? Oletame, et tegime valmis ainult equals meetodi ning proovime kasutada oma klassi võtmena HashMapis.

.. code-block:: java

    HashMap<Point, Integer> pointNumbers = new HashMap<>();
    
    Point point1 = new Point(0, 9);
    Point point2 = new Point(0, 9);
    Point point3 = new Point(9, 0);
    
    pointNumbers.put(point1, 1);
    
    System.out.println(pointNumbers.get(point1));
    System.out.println(pointNumbers.get(point2));
    System.out.println(pointNumbers.get(point3));
    
Tulemus, kui implementeeritud on ainult equals::

    1
    null
    null
    
Kuigi equals meetodi põhjal on point1 ja point2 võrdsed, ei kohelda neid HashMapis võrdsetena ning võtmena saab kasutada ainult täpselt sama objekti, mlle väärtuse lisamisel võtmeks määrasime.

Tulemus, kui implementeeritud on equals ja hashCode::

    1
    1
    null
    
Selline näeb välja korrektne tulemus. Kuna point1 ja point2 on võrdsed, saab neid mõlemaid kasutada HashMapi poole pöördumisel. Kolmas rida peabki olema null, kuna point3 erineb teisest kahest ning sellise võtmega väärtust me HashMap'i lisanud ei ole.

**Lisalugemist:** Joshua Bloch's Effective Java 2nd edition Item 8, Item 9 (chapter 3)

clone
=====

Meetod **clone** loob objektist koopia ning tagastab selle. Koopia põhjalikkus oleneb clone meetodi realisatsioonist (*deep copy* vs *shallow copy*). *Deep copy* puhul luuakse koopia ka kõigi objektis sisalduvate muutujate sisust, *shallow copy* muutujad jäävad aga viitama samale objektile.

Võtame näiteks **ArrayList** objekti, mille puhul tehakse clone meetodis *shallow copy*. Elementidena kasutame **Point** objekte.

.. code-block:: java

    Point p1 = new Point(0, 0);
    Point p2 = new Point(3, 8);

    ArrayList<Point> pointList = new ArrayList<>();

    pointList.add(p1);
    pointList.add(p2);

    ArrayList<Point> pointListClone;
    pointListClone = (ArrayList) pointList.clone(); // Must cast to ArrayList because return type of clone is Object

    System.out.println(pointList);                  // Asssuming the toString method has already been overridden
    System.out.println(pointListClone);
    System.out.println();

    Point p3 = new Point(2, 6);
    pointListClone.add(p3);

    System.out.println(pointList);                  // The contents are different now!
    System.out.println(pointListClone);
    System.out.println();

    Point p = pointList.get(0);                     // Choose a point from the original list
    p.setX(9);                                      // Change its coordinate

    System.out.println(pointList);                  // The change happened in both lists - shallow copy!
    System.out.println(pointListClone);

Implementeerimine
-----------------

Selleks, et clone meetodit kasutada, peab klass implementeerima liidest **Cloneable**. Vastasel juhul viskab meetod erindi **CloneNotSupportedException**. *Deep copy* realiseerimisel tuleb jälgida, et kõik kloonitavad objektid seda liidest implementeeriksid.

Loome näiteks klassi Line, kus hoitakse alg- ja lõpppunkti koordinaate Point objektidena.

.. code-block:: java

    class Line {
        Point startPoint;
        Point endPoint;

        public Line(Point start, Point end) {
            startPoint = start;
            endPoint = end;
        }

        @Override
        public String toString() {
            return "Line: " + "startPoint=" + startPoint + "; endPoint=" + endPoint;
        }
    }

Loome vajaliku meetodi ja lisame märke liidese Cloneable kohta. Kuna me tahame seekord teha *deep copy*, peame kloonima eraldi ka mõlemad punktid.

.. code-block:: java

    class Line implements Cloneable{
        //...

        @Override
        public Object clone() throws CloneNotSupportedException {
            Point startClone = new Point(startPoint.getX(), startPoint.getY());
            Point endClone = new Point(endPoint.getX(), endPoint.getY());
            Line clonedLine = new Line(startClone, endClone);
            return clonedLine;
        }
    }

Kuna punktide sisuks on primitiivsed andmetüübid, võime Point klassi hetkel muutmata jätta. Kui me siiski realiseeriksime clone meetodi ka seal, võiksime kirjutada nii:

.. code-block:: java

    @Override
    public Object clone() throws CloneNotSupportedException {
        Point startClone = startPoint.clone();
        Point endClone = endPoint.clone();
        Line clonedLine = new Line(startClone, endClone);
        return clonedLine;
    }

Erinevalt eelnevalt demonstreeritud ArrayListist, võime julgelt muuta esialgse joone punktide koordinaate nii, et kloonitud joone punktid jäävad samaks. See ongi *deep copy* põhimõte.
