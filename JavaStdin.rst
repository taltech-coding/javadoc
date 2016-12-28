==================================
Sisendi lugemine standardsisendist
==================================

Kasutaja sisendit saab Javas konsoolist lugeda mitmel viisil.

**NB** Sisendi-väljundiga töötades peab tegelema ka IOExceptioniga.
Antud näiteid käivitades võib erindi lihtsalt main-meetodist välja visata

.. code-block:: java

    public static void main(String[] args) throws java.io.IOException

System.in.read()
----------------

*System.in.read()* meetod loeb standardsisendist ühe baidi ja tagastab selle karakteri ASCII väärtuse int-ina.

Kood:

.. code-block:: java

    int input = System.in.read();

Sisend:

.. code-block:: java

    >> hello

Antud näites on inputi väärtus 104, ehk tähe 'h' ASCII väärtus.
ASCII-väärtuse saab castida characteriks.

Kood:

.. code-block:: java

    System.out.println((char) input);

Väljund:

.. code-block:: java

    h

Scanner klass
---------------

Mugavam viis sisendit lugeda on kasutada Scanner klassi.
Scanner saab lugeda erinevaid sisendeid. Standardsisendist lugemiseks tuleb talle kaasa anda System.in
Üks Scanneri suuri eeliseid on see, et sellega saab sisendit otse *parse*-ida. Scanner klassil on palju erinevaid meetodeid, näiteks *nextInt*, *hasNext*, *findInLine*, jne, millega saab sisendi lugemist kontrollida.

Scanner *parse*-ib teksti tokeniteks, ehk tühikutega eraldatud sõnad.

*hastNext* meetodid tagastavad booleani, kas järgmine token eksisteerib/on vastav väärtus.
*next* meetodi *parse*-ivad järgmise tokeni antud tüübiks ja tagastavad selle.

Kood:

.. code-block:: java

    Scanner in = new Scanner(System.in);
    System.out.println(in.nextInt());
    System.out.println(in.next());
    System.out.println(in.nextBoolean());
    System.out.println(in.next());
    if (in.hasNext()) System.out.println("More input.");

Sisend:

.. code-block:: java

    >> 24 randomword true 160

Väljund:

.. code-block:: java

    24
    randomword
    true
    160



BufferedReader klass
----------------------

BufferedReaderit saab samuti kasutada erinevate sisendite lugemiseks, kuid see vaid loeb teksti ja tagastab selle.
BufferedReaderi eelis on see, et sellel on suurem buffer, ehk siis suuri sisendeid on soovitatav BufferedReaderiga lugeda.
Samuti on BufferedReader sünkroniseeritud, ehk seda saab kasutada lõimedega (threads).

BufferedReaderile tuleb initisaliseerimisel kaasa anda mingi muu Reader, näiteks InputStreamReader või FileReader.

Kood:

.. code-block:: java

    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    System.out.print("Enter your name: ");
 
    String name = reader.readLine();
    System.out.println("Your name is: " + name);

Sisend:

.. code-block:: java

    >> Alice

Väljund:

.. code-block:: java

    Your name is Alice
