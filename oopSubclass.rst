=========
Alamklass
=========

Ülevaade
*********
Klassi, mis on tuletatud teisest klassist, nimetatakse *alamklassiks*. Klassi, millest tuleneb *alamklass*, nimetatakse *ülemklassiks*.

Kõikidel klassidel peale *Object*-tüüpi klassi on olemas oma üks ja ainus ülemklass.

Javas on kõik klassid üht- või teistpidi tuletatud *Object* klassist.

Seega, kui pöördutakse mõne meetodi poole *someObject.someMethod()*,  siis otsitakse seda kõigepealt someObject instantsist. Kui seal ei ole, siis selle ülemklassis jne. Kuni *Object* klassini välja.

Alamklass Javas pärib omadusi ülemklassist. Tänu pärimisele lisavad alamklassid spetsiifilist käitumist üldistatud ülemklassile. Püüame seda näite abil selgitada.

Ütleme, et *koer* on *loom*. Seepärast on loogiline luua klass *loom* ning panna *koer* pärima sealt. Sel juhul on alamklassiks *koer* ning ülemklassiks *loom*.

 .. code-block:: java
 
    public class Animal {
    }
    
    public class Dog extends Animal{
    }




Mida saab teha alamklassis
****************************


Alamklass pärib kõik *public* ja *protected* ülemklassi liikmed olenemata sellest, mis paketis alamklass on. Kui alam- ning ülemklass on samas paketis, siis pärib alamklass ka *package-private* liikmed ülemklassist.


- Päritud välju saab kasutada nagu tavavälju.
- Alamklassis tohib deklareerida täpselt sama nimega välja nagu ülemklassis, peites ülemklassi välja (ei ole soovitatav).
- Alamklassis saab deklareerida uusi välju, mida ülemklassis ei ole.
- Päritud meetodeid saab kasutada nii, nagu soovitakse.
- Kui kirjutada alamklassi meetod sama signatuuriga nagu tema ülemklassis, siis kirjutatakse meetod üle @Override.
- Alamklassis saab deklareerida uusi meetodeid, mida ei ole ülemklassis. 
- Alamklassi konstruktoris saab kasutada ülemklassi konstruktorit *super* võtmesõna abil.

 

Privaatsed liikmed ülemklassis
******************************

Kui ülemklassis on liikmeid (meetodid, väljad jne.), mis on deklareeritud kui *private*, siis alamklass neid ei päri. Samas, kui ülemklassis on *public* või *protected* meetodeid, mis võimaldavad ligipääsu *private* väljadele, siis neid saab kasutada ka alamklassis. Näiteks *getterid* ja *setterid* on konstruktsioonid, mille abil saab *private* väljadele ligi. 

.. code-block:: java

  public class Student {
      private String name;

      public String getName() {
          return this.name;
      }

      public void setName(String name) {
         this.name = name;
      }
  } 

Näide alamklassidest ja ülemklassist
************************************

.. code-block:: java

      public class Animal {

          public void hide() {
              System.out.println("The hide method in Animal.");
          }
      }

      public class Cat extends Animal {
      
          @Override
          public void hide() {
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

          public void hide() {
              System.out.println("The hide method in Animal.");
          }
      }

      public class Cat extends Animal {

          public static void main(String[] args) {
               Cat myCat = new Cat();
               myCat.hide();
          }
      }

Nüüd ei ole meil alamklassis üldse meetodit *hide()*, kuid vaatamata sellele prinditakse konsooli *"The hide method in Animal."*. Alamklass kasutab ülemklassi meetodit, kuna midagi muud nimega *hide* tal kasutada ei ole.
