*Inheritance* ehk pärimine
==========================

*Inheritance*'i ehk pärimise abil saab luua ülemklasse ning neile vastavaid alamklasse. 
Ülemklass on justkui üldisem mõiste, mille alla saavad kuuluda täpsemad sama mõistet kirjeldavad mõisted.
Näiteks võib üldisemaks mõisteks olla pirukas, 
omakorda on aga olemas ka magusad ja soolased prirukad,
soolased pirukad on võimalik jaotada näiteks juustu-, liha-, kapsa- ning porgandipirukateks.
Samalaadset loogikat rakendatakse ka objektorienteeritud koodi kirjutamisel.
Ülemklassil on meetodid ning väljad, mis laiendamisel kanduvad edasi alamklassidele, 
nagu piruka üldised omadused kapsapirukale,
kuid alamklassil võivad olla omakorda täiendavad meetodid ning väljad.

Klasside laiendamisel kehtivad järgmised reeglid:
-------------------------------------------------

- Laiendav klass ehk alamklass pärib kõik laiendatava klassi ehk ülemklassi meetodid (va need, mille nähtavuseks on määratud *private*)
- Alamklass kirjutab üle kõik laiendatava klassi meetodid, mis on mõlemas klassis sama nimega
- Laiendav klass ehk alamklass võib lisada uusi meetodeid

*extends* võtmesõna
-------------------

Klasse saab muuta alamklassideks kasutades *extends* võtmesõna.
Oluline on silmas pidada,
et klasse laiendades eksisteeriks kahe klassi vahel ülem- ja alamklasse iseloomustav suhe, 
näiteks klassi *Car* alamklassiks ei saa olla *Wheel*, 
küll aga saab laiendavaks klassiks olla *Hatchback* või *Convertible*, 
juhul kui puudub ülem- ning alamklasse iseloomustav suhe tuleks kasutada hoopis kompositsiooni.

Oletame et on olemas järgnev klass:

.. code-block:: java

    public class Pie {
    
    }
    

Selleks, et laiendada klassi tuleb luua uus klass *SavouryPie* kasutades *extends* võtmesõna, mille järgi lisatakse selle klassi nimi,
mida soovitakse laiendada, antud juhul on selleks klass *Pie*.

.. code-block:: java

    public class SavouryPie extends Pie {

    }
    
*Override* võtmesõna
--------------------

*Override* võtmesõna kasutatakse meetodite ülekirjutamiseks, 
alamklassis defineeritakse sama nime ning samasuguste argumentidega
meetod nagu ülemklassis, 
meetodil peab olema tagastustüübiks sama tagastustüüp, mis ülemklassiski või sealse tagastustüübi alamtüüp. 
Tavaliselt kasutatakse ülekirjutamist, 
kui alamklassi objektidega
peab saama teha sarnast tegevust nagu ülemklassi objektidega, 
kuid on vaja arvesse võtta mõningaid üksikud alamklassile omased tegevusi
või omadusi.
Selleks defineeritakse sama nimega meetod, mille sisu erineb pisut ülemklassi samanimelise funktsiooni koodist. 

Täpsemalt on võimalik selle kohta lugeda OOP *Override* ja *Overload* teema juures:
https://github.com/tutjava/materjalid/blob/master/oopOverrideVsOverload.rst

Konstruktorid
-------------

Uut alamklassi objekti luues kutsutakse kõigepealt alati välja ülemklassi konstruktor. 
Juhul kui ülemklassis on ainult argumentidega konstruktor ning alamklassi konstrukoris pole kasutatud *super()* võtmesõna abi, 
et ülemklassi argumentidega konstruktorit välja kutsuda, siis kirjutatud kood ei kompileeru. 
Kui ülemklassis pole konstruktorit, siis kasutatakse kompileerimisel vaikimisi argumendita konstruktorit. 
Samuti kompileerub kood, kui ülemklassis on olemas argumendita konstruktor.

Detailsemalt käsitletakse konstruktoreid:
https://github.com/tutjava/materjalid/blob/master/oopConstructor.rst

*super* võtmesõna kohta saab lisainfot: :doc:`oop-super`