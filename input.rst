==================================
Sisendi lugemine standardsisendist
==================================

Standardsisend on sisend mida saab programmi sisestada. Kui seda pole mujale suunatud, ootab programm standardsisendit programmi käivitanud klaviatuurilt.
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
Scanner saab lugeda erinevaid sisendeid. Standardsisendist lugemiseks tuleb talle kaasa anda *System.in*.
Üks Scanneri suuri eeliseid on see, et sellega saab sisendit otse töödelda. Scanner klassil on palju erinevaid meetodeid, näiteks *nextInt*, *hasNext*, *findInLine* jne, millega saab sisendi lugemist kontrollida.

Scanner tükeldab teksti sõnedeks kasutades tühikuid, reavahetust jms sümboleid (täpsemalt kasutab meetodit :code:`Character.isWhitespace` eraldajate tuvastamiseks).

*hasNext* meetodid tagastavad tõeväärtuse, kas järgmine tükk (*token*) eksisteerib/on vastavat tüüpi väärtus.
*next* meetodid loevad järgmise tüki antud tüübiks ja tagastavad selle.

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



Scanner'i näide ja kasutamine
------------------------------

Toome siin peatükis näite, kuidas võiks Scanner'it oma koodis kasutada.

Scanner'i loomisel võib sellele argumendiks anda sõne, mida hakatakse töötlema. Siin näidetes oleme seda võimalust kasutanud, et näited oleks lihtsamini loetavad. Aga kõik need näited töötavad ka kasutades :code:`System.in` argumendina.

Alustame lihtsa näitega ja täiendame oma koodi samm-sammult.

Loeme kõigepealt ühe arvu sisendist:

.. code-block:: java

        Scanner scanner = new Scanner("123");
        double nr = scanner.nextDouble();
        System.out.println("Got nr:" + nr);
        scanner.close();
        
.. code-block:: console

    Got nr: 123.0
    
*nextDouble* võtab järgmise tüki ("123"), teeb sellest double-tüüpi väärtuse ja tagastab.

Aga mis siis, kui kasutaja ei sisesta korrektset sisendit? Eelmine kood annaks siis vea. Enne *next* meetodit peaks veenduma, et järgmisena tulev tükk on üldse õiget tüüpi (ja et üldse on järgmine tükk).

.. code-block:: java

        Scanner scanner = new Scanner("notanumber");
        if (scanner.hasNextDouble()) {
            double nr = scanner.nextDouble();
            System.out.println("Got nr: " + nr);
        } else {
            System.out.println("Not a number!");
        }
        scanner.close();
        
Väljund:

.. code-block:: console

    Not a number!
    
 
Kui kasutaja sisestas ebasobiva sisendi, tahaksime, et ta prooviks uuesti. Paneme kogu eelmise koodi tsüklisse - kordame sisendi küsimist seni, kuni kasutaja sisestab korrektse sisendi.

.. code-block:: java

        Scanner scanner = new Scanner("notanumber");
        while (true) {
            System.out.println("Insert your salary:");
            if (scanner.hasNextDouble()) {
                double nr = scanner.nextDouble();
                System.out.println("Got nr: " + nr);
                break;
            } else {
                System.out.println("Not a number!");
            }
        }
        scanner.close();
        
Lisasime eelneva näite ümber while-tsükli. Kui kasutaja sisestab arvu korrektselt, lõpetatakse tsükkel (:code:`break` lause). Kui kasutaja ei sisesta korrektset arvu, toimib kood järgmiselt:
 - tingimus (*hasNextDouble*) annab tulemuseks väär, mistõttu käivitub tingimuslause *else*-plokk.
 - *else*-plokis kuvatakse kasutajale teade "Not a Number!"
 - programm jätkab *while*-tsükli käivitamist algusest
 - kasutajale kuvatakse "Insert your salary:"
 - tingimus *hasNextDouble* on endiselt väär, kuna sisendis (scanner'is) ootab endiselt sama tükk.
 
Ehk siis antud koodi puhul jääb "Insert your salary:" lõputult ekraanile trükkima.

Väljund:

.. code-block:: console

    Insert your salary: 
    Not a number!
    Insert your salary: 
    Not a number!
    Insert your salary: 
    Not a number!
    Insert your salary: 
    Not a number!
    ...
    
Selleks, et saaksime eelnevalt ilmnenud "vea" parandada, tuleb ebakorrektne tükk sisendist "ära lugeda" (peale lugemist eemaldatakse see järjekorrast). Kasutame selleks scanner'i meetodit *next*, mis loeb järgmise tüki sõnena (sõltumata sellest, mis tüüpi see tükk võiks tegelikult olla).

.. code-block:: java

        Scanner scanner = new Scanner("notanumber nope 3");
        while (true) {
            System.out.println("Insert your salary:");
            if (scanner.hasNextDouble()) {
                double nr = scanner.nextDouble();
                System.out.println("Got nr: " + nr);
                break;
            } else {
                String temporary = scanner.next();
                System.out.println("Not a number! Got: " + temporary);
            }
        }
        scanner.close();
        
Väljund:

.. code-block:: console

    Insert your salary:
    Not a number! Got: notanumber
    Insert your salary:
    Not a number! Got: nope
    Insert your salary:
    Got nr: 3.0

Nagu näha, tuvastab kood ilusti ära, et kasutaja on sisestanud ebakorrektse arvu. Programm loeb kasutaja ebakorrektse sisendi *next* meetodiga "ära". Järgmisel korral seda sisendit enam ei loeta. Antud koodinäites on *next* tulemus salvestatud muutujasse selleks, et seda saaks välja näidata. Kui seda välja pole vaja näidata, ei ole seda mõtet ka muutujasse lugeda. Piisab lihtsalt :code:`scanner.next();`.

.. _scanner_no_such_element_exception:

Tegelikult on viimases näites veel üks probleem. Nimelt võib juhtuda, et sisend saab varem otsa. Näiteks kui sisend oleks lihtsalt "a", siis loetakse sealt "a", seejärel saab sisend tühjaks. Meie näites aga *while*-tsükkel jätkab tööd. Kui programm jõuab if-lauseni, on see väär (kuna järgmist double-tüüpi väärtust me sisendist ei leia), käivitub else-plokk. Seal aga saab meie programm vea, kuna :code:`scanner.next();` ei suuda midagi lugeda (antakse :code:`NoSuchElementException`). Siin on lihtsustatud näide:

.. code-block:: java

        Scanner scanner = new Scanner("a b");
        while (true) {
            String token = scanner.next();
            System.out.println("Got:" + token);
        }

Tulemus:

.. code-block:: console

    Got:a
    Got:b
    Exception in thread "main" java.util.NoSuchElementException
        at java.util.Scanner.throwFor(Scanner.java:862)
        at java.util.Scanner.next(Scanner.java:1371)
        ....
        
Kuigi loeme andmetüübi mõttes turvaliselt :code:`next()`, tekib probleem sellega, et scanner'i sisend saab läbi (antud juhul sõne). :code:`Standard.in`'iga seda nii lihtsalt ei juhtu (kuigi on võimalik, et see suletakse mingil põhjusel). Nagu näha, tekib viga "NoSuchElementException". 

Seega, me peaksime lisama kontrolli, kas midagi üldse on sisendis. Kui sisend on tühi, siis lõpetame while-tsükli ära.

Tavaliselt tuleb sisendit valideerida ka lähtuvalt sisust (seni vaatasime vaid andmetüübi probleemi). Oletame, et meil on koodis defineeritud meetod *isValid*, mis saab argumendiks arvu ja tagastab tõeväärtuse, kas argument on sobiv. Näiteks võib *isValid* kontrollida, kas sisend on korrektne aastaarv (sobivad näiteks arvud 2017 - 2050), inimese pikkus cm (sobivad 90.0 - 200.0), palga suurus (>= 0) jne. Kui sisestatud arv ei vasta nõuetele, tuleb see uuesti küsida. Selleks lisame kontrolli, kas sisestatud arv on korrektne.

.. code-block:: java

        Scanner scanner = new Scanner("wat? -4 600");
        while (true) {
            System.out.println("Insert your salary:");
            if (!scanner.hasNext()) {
                System.out.println("Bye!");
                break;
            }
            if (scanner.hasNextDouble()) {
                double nr = scanner.nextDouble();
                if (isValid(nr)) {
                    System.out.println("Got nr: " + nr);
                    break;
                } else {
                    System.out.println("Salary must be in range [0..1000].");
                }
            } else {
                String temporary = scanner.next();
                System.out.println("Not a number! Got: " + temporary);
            }
        }
        scanner.close();
        
Väljund:

.. code-block:: console

    Insert your salary:
    Not a number! Got: wat?
    Insert your salary:
    Salary must be in range [0..1000].
    Insert your salary:
    Got nr: 600.0
    
    
Ülaltoodud koodinäide oli mõnevõrra lihtsustatud, et oleks parem seletada ja jälgida. Korrektsem oleks kogu asi kirjutada umbes nii:

.. code-block:: java

        // define salary here, then we can use it later after reading input
        // the value -1 gives us the opportunity to check if the input
        // reading part has failed or not. Not really necessary.
        double salary = -1;

        // try with resources - the scanner is closed automatically
        // and optionally, catch-blocks can be added
        try (Scanner scanner = new Scanner(System.in)) {
            while (true) {
                // no need to use println here as user inserts the number
                // after the text and hits enter (we then get a new line).
                System.out.print("Insert your salary:");
                if (!scanner.hasNext()) {
                    // if for some reason the scanner is closed,
                    // let's break the while
                    System.out.println("Bye!");
                    break;
                }
                if (scanner.hasNextDouble()) {
                    salary = scanner.nextDouble();
                    if (isValid(salary)) {
                        System.out.println("Thanks!");
                        break;
                    }
                    // no need to else. if the previous condition
                    // was true, the break would end the while loop
                    System.out.println("Salary must be in range [0..1000]. Try again!");
                } else {
                    scanner.next();
                    System.out.println("Not a number, try again!");
                }
            }
        }
        // we can check here. if the value is -1, then the input loop has failed
        if (salary != -1) {
            System.out.println("We got your salary:" + salary);
        }
        
Näiteks võib saada sellise väljundi:

.. code-block:: console 

    Insert your salary:no
    Not a number, try again!
    Insert your salary:ok
    Not a number, try again!
    Insert your salary:-100
    Salary must be in range [0..1000]. Try again!
    Insert your salary:500
    Thanks!
    We got your salary:500.0



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
