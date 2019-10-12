Moodul (module-info.java)
=========================

Moodul sarnaneb pakettidele ehk võimaldab koodi strukureerida. Moodul on täiendav abtraktsiooni tase lisaks pakettidele.
Üks moodul peaks koosnema lähedalt seotud pakettidest ja ressurssidest. Moodul on justkui miniprojekt kuhu on lisatud module-info.java fail.
Moodulite module-info.java failipõhine tugi lisati Java 9-ga.

Mõned moodulite eelised on:

* Skalleeritav, modulaarne Java platvorm - väiksemad eraldiseisvad osad ühe monoliidi asemel
* Tugev kapseldamine - vaikesätetes on kõik paketid privaatsed ja *Reflection* keelatud
* Eraldiseisvad ressursid - igal moodulil on oma ressursifailid eraldiseisvalt, ühes suures rakenduses ilma mooduliteta on need kõigi pakettide vahel jagatud (xml, json, yml jne)

module-info.java
----------------
module-info.java fail on iga mooduli juurkaustas ja sisaldab konkreetse mooduli metaandmeid. Mooduli blokk võib olla tühi või sisaldada direktiive (juhiseid).
Järgnevalt toome näiteid direktiivide kasutamisest.

module-info.java näited
-----------------------

module-info.java fail mooduliga my.module mis on ilma direktiivideta:

.. code-block:: java

    module my.module {}


my.module sõltub module1-st:

.. code-block:: java

    module my.module {
      requires module1;
    }


Lubame mooduli my.module paketi com.package1 avalike meetodeid ja muutujaid kasutada tarbijatel (vaikeseadetes ei ole avalikud liikmed tarbijatele nähtavad - tugev kapseldamine):

.. code-block:: java

    module my.module {
      exports com.package1;
    }

my.module sõltub transitiivsest java.sql moodulist, tarbijad kes kasutavad my.module-t omavad ligipääsu ka java.sql moodulile:

.. code-block:: java

    module my.module {
      requires transitive java.sql;
      exports com.package1;
    }


Lubame mooduli my.module paketi com.package1 avalike meetodeid kasutada ainult kindlas paketis olevatel tarbijatel (com.specific):

.. code-block:: java

    module my.module {
      exports com.package1 to com.specific;
    }


Sarnaselt *requires* võtmesõnale, saame kasutada *uses* mida kasutatakse liideste või abtraktsete klasside korral:

.. code-block:: java

    module my.module {
      uses interface.name;
    }


Võimalik on moodul muuta teenuse pakkujaks koos liidese implementatsiooniga:

.. code-block:: java

    module my.module {
      provides MyInterface with MyInterfaceImpl;
    }


Ilma mooduliteta rakenduses on võimalik kasutada *Reflection*'it (isegi privaatsetel meetoditel ja väljadel), moodulite korral saab anda õiguse *open* võtmesõna abil:

.. code-block:: java

    open module my.module {}


Võimalik on anda *Reflection* ligipääs paketipõhiselt:

.. code-block:: java

    module my.module {
      opens com.package1;
    }


Võimalik on anda *Reflection* ligipääs paketipõhiselt kindlatele tarbijatele:

.. code-block:: java

    module my.module {
      opens com.package1 to module1, module2;
    }


Näide java.sql moodulist:

.. code-block:: java

    module java.sql {
      requires transitive java.logging;
      requires transitive java.xml;
      exports java.sql;
      exports javax.sql;
      exports javax.transaction.xa;
      uses java.sql.Driver;
    }

