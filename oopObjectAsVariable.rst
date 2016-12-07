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

Kirjutame näiteklassi, mille main-meetodis loome kaks **Point** objekti ja lisame need ArrayList'i. Seejärel loome uue muutuja, mis viitab ühele punktile ning veendume, et koordinaadid on samad. Lõpuks muudame selle punkti koordinaate ning kontrollime, kas koordinaatide väärtus on igal juhul muutunud.

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
            System.out.println("Coordinates before change:");
            for (Point point: pointList) {
                System.out.println(point.getX() + ", " + point.getY());
            }

            // Create new variable which refers to p1
            Point pp = p1;
            System.out.println("Coordinates of pp, which refers to p1:");
            System.out.println(pp.getX() + ", " + pp.getY());

            // Change coordinates of p1
            p1.setX(9);
            p2.setY(10);

            // Print again
            System.out.println("Coordinates after change:");
            for (Point point: pointList) {
                System.out.println(point.getX() + ", " + point.getY());
            }

            System.out.println("Coordinates of pp, which refers to p1:");
            System.out.println(pp.getX() + ", " + pp.getY());

            System.out.println("Coordinates of p1 directly:");
            System.out.println(p1.getX() + ", " + p1.getY());
        }
    }

Koodi käivitamisel näeme, et eelpool kirjeldatud käitumine vastab tõele.

Kui me tahaksime koodi ümber teha nii, et ühe muutuja kaudu objektis tehtud muudatus ei mõjutaks teisi, tuleb meil teha sellest objektist koopia. Selle jaoks on olemas spetsiaalne meetod nimega **clone**, mille kohta saab lähemalt lugeda näiteks eriliste meetodite peatükis siinsamas juhendis.

Objekt argumendina
------------------

Nagu teisi muutujaid, saab ka objekte kasutada argumentidena. Tegelikult tegime seda juba eespool, lisades Point objekti ArrayList'i, kasutades meetodit **add**. Teeme oma näiteklassi ümber nii, et punkti koordinaatide printimine toimuks eraldi meetodi **printCoordinates** abil. Väljundi loetavuse huvideks võiks koordinaadid olla ka sulgudega ümbritsetud, nüüd on meil võimalik seda lihtsasti muuta.

.. code-block:: java

    class ObjectVariableExample {
        public static void main(String[] args) {
            Point p1 = new Point(0, 0);
            Point p2 = new Point(3, 8);

            ArrayList<Point> pointList = new ArrayList<>();

            pointList.add(p1);
            pointList.add(p2);

            // Print coordinates
            System.out.println("Coordinates before change:");
            for (Point point: pointList) {
                printCoordinates(point);
            }

            // Create new variable which refers to p1
            Point pp = p1;
            System.out.println("Coordinates of pp, which refers to p1:");
            printCoordinates(pp);

            // Change coordinates of p1
            p1.setX(9);
            p2.setY(10);

            // Print again
            System.out.println("Coordinates after change:");
            for (Point point: pointList) {
                printCoordinates(point);
            }

            System.out.println("Coordinates of pp, which refers to p1:");
            printCoordinates(pp);

            System.out.println("Coordinates of p1 directly:");
            printCoordinates(p1);
        }

        private static void printCoordinates(Point p) {
            System.out.println("(" + p.getX() + ", " + p.getY() + ")");
        }
    }

Taaskord tuleb meeles pidada, et kaasa ei anta mitte koopiat objektist, vaid viide. See tähendab, et kui funktsiooni sees meie objekti kuidagi muudetakse, siis need muudatused on püsivad.

Kui me ei tea täpselt, kuidas funktsioon töötab, ning eesmärgiks pole objekti sisu muuta, oleks mõistlik eelnevalt objekt kloonida. Siis saame klooni argumendina kaasa anda ning objekti algne sisu säilib olenemata funktsiooni sisust.