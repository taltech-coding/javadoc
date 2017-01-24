=====
Erind
=====

Erind (*exception*) on mingi probleem, mis programmi töö jooksul ilmneb, ning üldjuhul programmi töö seiskub selle pärast. Seetõttu tuleb alati erindeid töödelda, ehk programmile öelda, mida erindi puhul ette võtta.

Üldiselt on kaks erinevat tüüpi erindit.

*Checked* erind
----------------

*Checked* erind ilmneb programmi kompileerimisel. Neid erindeid peab kindlasti programmis töötlema. Siia alla käib näiteks *FileNotFoundException*, mis juhtub siis, kui üritakse lugeda mingit faili, mida ei eksisteeri.

.. code-block:: java

    File file = new File("E://file.txt");
    FileReader fr = new FileReader(file);

Selle erindi vältimiseks oleks mõistlik kasutada *try-catch* blokki.

.. code-block:: java

    try {
        File file = new File("E://file.txt");
        Filereader fr = new FileReader(file);
    } catch (FileNotFoundException ex) {
        System.out.println("This file doesn't exist.");
    }

Teine viis erindit töödelda on see meetodist välja visata (*throw*). Niimoodi saab erindi anda edasi mingile teisele meetodile, mis seda töötleb või annab omakorda järgmisele meetodile edasi. Lõpuks peab mingi meetod kindlasti antud erindiga midagi tegema.

.. code-block:: java

    public static void main(String[] args) {
        try {
            openFile("E://file.txt");
        } catch (FileNotFoundException ex) {
            System.out.println("This file doesn't exist.");
        }
    }

    public void openFile(String filename) throws FileNotFoundException {
        File file = new File(filename);
        Filereader fr = new FileReader(file);
    }

*Unchecked* erind
------------------

*Unchecked* erind ilmneb programmi käivitamisel, seetõttu kutsutakse neid ka *runtime* erinditeks. Nende erindite põhjus on enamasti mingi loogiline viga programmikoodis (*bug*). Neid erindeid nö "valmis" programmi töös ei tohiks esineda, ehk kõik sellised loogilised vead tuleks programmis ära parandada enne programmi kasutamist.

Üks selline erind on näiteks *ArrayIndexOutOfBoundsException*.

.. code-block:: java

    int[] array = new int[4];
    System.out.println(array[5]);

Antud näites on deklareeritud massiiv, mille suurus on 4, kuid on proovitud välja kutsuda selle massiivi 6-ndat elementi. Programmi käivitades ilmnebki antud *ArrayIndexOutOfBoundsException*.
