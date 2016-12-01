=========
Alamklass
=========
Alamklass Javas pärib omadusi ülemklassist. Tänu pärimisele lisavad alamklassid spetsiifilist käitumist üldistatud ülemklassile.

Ütleme, et *koer* on *loom*. Seepärast on loogiline luua klass *loom* ning panna *koer* pärima sealt. Sel juhul on alamklassiks *koer* ning ülemklassiks *loom*.


Ülevaade
*********
Klassi, mis on tuletatud teisest klassist, nimetatakse *alamklassiks*. Klassi, millest tuleneb *alamklass*, nimetatakse *ülemklassiks*.

Välja arvatud *Objekt*'i tüüpi klass, kõikidel klassidel on olemas oma üks ja ainus ülemklass.

Javas on kõik klassid üht või teist pidi tuletatud *Object* klassist.


Mida saab teha alamklassis
****************************


Alamklass pärib kõik *public* ja *protected* ülemklassi liikmed, vaatamtata sellele, mis paketis alamklass on. Kui alam ning ülemklass on samas paketis, siis pärib alamklass ka *package-private* liikmed ülemklassist.


- Päritud välju saab kasutada nii nagu tavavälju
- Saab deklareerida välja alamklassis täpselt sama nimega nagu ülemklassis, peites ülemklassi väli (ei ole soovitatav)
- Alamklassis saab deklareerita uusi välja, mida ülemklassis ei ole
- Päritud meetodeid saab kasutada nii nagu nad on.
- Kui kirjutada meetod sama signatuuriga alamklassis, nagu ta on ülemklassis, siis kirjutatakse meetod üle @Override.
- Saab deklareerida uusi meetodeid alamklassis, mida ei ole ülemklassis. 
- Alamklassis konstruktoris saab deklareerida ülemklassi konstorktor *super* võtmesõna abil.

 

Private liikmed superklassis
****************************

Kui ülemklassis on liikmeid (meetodid, väljad jne.), mis on deklareeritud, kui *private*, siis alamklass neid ei päri. Samas, kui ülemklassis on *public* või *protected* meetodeid, mis lubavad *private* väljadele ligi, siis neid saab kasutada ka alamklassis. Näiteks *getterid* ja *setterid*

Näide alamklassidest ja ülemklassist
************************************

.. code-block:: java

      public class Animal {

      public static void hide() {
      System.out.println("The hide method in Animal.");
      }
      }

      public class Cat extends Animal {

      public static void hide() {
      System.out.println("The hide method in Cat.");
      }
      public static void main(String[] args) {
      Cat myCat = new Cat();
      myCat.hide();
      }
      }

Kuna loodud objekt on Cat tüüpi, siis loogiline on, et prinditakse *"The hide method in Cat."*

.. code-block:: java

      public class Animal {

      public static void hide() {
      System.out.println("The hide method in Animal.");
      }
      }

      public class Cat extends Animal {

      public static void main(String[] args) {
      Cat myCat = new Cat();
      myCat.hide();
      }
      }

Nüüd ei ole meil alamklassis üldse meetodit *hide()*, kuid vaatamata sellele prinditakse konsooli *"The hide method in Animal."*, kuna alamklass saab ülemklassi meetoditele ligi.
