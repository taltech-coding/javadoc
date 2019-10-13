Klassid ja objektid
=====================


*Objekt* 
-----------

Oleme kursuse raames juba kasutanud objekte. *ArrayList* on näiteks klass, mille järgi luuakse objekte. Selle objekti sisuks on informatsioon, mida ta sisaldab, ning selle objekti funktsionaalsuseks on klassis *ArrayList* olevad meetodid, mille abil saab sisu, ehk olekut muuta. Toome näite, kus on kaks *ArrayList* objekti *cities* ja *countries*.

.. code-block:: java

    public static void main(String[] args) {
        ArrayList<String> cities = new ArrayList<String>();
        ArrayList<String> countries = new ArrayList<String>();
    
        countries.add("Estonia");
        countries.add("Sweden");
        countries.add("Lithuania");
    
        cities.add("Berlin");
        cities.add("Tallinn");
        cities.add("London");
        cities.add("Madrid");
    
        System.out.println("number of countries " + countries.size() );
        System.out.println("number of cities " + cities.size() );
    }    
 

Objektid *countries* ja *cities* elavad igaüks oma elu. Nad ei mõjuta üksteist mitte kuidagi. Näiteks, *countries* sisuks on sõned "Estonia", "Sweden" ja "Lithuania".

Juhul, kui kutsuda välja meetod (*näiteks countries.add("Sweden");*), siis käib objekti nimi vasakul pool punkti, mis eraldab nime ning välja kutsutavat meetodit. Kui me tahame teada, mitu sõne on *countries* sees, siis me kutsume välja meetodi *countries.size()*. 

Oleme kasutanud võtmesõna **new** juba mitmeid kordi. Näiteks *ArrayList*'i loomisel või *Scanner*'i loomisel. Põhjus on selles, et need mõlemad on klassid, mille järgi luuakse objekte. *Objektide* loomine Javas käib alati võtmesõnaga **new** (va mõned erandid).

Näiteks on erandiks sõne loomine *String* klassist. Seal ei kasuta me tavaliselt **new** võtmesõna, kuigi see on täiesti lubatud.

.. code-block:: Java

    String text = "some text";
    //Same thing as.
    String anotherText = new String("more text");
    
*Klass* 
--------

On arusaadav, et *ArrayList* (järjendi) järgi loodud objektid erinevad meeletult objektidest, mis on loodud *String* (sõne) klassist. Kõigil *ArrayList* objektidel on meetodid *add, contains, remove, size ...*, ning igal *String* objektil on meetodid *substring, length, charAt...*. *ArrayList* ja *String* loovad erinevat tüüpi objekte ning seetõttu neil on erinevad meetodid.

Kindlate objektide grupi tüübiks on klass. *ArrayList* on klass, *String* on klass, *Scanner* on klass jne. Objetid ise on klassi järgi loodud eraldiseisvad juhud, ehk isendid.

*Klass ning tema objektid* 
---------------------------

Klass defineerib, millised objektid tal on:

- Mis meetodid on objektidel.
- Millist (mis tüüpi) sisu objektidele määrata saab, ehk teisisõnu väljad, mis objekte iseloomustavad.

Nagu on juba mitmeid kordi mainitud: klass on plaan või skeem, mille järgi objekte tegema hakatakse.

Ütleme, et päris elus on meil olemas mingisuguse hoone joonis. Joonisel kujutatakse, milline hoone olema peab: milline on selle kuju, kui suur ta on jne. Koodis võib seda kirjeldada järgmiselt:

.. code-block:: Java

    public class House {
      String color;
      int sizeInSquareMeters;
      String doorColor;
     
      public House(String color, int sizeInSquareMeters, String doorColor) {
        this.color = color;
        this.sizeInSquareMeters = sizeInSquaremeters;
        this.doorColor = doorColor;
      }
    }

Maja klass ning konstruktor.

.. image:: /_images/oop_blueprint.jpg
     :width: 200px
     :height: 200px
 
   

Nüüd kui meil on joonis olemas, saab maju ehitama hakata joonise järgi. Samas on meil olemas võimalus muuta individuaalseid välju või meetodeid maja ehitades. Näiteks ütleme, millist värvi ta täpselt olema peab, millisest materjalist on katus, kui suured on uksed, jne.

.. code-block:: java

    public static void main(String[] args) {
      House myDreamHouse = new House("grey", 60, blue);

    }


Ühe maja isendi loomine objektina.

.. image:: /_images/oop_object.jpg
         :width: 200px
         :height: 100px
 







