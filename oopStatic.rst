Staatilised meetodid, muutujad
===========================================

Esmalt on vaja aru saada, mida üldse staatiline tähendab. Daniel Y. Liang'i Javat õpetavas raamatus on kirjas selle kohta nii. "Static keyword means that variable or method is shared between all instances of that class as it belongs to the type, not objects". Ehk eesti keeles võiks seda tõlgendada nii, et staatiline muutuja või meetod on jagatud kõikide klassi poolt loodud objektide vahel. Antud meetod või muutuja kuulub tüübile, mitte objektile.

Staatilised meetodid
----------------------

- Kuuluvad klassile, mitte objektile(isendile=.
- Saab ligi ainult staatilistele andmetele. Ei saa ligi mitte-staatilistele andmetele.
- Saavad kutsuda välja ainult staatilisi meetodeid.
- Staatilistele meetoditele saab ligi otse läbi klassi nime.

 .. code-block:: java

    //Süntaks
    <class-name>.<method.name>

- Staatiline meetod ei saa kasutada *this* ja *super* võtmesõnu.

Staatilised väljad
-------------------

Kui väli on deklareeritud, kui staatiline, siis kuulub ta klassile. Kõik selle klassi poolt loodud isendid saavad kasutada ühte ja sama staatilist välja. Ligi saab otse klassist, ei ole vaja luua objekti.

- Kuulub klassile, mitte objekite(isendile).
- Initsialiseeritakse neid välju ainult üks kord, programmi käivitamisel. Neid välju initsialiseeritakse esimestena.
- Sama koopia on kõikide isendite (loodud objektide) käes.
- Kätte saab staatilise välja otse klassi nime järgi. Objekti ei ole vaja.

.. code-block:: java

    //Süntaks
    static int y = 0;
    //Kättesaamine
    <class-name>.<variable-name>

Mitte-staatilised väljad
------------------------

Mitte-staatilinsed väljad kuuluvad klassi isenditele. Igal isendil (instance) on oma koopia sellest väljast.

Näite staatiliste ja mitte-staatiliste väljade kättesaamisest
-------------------------------------------------------------

 .. code-block:: java

    public class Example {

    private static boolean staticField;
    private boolean instanceField;

    public static void main(String[] args) {

        // Staatiline meetod saab ilusti kätte otse.
        staticField = true;

        // staatiline meetod saab kätte läbi objekti viida.
        Example instance = new Example();
        instance.instanceField = true;
    }
