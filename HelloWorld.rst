Hello World
============

Näide
------
Alloleva koodinäite võib kopeerida faili nimega HelloWorld.java

.. code-block:: java

	public class HelloWorld {
		public static void main(String[] args) {
			// Prints "Hello world!" to console window.
			System.out.println("Hello world!");
		}
	}

Selgitus
--------
.. code-block:: java

  public class HelloWorld {
  
See rida defineerib klassi, mille nimi on "HelloWorld". Javas on oluline, et klassi nimi oleks sama mis faili nimi, ehk kui faili nimeks on HelloHello.java, siis peab selles sisalduva klassi nimi olema ka HelloHello (suured ja väikesed tähed on erinevad, näiteks HelloHello ja hellohello on erinevad nimed).

Klasside nimed kirjutatakse suure algustähega. Kui klassi nimi koosneb mitmest sõnast, siis need sõnad kirjutatakse kokku ning iga uue sõna esimene täht on suur: HelloWorld, MySuperClass.

{ märk rea lõpus alustab plokki. Üldiselt klassi koodiplokk sisaldab kogu ülejäänud faili sisu, ehk siis ploki lõpp on faili lõpus. Meie näide on selline, kus plokk lõppeb viimasel real } märgiga.

.. code-block:: java

	public static void main(String[] args) { 
	
See rida kirjeldab ära "main" meetodi. :code:`public static void` osa võib hetkel ignoreerida - sellest räägitakse kursuse jooksul. Oluline on meetodi nimi "main". Faili/klassi käivitamisel pannakse esimesena käima "main" meetod. 

.. code-block:: java

			// Prints "Hello world!" to console window.
			
See on üherealine kommentaar, mida kompilaator ignoreerib.


.. code-block:: java

	System.out.println("Hello world!"); 
	
See on ainuke "main" meetodis sisalduv rida (5. real on "main" meetodi plokki lõpetav } märk). See rida kuvab ekraanile programmeerija poolt määratud teksti. Mida täpsemalt see System.out.println teeb, räägitakse hiljem. Esialgu piisab teadmisest, et selliselt saab teksti ekraanile trükkida: :code:`System.out.println("Mingi tekst");`. Lisaks sellele meetodile on olemas ka :code:`System.out.print("Ilma ln-ta print");`. Nende kahe meetodi vahe on, et esimene prindib välja teksti ja lisab lõppu reavahetuse (kursor liigub järgmisele reale, järgmine väljatrükk läheb järgmisele reale). Teine meetod prindib teksti, aga reavahetust ei lisa (kursor jääb prinditud teksti lõppu; järgmine väljatrükk läheb otse prinditud teksti järgi).

5.rea loogeiline sulg } lõpetab "main" meetodi. Kui "main" meetodis tahetakse veel midagi teha, tuleb see kood lisada enne lõpetavat loogelist sulgu. Kogu kood, mis on "main" meetodis { ja } vahel, läheb käivitamisele.

6.rea loogeline sulg } lõpetab klassi.

Tuleks jälgida, kuidas kood on "trepitud". Iga ploki sisu on eelmisest taande võrra edasi (paremale) nihutatud. Ehk siis kõik kood, mis on klassi ploki sees (read 2-5), on ühe taande võrra paremal. Need, mis on "main" meetodi ploki sees (read 3-4) on omakorda veel ühe taande võrra paremal.

Trepitud koodi on oluliselt parem ja selgem lugeda. Tänapäeval suudavad kõik IDE'd selle treppimise vajadusel ise ära teha (IntelliJ IDEA's näiteks Code -> Reformat Code, Eclipse'is Source -> Format)

----

Lisalugemist "`Hello World`_" ajaloost.

.. _Hello World: http://blog.hackerrank.com/the-history-of-hello-world/
