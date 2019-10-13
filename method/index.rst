===================
Meetod (funktsioon)
===================

Kirjeldus
---------

Meetod täidab ideaalis ainult ühte funktsionaalsust (näiteks antakse ette 2 numbrit ning meetod liidab need kokku ja tagastab saadud väärtuse. Lahutamise, korrutamise, jagamise jms see meetod ei tegele, vaid selleks on eraldi meetodid).

Meetodi ülesehitus
-------------------

*modifier* − defineerib nähtavuse ning selle kasutamine on valikuline (nt *public*).

*returnType* − meetodi tagastustüüp (*void* ei tagasta midagi).

*nameOfMethod* − meetodi nimi. 

*Parameters* − parameetrid, mis meetodile ette antakse. Võib ka tühjaks jätta, kui ei soovi midagi ette anda.

*method body* − kogu loogika, mida see meetod teeb.

.. code-block:: java

    modifier returnType nameOfMethod (Parameters) {
       // method body
    }

Kuna nähtavus on *public*, siis see funktsioon on nähtav kõikjale.
Tagastustüüp on *int*, seega antud funktsioon tagastab täisarvu ehk *int*-tüüpi väärtuse.

.. code-block:: java

    public int add(int a, int b) {
        return a + b;
    }
    
Kuna nähtavus on *private*, siis see funktsioon on nähtav vaid klassis, kus see paikneb.
Tagastustüüp on *String*, seega antud funktsioon tagastab sõne ehk *String*-tüüpi väärtuse.

.. code-block:: java

    private static String removeFirst(String word) {
        return word.substring(1);
    }

Kui nähtavust ei ole defineeritud, on see *package-private*.

Kuna nähtavus on *package-private*, siis see funktsioon on nähtav vaid selle paketi klassidele, kus see paikneb.
Tagastustüüp on *List<Double>*, seega antud funktsioon tagastab loendi ujukomaarvudest ehk *List<Double>*-tüüpi väärtuse.

.. code-block:: java

    List<Double> turnIntoList(double a, double b) {
        return Arrays.asList(a, b);
    }

.. toctree::
   :maxdepth: 2
   :caption: Alamteemad:
   
   method-void
   method-arguments
   method-return-value
   method-overload
