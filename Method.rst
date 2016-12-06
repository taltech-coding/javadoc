===================
Meetod (funktsioon)
===================

Kirjeldus
---------

Meetod täidab ideaalis ainult ühte funktsionaalsust (näiteks antakse ette 2 numbrit ning meetod liidab need kokku ja tagastab saadud väärtuse. Lahutamise, korrutamise, jagamise jms see meetod ei tegele, vaid selleks on eraldi meetodid).

Meetodi ülesehitus
-----

modifier − defineerib nähtavuse ning selle kasutamine on valikuline (nt public).

returnType − meetodi tagastustüüp (void ei tagasta midagi).

nameOfMethod − meetodi nimi. 

Parameters − parameetrid, mis meetodile ette antakse. Võib ka tühjaks jätta, kui ei soovi midagi ette anda.

method body − kogu loogika, mida see meetod teeb.

.. code-block:: java

    modifier returnType nameOfMethod (Parameters) {
       // method body
    }
