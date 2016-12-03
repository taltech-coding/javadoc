Staatilised meetodid, muutujad
===========================================

Esmalt on vaja aru saada, mida üldse staatiline tähendab. Inglise keeles on selle kohta öeldud nii: "Static keyword means that variable or method is shared between all instances of that class as it belongs to the type, not objects". Ehk eesti keeles võiks seda tõlgendada nii, et staatiline muutuja või meetod on jagatud kõikide klassi poolt loodud objektide vahel. Antud meetod või muutuja kuulub tüübile, mitte objektile.

Staatilised meetodid
----------------------

- Kuuluvad klassile, mitte objektile (isendile).
- Saab ligi ainult staatilistele andmetele. Ei saa ligi mitte-staatilistele andmetele.
- Saavad kutsuda välja ainult staatilisi meetodeid.
- Staatilistele meetoditele saab ligi otse läbi klassi nime.

 .. code-block:: java

    //Süntaks
    <class-name>.<method.name>

- Staatiline meetod ei saa kasutada *this* ja *super* võtmesõnu.

Staatilised väljad
-------------------

Kui väli on deklareeritud, kui staatiline, siis kuulub ta klassile. Kõik selle klassi poolt loodud isendid saavad kasutada ühte ja sama staatilist välja. Ligi saab otse klassist, ei ole vaja luua uut objekti.

- Kuuluvad klassile, mitte objekite (isendile).
- Initsialiseeritakse neid välju üks kord, programmi käivitamisel. Neid välju initsialiseeritakse kõige esimestena.
- Sama koopia on kõikide isendite (loodud objektide) käes.
- Staatilistele meetoditele saab ligi otse läbi klassi nime.

.. code-block:: java

    //Süntaks
    static int y = 0;
    //Kättesaamine
    <class-name>.<variable-name>

Meeldetuletus mitte-staatilistest väljadest
--------------------------------------------

Mitte-staatilised väljad kuuluvad klassi isenditele. Igal isendil (instance) on oma koopia sellest väljast.

Näite staatiliste ja mitte-staatiliste väljade kättesaamisest
-------------------------------------------------------------

 .. code-block:: java

    public class Example {

    private static boolean staticField;
    private boolean instanceField;

    public static void main(String[] args) {

        // Staatiline meetod saab staatilise väja kätte otse.
        staticField = true;

        // Staatiline meetod saab mitte-staatilise välja kätte läbi objekti.
        Example instance = new Example();
        instance.instanceField = true;
    }
