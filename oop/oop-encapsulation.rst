*Encapsulation* ehk kapseldamine
================================

*Encapsulation* ehk kapseldamine on üks OOP'i põhikontseptsioonidest,
Javas kujutab see endast muutujate ning neid kasutava koodi sidumist ühtseks tervikuks.
Kapseldamise korral peidetakse klassi välju teiste klasside eest, nendele muutujatele pääsetakse ligi ainult läbi meetodite,
mis on väljadega samas klassis.
Kapseldamine aitab vältida valede muutujate kasutamist, muutes väljadele ligipääsemise teadlikuks ning kontrollitud tegevuseks.

Kapseldamiseks on vaja:
-----------------------

- Anda klassis olevatele väljadele *private* nähtavus
- Luua väljade muutmiseks *getter* ja *setter* meetodid

*Getter* ning *Setter* meetodid
-------------------------------

*Getter* meetodit kasutatakse klassis oleva välja väärtuse teada saamiseks,
seega ei võta *getter* meetod endale sisendeid ning tagastab muutuja väärtuse.
*Getter* meetod on *public* nähtavusega, mis tähendab, 
et klassis olevale väljale on vaatamata *private* nähtavusele võimalik ligi pääseda ka teistest klassidest.
*Getter* meetodite nimeks on *get* + VäljaNimi + (), erandiks on *boolean* väärtused,
millel on *getter*'ite asemel nende olekut küsivad meetodid, mille nimetused on kujul *is* + BooleanMuutujaNimi + ().

*Setter* meetod on mõeldud klassis olevate *private* väljade väärtuste muutmiseks,
selle sisendiks on uus väärtus, mida soovitakse muutujale anda.
*Setter*'id on *void* meetodid, mis tähendab et nad ei tagasta midagi.
*Setter* meetodeid nimetatakse järgnevalt: *set* + VäljaNimi + ().

Selleks, et ei peaks palju vaeva nägema selle nimel, et luua *getter* ning *setter* meetodeid,
pakub näiteks *IntelliJ* mugavat võimalust enda loodud klassiväljadele automaatselt vastavad meetodid genereerida.
Tarvis on ainult teha paremklikk väljal,
millele soovitakse genereerida meetodeid, valida avanenud menüüst *Generate...* ning otsustada,
kas genereerida *Getter*, *Setter* või suisa mõlemad korraga.


.. code-block:: java

    public class EncapsulationExample {

    // All of these fields have private visibility

    private int number;
    private boolean state = false;
    private ArrayList<Integer> list;

    public ArrayList<Integer> getList() {

        //returns the field variable

        return list;
    }

    public void setList(ArrayList<Integer> list) {

        // The word this refers to the current class
        // in this instance EncapsulationExample

        this.list = list;
    }

    public boolean isState() {
        return state;
    }

    public void setState(boolean state) {
        this.state = state;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }


    public static void main(String[] args) {

        // Getter and setter methods can be used in other classes


        EncapsulationExample example = new EncapsulationExample();


        // Returns 0 because number doesn't have a value yet
        System.out.println(example.getNumber());


        // This setter gives a value to the variable number
        example.setNumber(666);


        // Returns false, since it already has a set value
        System.out.println(example.isState());


        // Changes the value of state to true
        example.setState(true);


        // Now this getter returns true
        System.out.println(example.isState());


        // Creates a new ArrayList object
        ArrayList<Integer> list = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6));


        // Getter and Setter methods can be used with any type of objects
        example.setList(list);


        // Returns [1, 2, 3, 4, 5, 6]
        System.out.println(example.getList().toString());

    }
 }
 

See koodinäide tagastab:

.. code-block:: java

    0
    false
    true
    [1, 2, 3, 4, 5, 6]


