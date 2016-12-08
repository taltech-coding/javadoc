=================
Erilised meetodid
=================

Kõik objektid pärivad automaatselt **Object** klassilt hulga meetodeid, mida võib soovi korral kasutada või üle kirjutada (*override*). Object klassist otse pärituna need meetodid midagi huvitavat ei tee, kuid paljudel klassidel nagu HashMap ja ArrayList on sobivad implementatsioonid olemas.

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

Kui me loome ise mõne klassi ning ei kirjuta üle **toString** meetodit, pole tulemus printimisel kuigi informatiivne. Võtame näiteks mingi klassi **Point**, mis sisaldab x- ja y-koordinaati täisarvudena ja proovime seda välja trükkida.

.. code-block:: java

    Point p = new Point(5, 9);
    System.out.println(p);

Konsooli trükitakse selle tulemusena midagi taolist::

    examples.Point@2a139a55

Tegemist on sõnega, mis koosneb klassi nimest, @-märgist ning objekti hashCode'i (vt allpool) väärtusest kuueteistkümnendarvuna. Nagu näha, ei ole sellest informatsioonist palju kasu, ning võiksime kirjutada sobivama **toString** meetodi.

.. code-block:: java

    @Override
    public String toString() {
        return "Point(" + x + ", " + y + ')';
    }

Antud koodi lisamisel Point klassi on tulemus järgmine::

    Point(5, 9)

equals ja hashCode
==================



clone
=====

