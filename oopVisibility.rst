OOP: nähtavus (private, protected, public, tühi)
================================================
-----------------------------------------------------------------------------------------
*Nähtavuse modifikaatorid võimaldavad määrata klassi ning selle klassi väljade nähtavust*
-----------------------------------------------------------------------------------------

Ülevaateliselt näitab allolev tabel erinevate modifikaatorite mõju kaugust. 

 - Package = pakett
 - Subclass = alamklass
 - same pkg, diff pkg  = sama pakett, teine pakett

+------------+------------+-----------+----------------------+----------------------+-----------+
|            | Class      | Package   |Subclass(same pkg)    | Subclass(diff pkg)   | World     | 
+============+============+===========+======================+======================+===========+ 
| public     |      jah   |    jah    | jah                  |      jah             |    jah    |
+------------+------------+-----------+----------------------+----------------------+-----------+
| protected  |      jah   |    jah    | jah                  |      jah             |     ei    |
+------------+------------+-----------+----------------------+----------------------+-----------+ 
| no modifier|      jah   |     jah   | jah                  |       ei             |      ei   | 
+------------+------------+-----------+----------------------+----------------------+-----------+
| private    |      jah   |     ei    | ei                   |       ei             |     ei    |
+------------+------------+-----------+----------------------+----------------------+-----------+


*private* 
---------

Meetoditele, muutujatele ning konstruktoritele, mis on määratud kui *private*, saab ligi ainult samast klassist.
*Private* ligipääs on kõige piiravam ligipääs ning *klassid* ja *liidesed* (*interface*) ei saa olla privaatsed. Muutujatele, mis on deklareeritud kui *private*, saab ligi teistest klassidest, kui nendes on olemas *getter*'id ja *setter*'id. Kasutades *private* nähtavust on võimalik olla kindel, et objekt peidab oma infot  välismaailma eest.

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

Kuna me ei saa teistest klassidest *Student* klassile ligi, siis kasutame kahte *public* meetodit, *getName()*
ja *setName(String name)*, et tagastada *name* väärtus või soovi korral seada see väärtus.

.. code-block:: java

  private void privateMethod() {
      System.out.println("Tere! Olen privaatne meetod!");
  }
    
Samuti saab ka meetod olla privaatne. Sel juhul tuleb arvestada sellega, et antud meetodit saab välja kutsuda ainult samas klassis, kus see meetod deklareeritud on.  

*no modifier* 
-------------

Kui ei ole eraldi deklareeritud, mis on antud meetodi, klassi või välja nähtavus, siis on nad kättesaadavad igast klassist, mis asub **samas** paketis. 

.. code-block:: java

    String version = "1.7";

    boolean processStudents() {
       return true;
    }
    
*protected* 
-----------

Muutujad, meetodid ja konstruktorid, mis on deklareeritud kui *protected*, on kättesaadavad kõikidele klassidele samas paketis või teise paketi klassidele, **juhul, kui nad laienduvad sinna klassi**. Allolev koodiplokk näitab just seda laiendumise juhtu!

- Klassid ning liidesed ei saa olla *protected*.

.. code-block:: java

     class AudioPlayer {
         
         protected boolean openSpeaker(Speaker sp) {
             // implementatsiooni detailid
         }
     }
    
     class StreamingAudioPlayer extends AudioPlayer {
        
         @Override
         boolean openSpeaker(Speaker sp) {
             // implementatsiooni detailid
         }
     }
    
Klassil *AudioPlayer* on meetod *openSpeaker()*, mida ta lubab oma alamklassil üle kirjutada. Kui *openSpeaker()* oleks *public*, siis saaks sellele ligi **kõik, kes soovivad**  või, kui oleks *private*, siis saaks sellele ligi ainult *AudioPlayer* klass. Meie eesmärgiks on aga teha meetod nähtavaks **ainult** alamklassile.

*public* 
--------

Klass, meetod, konstruktor, liides jne, mis on deklareeritud kui *public*, on kättesaadav igast teisest klassist. Kui *private* oli kõige piiravam nähtavusaste, siis *public* on vastupidiselt kõige avatum.



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
   
Selleks, et saada kätte privaatne väli *name*, kasutatakse *public* nähtavusega getName() ja setName(). Neid meetodeid on näha igast teisest klassist vaatamata paketist. 


.. code-block:: java

      public static void main(String[] arguments) {
       // ...
    }

*main()* meetod peab olema *public*, kuna vastasel juhul ei saaks Java interpretaator teda välja kutsuda, et klass tööle panna. *Public* visibility **EI** tähenda, et kindlasti peab olema ka võtmesõna *static*.
