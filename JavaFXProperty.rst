================
JavaFX: Property
================

**Property'd**  ehk omadused on erilist tüüpi muutujad, mis võimaldavad registreerida objekti oleku ehk selles sisalduvate andmete muutusi. Samuti saab Property'd teineteisega siduda (*binding*).

Tegelikult oleme juba kaudselt Property'te poole pöördunud, kuna neid kasutatakse kõikides JavaFX kasutajaliideste komponentides. Näiteks on kõikidel komponentidel olemas BooleanProperty **visible**. Meetod **setVisible(false)**, mis muudab komponendi nähtamatuks, seab **visible** Property väärtuseks false ning selle tulemusena joonistatakse pilt ümber nii, et komponent pole nähtav.

On olemas kahte tüüpi Property objekte: tavalised ning *read-only* Property'd, mida saab ainult lugeda ja mitte muuta.

Tavalise Property näited: SimpleBooleanProperty, SimpleDoubleProperty, SimpleStringProperty, SimpleObjectProperty.

Read-only Property näited: ReadOnlyBooleanProperty, ReadOnlyStringProperty, ReadOnlyDoubleProperty, ReadOnlyObjectProperty.

Property kasutamine
===================

Selleks, et hoida koodi lihtsana, ei kasuta me näidetes JavaFX komponente, vaid tavalisi klasse. Eesmärk on mõista, kuidas Property töötab, kuidas mitme komponendi Property'd omavahel siduda ning kuidas tuvastada muutusi nende väärtustes.

Property loomine
----------------

Loome näiteks klassi Exam, mille ainsaks sisuks on DoubleProperty nimega **grade**. Vastavalt kapseldamise põhimõttele loome privaatse Property objekti ning getteri selle küsimiseks. Samuti on vaja getterit ja setterit Property väärtuse jaoks. Kõiki kolme funktsiooni on võimalik IntelliJ's automaatselt genereerida (*Code* -> *Generate* -> *Getter and Setter*).

.. code-block:: java

    class Exam {

        private DoubleProperty grade = new SimpleDoubleProperty();

        public double getGrade() {
            return grade.get();
        }

        public DoubleProperty gradeProperty() {
            return grade;
        }

        public void setGrade(double grade) {
            this.grade.set(grade);
        }
    }

ChangeListener ja muutustele reageerimine
-----------------------------------------

Loome peafunktsiooni, mis trükib konsooli teate iga kord, kui hinne muutub. Selleks kasutame **ChangeListeneri**, kus kirjutame üle abstraktse meetodi **changed**. Vana ja uus väärtus sisalduvad argumentides oldValue ja newValue ning ObservableValue on objekt, mida muudetakse.

.. code-block:: java

    public class Main {
        public static void main(String[] args) {
            Exam javaExam = new Exam();

            javaExam.gradeProperty().addListener(new ChangeListener<Number>() {
                @Override
                public void changed(ObservableValue<? extends Number> observable, Number oldValue, Number newValue) {
                    System.out.println("Grade has changed from " + oldValue + " to " + newValue);
                }
            });

            javaExam.setGrade(2.5);
            javaExam.setGrade(5.0);

        }
    }

Koodi käivitamisel trükitakse välja tekst::

    Grade has changed from 0.0 to 2.5
    Grade has changed from 2.5 to 5.0

Sidumine (*binding*)
--------------------

Võime luua mitu Exam objekti ning siduda nende Property'd kokku nii, et nende põhjal arvutatakse kokku keskmine hinne. Selleks kasutame **NumberBinding** objekti, kus liidame kaks Property't kokku ja jagame kahega. Kummagi Property väärtuse muutmisel muutub NumberBindingu väärtus automaatselt.

.. code-block:: java

    public class Main {
        public static void main(String[] args) {
            Exam javaExam = new Exam();
            Exam calculusExam = new Exam();

            javaExam.setGrade(4.0);
            calculusExam.setGrade(1.0);

            DoubleProperty javaGrade = javaExam.gradeProperty();
            DoubleProperty calculusGrade = calculusExam.gradeProperty();

            NumberBinding average = (javaGrade.add(calculusGrade)).divide(2.0);
            System.out.println(average.getValue());

            // Change the grade of the calculus exam.
            calculusExam.setGrade(2.5);

            // The average has changed automatically.
            System.out.println(average.getValue());
        }
    }

Väljund konsoolist::

    2.5
    3.25

InvalidationListener ja muutuste ümberarvutamine
------------------------------------------------

Eespool nägime, et keskmine hinne muutus automaatselt, kui ühe seotud Property väärtust muudeti. Reaalsuses toimub ümberarvutamine alles siis, kui Bindingu väärtust küsitakse. Selleks, et ilma väärtust välja arvutamata teada saada, kui midagi on muudetud, saab kasutada **InvalidationListeneri**. Erinevus ChangeListeneriga seisnebki selles, et väärtuse arvutamist vahepeal ei toimu.

.. code-block:: java

    public class Main {
        public static void main(String[] args) {
            Exam javaExam = new Exam();
            Exam calculusExam = new Exam();

            javaExam.setGrade(4.0);
            calculusExam.setGrade(1.0);

            DoubleProperty javaGrade = javaExam.gradeProperty();
            DoubleProperty calculusGrade = calculusExam.gradeProperty();

            NumberBinding average = (javaGrade.add(calculusGrade)).divide(2.0);

            average.addListener(new InvalidationListener() {
                @Override
                public void invalidated(Observable observable) {
                    System.out.println("One of the values in the binding has become invalid!");
                }
            });

            // Change a value - the average is not calculated until we want to access the result
            javaExam.setGrade(5.0);

            // Change it again - no warning is printed because the value was already invalid
            javaExam.setGrade(1.0);

            // Validate the change
            System.out.println(average.getValue());
        }
    }

Tulemus::

    One of the values in the binding has become invalid!
    1.0

Teist korda väärtuse muutmisel hoiatust ei prindita, kuna see oli juba kehtetu. Kui peale valideerimist uuesti midagi muuta, trükitakse esimesel korral taaskord sama hoiatus.