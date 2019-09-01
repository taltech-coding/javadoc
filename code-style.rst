Koodistiil
==========

Programmeerijad on teinud teatud kokkulepped, et kiiremini aru saada võõrast koodist. Need kokkulepped moodustavad nn koodistiili.

Koodistiili juures on osa reegleid, mis ei sõltu programmeerimiskeelest, teine osa on keelespetsiifilised. Üldiste reeglite hulka kuulub näiteks nõue valida muutujate, meetodite, klasside, liideste, failide jt. objektide nimed nii, et need peegeldaksid nende otstarvet, samuti nõue teksti "treppida" jpt.

.. image:: /images/cleancode.png

Allikas: https://blog.codinghorror.com/content/images/uploads/2009/02/6a0120a85dcdae970b012877707a45970c-pi.png

----

*Checkstyle*
------------
*Checkstyle* automatiseerib Java koodi kontrollimist, et tuua esile stiilivead.

*Checkstyle* *plugin*'i lisamine *IntelliJ*-le:

Esmalt ava *IntelliJ* ning *settings* (*Windows Ctrl-Alt-s* või *Mac OS X ⌘,*). Seadete alt vali *plugins* ning selle alt *Browse repositories*. Kirjuta otsingusse "*checkstyle*" ja vali *checkstyle-IDEA*. Vali paremalt *install* ning *restart IntelliJ IDEA*. 

Mõnel kursusel on oma stiilinõuete konfiguratsioon, Java põhikursusel näiteks iti0011.xml.

Peale restarti avada uuesti *settings* ning sealt *other settings* ning *checkstyle*. Paremal ääres on roheline "+" ja sealt määrata xml faili asukoht. Seejärel panna lisatud konfiguratsiooni ette linnuke, et muuta see aktiivseks.

Nimetamine
-------------

Klasside/meetodite/muutujate nimed peaksid olema kindlasti tähenduslikud. Mitmesõnalistes identifikaatorites kirjutatakse sõnad alates teisest sõnast **suure algustähega (camelCase)**.

**Faili nimetamine** - nimetus tuleneb selles sisalduva klassi nimest. :code:`MyClass.java`

**Klasside nimetamine** - nimetus peaks olema nimisõna, lihtne ja kirjeldav, algama suure tähega. Tuleks vältida akronüümide kasutamist, välja arvatud kui seda kasutatakse laialdasemalt kui pikka vormi, näiteks HTML. :code:`class MyClass;`

**Liideste nimetamine** - nimetus algab suure algustähega, nagu klasside nimedki.  :code:`interface MyInterface;`

**Meetodite nimetamine** - nimetus peaks olema tegusõna, mis kirjutatakse väikese algustähega. :code:`doSomething();`

**Muutujate nimetamine** - nimetus algab väikese algustähega. :code:`float myWidth;`

**Konstantide nimetamine** - nimedes on kõik tähed suured, sõnad eraldatakse alakriipsuga. :code:`int MIN_WIDTH = 4;`

**Pakettide nimetamine** - nimetus on läbiva väikese tähega.


Faili struktuur
----------------

Fail koosneb:

1. Paketi deklaratsioon
2. Import laused
3. Täpselt üks kõrgema taseme klass

**Täpselt üks** tühi rida eraldab iga sektsiooni ja meetodit. Kui samas failis on mitu klassi või liidest (reeglina ei peaks sellist olukorda tekkima), siis nende vahele jäetakse vähemalt üks tühi rida. 

.. code-block:: java
  
  package program;

  import java.time.LocalDate;

  public class Main {

    public static void main(String[] args) {
        System.out.println("Date : " + LocalDate.now());
    }
  }

Vormistus
---------

Looksulge **{}** kasutatakse *if*, *else*, *for*, *do* ja *while* lausetega, isegi kui nende kehad on tühjad või sisaldavad ainult ühte lauset.

**Reavahetused**

Loogeline avav sulg kirjutatakse reeglina rea lõppu, vastav sulgev sulg on joondatud selle rea alguse järgi.

- Reavahetust ei toimu enne loogelist alustavat sulgu **{**.
- Reavahetus toimub peale loogelist alustavat sulgu.
- Reavahetus toimub enne loogelist sulgevat sulgu **}**.
- Reavahetus toimub ainult peale loogelist sulgevat sulgu siis, kui see sulg lõpetab lause või lõpetab meetodi keha, konstruktori või klassi. Näiteks peale loogelist sulgevat sulgu pole reavahetust, kui peale sulgu tuleb *else*.

Näide:

.. code-block:: java

  public class MyClass() {

    public static void method() {
        if (condition()) {
            try {
                something();
            } catch (ProblemException e) {
                recover();
            }
        } else if (otherCondition()) {
            somethingElse();
        } else {
            lastThing();
        }
    }
 }

**Tühjad blokid**

Tühjad blokid võivad olla lühikesed. Bloki võib sulgeda ( **{}** ) samal real, ilma et selle vahel oleks sümboleid või reavahetus , välja arvatud kui see on osa mitmeblokilisest lausest (sisaldab vahetult mitut blokki: *if/else* või *try/catch/finally*.

.. code-block:: java

  // This is acceptable
  void doNothing() {}

  // This is equally acceptable
  void doNothingElse() {
  }
  
  // This is not acceptable: No concise empty blocks in a multi-block statement
  try {
      doSomething();
  } catch (Exception e) {}

**Koodi treppimine**

Koodi treppimiseks kasutatakse **tühikuid**, soovitatav (minimaalne) treppimissamm on 2-4 tühikut. Trepitakse kõik juhtimisstruktuurid, klassi sisu klassi päise suhtes, meetodi sisu meetodi päise suhtes. Tabulaatori abil treppimine toob kaasa probleeme lähteteksti viimisel ühelt platvormilt teisele (pikkus võib arvutitel erineda). Treppimine kehtib nii koodile kui ka kommentaaridele blokis.

Taandeid saab koodiformaatoriga üle kontrollida (*Windows Ctrl + Alt + L* või *Mac OS Alt + ⌘ + L*).

Iga lause on eraldi real, lauset pole vaja ilma põhjuseta poolitada.

.. code-block:: java

  // Bad example
  final String value =
      someValue;

  // Good example
  final String value = someValue;
    
**Ridade murdmine**

Kui rida on liiga pikk, tuleks seda murda üldiste põhimõtete järgi:

- Peale koma
- Enne märki, sümbolit või operaatorit
- Murtud rida tuleks jätkata järgmisel real kohakuti eelmise reaga

.. code-block:: java

    function(longExpression1, longExpression2, longExpression3,
             longExpression4, longExpression5);
             
    var = function1(longExpression1,
                    function2(longExpression2,
                              longExpression3));
                              
    longName1 = longName2 * (longName3 + longName4 - longName5)
                + 4 * longname6;                            
 
**Tühikud**

Komadele ja semikoolonitele järgeb alati tühik. *if, while, for, switch* ja *catch* võtmesõnadele järgneb tühik.

.. code-block:: java

  // Bad example
  while(condition) {
      statements;
  }
  
  // Good example
  while (condition) {
      statements;
  }

Matemaatiliste operaatorite ümber tuleks kasutada tühikuid. Tühikud ei peaks eraldama juurdekasvu (++) ja alandamist (--) nende operandist.

.. code-block:: java

  // Bad example, because this offers poor visual separation of operations
  int foo=a+b+1;
  foo ++;

  // Better example
  int foo = a + b + 1;
  foo++;

**Loetavus**

Kasutamata koodi (*import* laused, meetodid, parameetrid, klassid) ei tohiks alles jätta. Tuleks ka vältida üleliigset koodi, näiteks ajutisi muutujaid.

.. code-block:: java

    // Bad example
    a = getValue();
    return a;
    
    // Better example
    return getValue();
    

Alati tuleks eelistada loetavust ja üheselt mõistetavust.

.. code-block:: java

  // Bad example
  // Depending on the font, it may be difficult to distinguish 1001 from 100l.
  long count = 100l + n;

  // Good example
  long count = 100L + n;
  
-------

https://google.github.io/styleguide/javaguide.html#s3-source-file-structure

http://www.oracle.com/technetwork/java/codeconventions-150003.pdf
