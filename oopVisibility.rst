OOP: nähtavus (private, protected, public, tühi)
================================================
-----------------------------------------------------------------------------------------
*Nähtavuse modifikaatorid võimaldavad määrata klassi ning selle klassi väljade nähtavust*
-----------------------------------------------------------------------------------------

Ülevaateliselt näitab allolev tabel erinevate modifikaatorite mõju kaugust. 

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
*Private* ligipääs on kõige piiravam ligipääs ning klassid ja liidesed ei saa olla *private*. Muutujatele, mis on deklareeritud, kui *private* saab ligi teistest klassidest, kui on klassis on olemas *getterid* ja *setterid*. Kasutades *private* nähtavust on võimalik olla kindel, et objekt peidab oma infot muust maailmast.

.. code-block:: java

  public class Student {
   private String name;

   public String getName() {
      return this.name;
   }

   public void setName(String name) {
      this.name = name;
   }}

Kuna me ei saaks teistest klassidest klassile *Student* ligi, siis kasutame kahte *public* meetodit, *getName()*
ja *setName(String name)*, et tagastada *name* väärtus, või seada see.

*no modifier* 
-------------

Kui ei ole eraldi deklareeritud, mis on ainut meetodi, klassi, välja nähtavus, siis on nad kättesaadavad igast klassist, mis asub samas paketis. 

.. code-block:: java

    String version = "1.7";

    boolean processStudents() {
       return true;
    }
    
*protected* 
-----------

Muutujad, meetoid ja konstruktorid, mis on deklareeritud, kui *protected* on kättesaadavad kõikidele klassidele samas paketis, või teise paketi klassidele, juhul, kui nad laienduvad sinna klassi.

Klassid ning liidesed ei saa olla *protected*.

.. code-block:: java

         class AudioPlayer {
       protected boolean openSpeaker(Speaker sp) {
          // implementation details
       }
    }
    
        class StreamingAudioPlayer extends AudioPlayer {
        @Override
        boolean openSpeaker(Speaker sp) {
              // implementation details
           }
        }
    
Klassil *AudioPlayer* on meetod *openSpeaker()*, mida ta lubab oma alamklassil üle kirjutada. Kui *openSpeaker()* oleks *public*, siis saaks sellele ligi kõik või, kui oleks *private*, siis saaks sellele ligi ainult *AudioPlayer* klass. Meie eesmärgiks on aga teha meetod nähtavaks ainult alamklassile.

*public* 
--------

Klass, meetod, konstruktor, liides jne, mis on deklareeritud, kui *public* on kättesaadav igast teisest klassist.



.. code-block:: java

      public static void main(String[] arguments) {
       // ...
    }

*main()* meetod peab olema *public*, kuna vastasel juhul ei saaks Java interpretaator teda välja kutsuda, et klass tööle panna.
