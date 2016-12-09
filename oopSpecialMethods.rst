=================
Erilised meetodid
=================

Kõik objektid pärivad automaatselt **Object** klassilt hulga meetodeid, mida võib soovi korral kasutada või üle kirjutada (*override*). Object klassist otse pärituna need meetodid midagi huvitavat ei tee, kuid paljudel klassidel nagu HashMap ja ArrayList on sobivad implementatsioonid olemas. Enda klasside jaoks tuleb need ise kirjutada.

Implementatsiooni näidetes kasutame klassi **Point**, mille täielik kood on leitav peatükis *Objekt muutujana*.

toString
========

**toString** meetod tagastab sõne, mis peaks võimalikult efektiivselt esitama olulist informatsiooni objekti kohta. Printimisel kutsutakse see meetod välja automaatselt.

.. code-block:: java

    ArrayList<String> names = new ArrayList<>();
    names.add("John");
    names.add("Jane");

    System.out.println(names);                           // toString() kutsutakse välja automaatselt

    HashMap<String,Integer> grades = new HashMap<>();
    grades.put("John", 5);
    grades.put("Jane", 3);

    String gradesString = "Grades:" + grades.toString(); // võime ka ise välja kutsuda, kui vaja
    System.out.println(gradesString);

Implementeerimine
-----------------

Kui me loome ise mõne klassi ning ei kirjuta üle **toString** meetodit, pole tulemus printimisel kuigi informatiivne. Võtame näiteks klassi **Point**, mis sisaldab x- ja y-koordinaati täisarvudena, ning proovime seda välja trükkida.

.. code-block:: java

    Point p = new Point(5, 9);
    System.out.println(p);

Konsooli trükitakse selle tulemusena midagi taolist::

    examples.Point@2a139a55

Tegemist on sõnega, mis koosneb klassi nimest, @-märgist ning objekti hashCode (vt allpool) väärtusest kuueteistkümnendarvuna. Nagu näha, ei ole sellest informatsioonist palju kasu, ning võiksime kirjutada sobivama **toString** meetodi.

.. code-block:: java

    @Override
    public String toString() {
        return "Point(" + x + ", " + y + ')';
    }

Antud koodi lisamisel **Point** klassi on tulemus järgmine::

    Point(5, 9)

equals ja hashCode
==================

**equals** ja **hashCode** on kaks meetodit, mis on omavahel tihedalt seotud, ning seetõttu räägitakse neist tihti koos. **equals** meetodit kasutatakse kahe objekti sisuliseks võrdlemiseks ning **hashCode** arvutab objekti andmete põhjal räsiväärtuse, mida kasutatakse näiteks HashSetis või HashMapis objektide paigutamiseks ja kiireks leidmiseks.

**NB!** Võrdne HashCode ei tähenda, et objektid on võrdsed. Seega ei saa HashCode'i kasutada unikaalse võtmena.

Järgnevas näites eeldame, et meie klassis Point on juba kirjeldatud korrektne **equals** ja **hashCode** paar. Allpool näeme ka seda, kuidas neid meetodeid luua saab.

.. code-block:: java

    Point p1 = new Point(1, 0);
    Point p2 = new Point(0, 0);
    Point p3 = new Point(0, 0);

    System.out.println(p1 == p2);      // false
    System.out.println(p1.equals(p2)); // false
    System.out.println(p2.equals(p3)); // true

Implementeerimine
-----------------

Meetodid tuleks realiseerida järgmistel põhimõtetel:

- võrdsetel objektidel peavad olema ühe protsessi piires võrdsed räsiväärtused
- realiseerida tuleb mõlemad meetodid korraga, kuna vastasel juhul pole eelmine punkt tagatud ning objekti käitumine teatud andmestruktuurides on vigane
- räsiväärtuse arvutamisel tuleb võtta arvesse kõiki välju, mida kasutatakse **equals** meetodis võrdumise kontrollimiseks.

Levinumates IDE-des on olemas võimalus neid meetodeid automaatselt genereerida. IntelliJ's saab seda teha nii:

 1. Vali menüüst **Code** -> **Generate** -> **equals() and hashCode()** või vajuta Alt+Insert
 2. Vali sobiv mall, näiteks IntelliJ Default
 3. Vali väljad, mida tuleks arvutamisel kasutada.

Üks rida tuleks meie näite puhul välja kommenteerida, kuna see töötab ainult klasside puhul, mis laiendavad mõnda muud klassi. Vastasel juhul on ülemklassiks Object, mille equals meetod kontrollib, kas tegu on täpselt sama objektiga, ning tulemus on vale:

.. code-block:: java

    if (!super.equals(object)) return false;

Tulemus on selline:

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
        int result = super.hashCode();
        result = 31 * result + x;
        result = 31 * result + y;
        return result;
    }

Kui soovite hiljem näiteks **equals** meetodit muuta, tuleks sellega koos genereerida ka uus **hashCode**.

clone
=====

Meetod **clone** loob objektist koopia ning tagastab selle. Koopia põhjalikkus oleneb clone meetodi realisatsioonist (*deep copy* vs *shallow copy*). *Deep copy* puhul luuakse koopia ka kõigi objektis sisalduvate muutujate sisust, *shallow copy* muutujad jäävad aga viitama samale objektile.

Võtame näiteks ArrayListi, mille puhul tehakse **clone** meetodis *shallow copy*. Elementidena kasutame **Point** objekte.

.. code-block:: java

    Point p1 = new Point(0, 0);
        Point p2 = new Point(3, 8);

        ArrayList<Point> pointList = new ArrayList<>();

        pointList.add(p1);
        pointList.add(p2);

        ArrayList<Point> pointListClone;
        pointListClone = (ArrayList) pointList.clone(); // tuleb cast'ida, kuna clone tagastustüübiks on Object

        System.out.println(pointList);                  // Eeldame, et toString meetod on eelnevalt realiseeritud
        System.out.println(pointListClone);
        System.out.println();

        Point p3 = new Point(2, 6);
        pointListClone.add(p3);

        System.out.println(pointList);                  // Kahe listi sisud on erinevad
        System.out.println(pointListClone);
        System.out.println();

        Point p = pointList.get(0);                     // Valime mingi punkti esimesest listist
        p.setX(9);                                      // Muudame selle sisu

        System.out.println(pointList);                  // Muutus toimub mõlema listi punktides - shallow copy!
        System.out.println(pointListClone);

Implementeerimine
-----------------

Selleks, et **clone** meetodit kasutada, peab klass implementeerima liidest **Cloneable**. Vastasel juhul viskab meetod *CloneNotSupportedExceptioni*. *Deep copy* realiseerimisel tuleb jälgida, et kõik kloonitavad objektid seda liidest implementeeriksid.

Loome näite tarbeks klassi Line, kus hoitakse alg- ja lõpp-punkti koordinaate Point objektidena.

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

Alustuseks loome vajaliku meetodi ja lisame märke liidese Cloneable kohta. Kuna me tahame seekord teha *deep copy*, peame kloonima eraldi ka mõlemad punktid.

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

Kuna punktide sisuks on primitiivsed andmetüübid, võime **Point** klassi hetkel muutmata jätta. Kui me siiski realiseeriksime **clone** meetodi ka seal, võiksime kirjutada nii:

.. code-block:: java

    @Override
    public Object clone() throws CloneNotSupportedException {
        Point startClone = startPoint.clone();
        Point endClone = endPoint.clone();
        Line clonedLine = new Line(startClone, endClone);
        return clonedLine;
    }

Erinevalt eelnevalt demonstreeritud ArrayListist, võime julgelt muuta esialgse joone punktide koordinaate nii, et kloonitud joone punktid jäävad samaks. See ongi *deep copy* põhimõte.