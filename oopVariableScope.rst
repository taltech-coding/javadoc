=============
Muutuja skoop
=============

Klassimuutujad
--------------

Klassis saab deklareerida muutujad, mida saab kasutada kõigis selle klassi meetodites.

Klassimuutujad kirjutatakse klassi algusesse, enne meetodeid.

.. code-block:: java

    public class Animal {
        public int numberOfLegs;
        public String name;
        public boolean alive = true;
    }

Lokaalsed muutujad
------------------

Meetodi sees saab muutujat kasutada selle bloki sees, kus see deklareeriti.

Piltlikult öeldes saab antud muutujat kasutada samal ja madalamal tasemel, kui on tema deklaratsioon.

.. code-block:: java

    int x = 0;
    int y = 10;
    if (y > 5) {
        x++;
    }
    x += 3;

If-lause sees deklareeritud muutujad ei kehti lausest väljas.

.. code-block:: java

    int y = 10;
    if (y > 5) {
        int z = 2;
    }
    // System.out.println(z)  Annaks vea, kuna seda muutujat pole deklareeritud

Samamoodi kehtib for- või while-tsükli päises deklareeritud muutuja kogu tsükli jooksul, kuid mitte sellest väljas.

.. code-block:: java

    for (int i = 0; i < 10; i++) {
        System.out.println(i);
    }
    // System.out.println(i) Annaks vea

Samas tsükli sees deklareeritud muutuja kehtib ainult ühe tsükli iteratsiooni jooksul.

.. code-block:: java

    for (int i = 0; i < 10; i++) {
        int j = 2;
        System.out.println(j);
        j++
    }

Antud tsükkel prindib alati :code:`2`, kuna iga iteratsioon deklareeritakse muutuja j uuesti.
