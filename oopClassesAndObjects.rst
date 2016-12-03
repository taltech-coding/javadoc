Klassid ja objektid
=====================


*Objekt* 
-----------

Oleme kursuse raames juba kasutanud objekte. *ArrayList* on näiteks klass, mille järgi luuakse objekte. Selle objekti sisuks on informatsioon, mida ta sisaldab, ning selle objekti funktsionaalsuseks on seal sisalduvad meetodid, mille abil saab sisu, ehk olekut muuta. Toome näite, kus on kaks *ArrayList* objekti *cities* ja *countries*.

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

Juhul, kui kutsuda välja meetod (*näiteks countries.add("Sweden");*), siis läheb objekti nimi vasakule poole ning punkt eraldab nime ja meetodit, mida välja kutsuti. Kui me tahame teada, mitu sõne on *countries* sees, siis me kutsume välja meetodi *countries.size()*. 

Oleme kasutanud võtmesõna **new** juba mitmeid kordi. Näiteks *ArrayList* loomisel või *Scanner* loomisel. Põhjus on selles, et need mõlemad on klassid, mille järgi luuakse objekte. *Objektide* loomine Javas käib alati võtmesõnaga **new**, mõne erandiga.

Näiteks erandiks on sõne loomine *String* klassist. Seal ei kasuta me **new** võtmesõna, kuigi see on täiesti lubatud.

 .. code-block:: Java

    String text = "some text";
    //See on sama asi!
    String anotherText = new String("more text");
    
*Klass* 
--------

On arusaadav, et *ArrayList* järgi loodud objektid erinevad meeletult objektidest, mis on loodud *String* klassist. Kõigil *ArrayList* objektidel on meetodid *add, contains, remove, size ... *, ning igal *String* objektil on meetodid *substring, length, charAt...*. *ArrayList* ja *String* loovad erinevat tüüpi objekte ning seetõttu neil on erinevad meetodid.

Kindlate objektide grupi tüübiks on klass. *ArrayList* on klass, *String* on klass, *Scanner* on klass jne. Objetid ise on klassi järgi loodud eraldiseisvad juhud, ehk isendid.

*Klass ning tema objektid* 
---------------------------

Klass defineerib, millised objektid tal on:

- Mis meetodid on objektidel.
- Mis sisu objektidel on, ehk teisisõnu väljad, mis objekte iseloomustavad.

Nagu on juba mitmeid kordi mainitud. Klass on plaan, ehk joonis, mille järgi objekte tegema hakatakse.

Ütleme, et päris elus on meil olemas mingisuguse hoone joonis. Joonisel on joonestatud, milline hoone olema peab: milline on selle kuju, kui suur ta on jne. See on meie:

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

Maja klass in konstruktor.

 .. image:: http://i.imgur.com/erKUk7I.jpg
     :width: 200px
     :height: 200px
 
   

Nüüd kui meil on joonis olemas, saab maju ehitama hakata joonise järgi. Samas on meil olemas võimalus muuta individuaalseid välju või meetodeid ehitades maja. Näiteks ütleme, millist värvi täpselt ta olema peab, millisest materjalist on katus, kui suured on uksed, jne.

.. code-block:: java

    public static void main(String[] args) {
    House myDreamHouse = new House("grey, 60, blue);

    }


Ühe maja isendi loomine objektina.

 .. image:: http://i.imgur.com/EU0ZdJ5.jpg
         :width: 200px
         :height: 100px
 







