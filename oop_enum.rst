*Enum* - konstantide loend
==================================================

*enum* tüüp on eriline andmetüüp, kus saab hoida eeldefineeritud konstante. Seda tüüpi muutuja saab sisaldada vaid ühte väärtust eeldefineeritud loendist.

*enum* kirjeldatakse sarnaselt klassile. See sisaldab konstante, mis kirjutatakse Javas läbivalt suurte tähtedega.

Näiteks kirjeldame ära liikumissuuna (kus diagonaalne liikumine pole lubatud):

.. code-block:: java

    public enum Direction {
        UP, DOWN, LEFT, RIGHT
    }
    
*enum*'i tuleks kasutada juhul, kui on teada lõplik hulk võimalikke väärtusi. Näiteks eelneva liikumise näite puhul ei saa sellise koodi puhul esitada üles-vasakule liikumist.

Kasutamine koodis
-------------------

*enum* väärtusi on võimalik võrrelda kas == võrdluse, :code:`equals()` meetodi või :code:`switch` valikuga. Näiteks:

.. code-block:: java

    public enum DirectionExample {

        public static Direction getDirection() {
            // return something meaningful
            return Direction.UP;
        }
        public static void main() {
            Direction dir = getDirection();
            if (dir == Direction.UP) {
                // move up
            } else if (dir == Direction.DOWN) {
                // move down
            } // etc
        }
    }

Allpool kasutame *switch*'i.

*enum* näide - nädalapäevad
----------------------------

Kirjeldame *enum*'i:

.. code-block:: java

    public enum Weekday {
        MONDAY, TUESDAY, WEDNESDAY, THURSDAY,
        FRIDAY, SATURDAY, SUNDAY
    }

ja kasutame mingis meetodis järgnevat (getWeekday() tagastab näiteks aktiivse nädalapäeva):

.. code-block:: java

        Weekday weekday = getWeekday();
        switch (weekday) {
            case MONDAY:
            case TUESDAY:
            case WEDNESDAY:
            case THURSDAY:
            case FRIDAY:
                System.out.println("work!");
                break;
            case SUNDAY:
            case SATURDAY:
                System.out.println("party!");
                break;
        }
        
Kuna *enum* saab sisaldada vaid piiratud koguse väärtusi, siis eelmise näite võib kirjutada ka selliselt:

.. code-block:: java

        switch (weekday) {
            case SATURDAY:
            case SUNDAY:
                System.out.println("party!");
                break;
            default:
                System.out.println("work!");
                break;
        }
        
        

Lisainformatsioon koos *enum* tüübiga
-------------------------------------

Lisaks konstandi nimele on võimalik igale väärtusele kaasa anda erinevaid lisaväärtusi.

Järgnevas näites loome Weekday *enum*'i teise klassi sees. Sama kood võiks olla eraldi failis Weekday.java.

.. code-block:: java

    public class WeekdayUsageAdvanced {
        enum Weekday {
            MONDAY(true), TUESDAY(true), WEDNESDAY(true), THURSDAY(true),
            FRIDAY(true), SATURDAY(false), SUNDAY(false);

            private final boolean workingDay;

            Weekday(boolean workingDay) {
                this.workingDay = workingDay;
            }

            public boolean isWorkingDay() {
                return workingDay;
            }
        }

        public static Weekday getWeekday() {
            // do something here
            return Weekday.SUNDAY;
        }

        public static void main(String[] args) {
            Weekday weekday = getWeekday();
            if (weekday.isWorkingDay()) {
                System.out.println("work!");
            } else {
                System.out.println("party!");
            }
        }
    }

Nüüd on iga *enum* konstandiga määratud lisaväärtus - kas tegemist on tööpäevaga. MONDAY(true) käivitab konstruktori, kuhu antakse argument true ette. Selle väärtus määratakse workingDay muutujasse. final muutuja tähendab seda, et selle väärtust enam muuta ei saa. Weekday *enum*'il on avalik meetod isWorkingDay(), mis iga nädalapäeva kohta tagastab vastava väärtuse. Laupäev ja pühapäev ei ole tööpäevad, ülejäänud on.


Alternatiiv - kasutada tavalisi konstante
--------------------------------------------

Nädalapäevade esitamiseks võib kasutada näiteks täisarv tüüpi (int) konstante:

.. code-block:: java

    public static final int MONDAY = 1;
    public static final int TUESDAY = 2;
    public static final int WEDNESDAY = 3;
    public static final int THURSDAY = 4;
    public static final int FRIDAY = 5;
    public static final int SATURDAY = 6;
    public static final int SUNDAY = 7;


    public static void getSchedule() {
        int weekday = getWeekday();
        if (weekday < SATURDAY) {
            // working days
        } else {
            // weekend
        }
    }
    
Aga mis juhtub, kui getWeekday() tagastab 8? Sellisel juhul meie kood arvestaks, et tegemist on nädalavahetusega. Sellist väärtust ei tohiks üldse lubada. *enum*'i kasutades sellist probleemi ei teki. Samuti on ühte tüüpi asjad grupeeritud ühe *enum*'i alla. Kui viimases näiteks oleks veel konstandid kuude kohta, siis võivad konstandid segamini minna (antud näites saab nime järgi üheselt aru, millega tegemist, aga mõne muu näite puhul ei pruugi saada). *enum*'i puhul oleks eraldi Weekday ja Month tüübid.

