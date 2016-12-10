*Inheritance* ehk klasside laiendamine
======================================

Klasside laiendamise ehk *Inheritance*'i abil saab luua ülemklasse ning neile vastavaid alamklasse. 
Ülemklass on justkui üldisem mõiste, mille alla saavad kuuluda täpsemad sama mõistet kirjeldavad mõisted.
Näiteks võib üldisemaks mõisteks olla pirukas, omakorda on aga olemas ka magusad ja soolased prirukad,
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
Oluline on silmas pidada, et klasse laiendades eksisteeriks kahe klassi vahel ülem- ja alamklasse iseloomustav suhe,
näiteks klassi *Car* alamklassiks ei saa olla *Wheel*, küll aga saab laiendavaks klassiks olla *Hatchback* või *Convertible*.
Oletame et on olemas järgnev klass:

.. code-block:: java

    public class Pie {
       
    }

Selleks, et laiendada klassi loome uue klassi *SavouryPie* kasutades *extends* võtmesõna ning selle järgi lisame selle klassi nime,
mida soovime laiendada, antud juhul *Pie*.

.. code-block:: java

    public class SavouryPie extends Pie {
       
    }
    
    
Siia tuleb kirjutada veel pärimise kohta



