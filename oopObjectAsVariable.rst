===============
Objekt muutujas
===============

Lisaks primitiivsetele andmetüüpidele võime muutuja tüübiks määrata ka mõne klassi. Sel juhul saab muutuja väärtuseks anda selle klassi instantse ehk objekte.

Kasutame näites enda loodud lihtsat klassi **Point**, millel on täisarvudena esitatavad koordinaadid x ja y ning vastavad get ja set meetodid.

.. code-block:: java

    class Point {
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return x;
        }

        public void setX(int x) {
            this.x = x;
        }

        public int getY() {
            return y;
        }

        public void setY(int y) {
            this.y = y;
        }
    }

Kui me anname muutujale väärtuseks objekti, hakkab muutuja sellele objektile viitama. Samale objektile võib viidata üheaegselt mitu muutujat – tegu on ikkagi üheainsa objektiga. Iga edaspidine muudatus selles objektis säilib ning on kättesaadav kõikide muutujate kaudu, mis talle viitavad.

Kirjutame näiteklassi, mille main-meetodis loome kaks **Point** objekti, ja lisame need ArrayList'i. Seejärel loome uue muutuja, mis viitab ühele punktile, ning veendume, et koordinaadid on samad. Lõpuks muudame selle punkti koordinaate ning kontrollime, kas koordinaatide väärtus on igal juhul muutunud.

.. code-block:: java

    import java.util.ArrayList;

    class ObjectVariableExample {
        public static void main(String[] args) {
            Point p1 = new Point(0, 0);
            Point p2 = new Point(3, 8);

            ArrayList<Point> pointList = new ArrayList<>();

            pointList.add(p1);
            pointList.add(p2);

            // Print coordinates
            System.out.println("Coordinates of p1 and p2 before change:");
            for (Point point: pointList) {
                System.out.println("(" + point.getX() + ", " + point.getY() + ")");
            }

            // Create new variable which refers to p1
            Point pp = p1;
            System.out.println("Coordinates of pp, which refers to p1:");
            System.out.println("(" + pp.getX() + ", " + pp.getY() + ")");

            // Change coordinates of p1
            p1.setX(9);
            p1.setY(10);

            // Print again
            System.out.println("Coordinates of p1 and p2 after change:");
            for (Point point: pointList) {
                System.out.println("(" + point.getX() + ", " + point.getY() + ")");
            }

            System.out.println("Coordinates of pp after change:");
            System.out.println("(" + pp.getX() + ", " + pp.getY() + ")");
        }
    }

Koodi käivitamisel näeme, et p1 muutmisel muutusid tõepoolest ka pp koordinaadid ning võime järeldada, et pp viitab p1-le::

    Coordinates of p1 and p2 before change:
    (0, 0)
    (3, 8)
    Coordinates of pp, which refers to p1:
    (0, 0)
    Coordinates of p1 and p2 after change:
    (9, 10)
    (3, 8)
    Coordinates of pp after change:
    (9, 10)

Kui me tahaksime koodi ümber teha nii, et ühe muutuja kaudu objektis tehtud muudatus ei mõjutaks teisi, tuleb meil teha sellest objektist koopia. Selle jaoks on olemas spetsiaalne meetod nimega **clone**, mille kohta saab lähemalt lugeda näiteks eriliste meetodite peatükis siinsamas juhendis.

Objekt argumendina
==================

Nagu teisi muutujaid, saab ka objekte kasutada argumentidena. Tegelikult tegime seda juba eespool, lisades Point objekti **add** meetodi abil ArrayList'i.

Objekti lugemine
----------------

Teeme oma näiteklassi ümber nii, et punkti koordinaatide printimine toimuks eraldi meetodi **printCoordinates** abil, millele anname väljatrükitava punkti argumendina kaasa.

.. code-block:: java

    import java.util.ArrayList;
    
    class ObjectVariableExample {
        public static void main(String[] args) {
            Point p1 = new Point(0, 0);
            Point p2 = new Point(3, 8);

            ArrayList<Point> pointList = new ArrayList<>();

            pointList.add(p1);
            pointList.add(p2);

            // Print coordinates
            System.out.println("Coordinates of p1 and p2 before change:");
            for (Point point: pointList) {
                printCoordinates(point);
            }

            // Create new variable which refers to p1
            Point pp = p1;
            System.out.println("Coordinates of pp, which refers to p1:");
            printCoordinates(pp);

            // Change coordinates of p1
            p1.setX(9);
            p1.setY(10);

            // Print again
            System.out.println("Coordinates of p1 and p2 after change:");
            for (Point point: pointList) {
                printCoordinates(point);
            }

            System.out.println("Coordinates of pp after change:");
            printCoordinates(pp);
        }

        private static void printCoordinates(Point p) {
            System.out.println("(" + p.getX() + ", " + p.getY() + ")");
        }
    }
    
Tulemus on identne eelmisega::

    Coordinates of p1 and p2 before change:
    (0, 0)
    (3, 8)
    Coordinates of pp, which refers to p1:
    (0, 0)
    Coordinates of p1 and p2 after change:
    (9, 10)
    (3, 8)
    Coordinates of pp after change:
    (9, 10)

Kui me ei tea täpselt, kuidas funktsioon töötab, ning eesmärgiks pole objekti sisu muuta, oleks mõistlik objekt enne kloonida. Siis saame klooni argumendina kaasa anda ning objekti algne sisu säilib olenemata funktsiooni sisust.

Objekti muutmine
----------------

Loome veel ühe meetodi, mille ülesanne on suurendada punkti koordinaate ühe võrra.

.. code-block:: java

    private static void increaseCoordinates(Point p) {
        p.setX(p.getX() + 1);
        p.setY(p.getY() + 1);
    }
    
Muudame eelmist näidet nii, et uute koordinaatide määramise asemel suurendame p1 koordinaate ühe võrra. 

.. code-block:: java

    public static void main(String[] args) {
        Point p1 = new Point(0, 0);
        Point p2 = new Point(3, 8);

        ArrayList<Point> pointList = new ArrayList<>();

        pointList.add(p1);
        pointList.add(p2);

        // Print coordinates
        System.out.println("Coordinates of p1 and p2 before change:");
        for (Point point: pointList) {
            printCoordinates(point);
        }

        // Create new variable which refers to p1
        Point pp = p1;
        System.out.println("Coordinates of pp, which refers to p1:");
        printCoordinates(pp);

        // Increase coordinates of p1 by 1
        increaseCoordinates(p1);

        // Print again
        System.out.println("Coordinates of p1 and p2 after change:");
        for (Point point: pointList) {
            printCoordinates(point);
        }

        System.out.println("Coordinates of pp after change:");
        printCoordinates(pp);
    }
    
Kui algselt olid p1 koordinaadid (0, 0), siis nüüd on koordinaatideks (1, 1)::

    Coordinates of p1 and p2 before change:
    (0, 0)
    (3, 8)
    Coordinates of pp, which refers to p1:
    (0, 0)
    Coordinates of p1 and p2 after change:
    (1, 1)
    (3, 8)
    Coordinates of pp after change:
    (1, 1)


Taaskord tuleb meeles pidada, et kaasa ei anta mitte koopiat objektist, vaid viide. See tähendab, et kui funktsiooni sees meie objekti kuidagi muudetakse, siis need muudatused on püsivad.
