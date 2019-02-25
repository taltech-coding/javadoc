Optional
========

Sissejuhatus
------------

Mõnikord tekib vajadus meetodis näidata, et tagastatav objekt võib puududa. Javas on võimalik sellisel juhul tagastada ``null`` viidet. Aga kogemus näitab, et ``null``'i tagastamine pigem suurendab vea tekkimise tõenäosust. Vanasti tagastati ``null``'i alati, kui ei saadud midagi normaalset tagastada. Aga see pigem tekitab segadust, sest ei ole võimalik aru saada, kas see ``null`` tähendab, et on tekkkinud mõni viga või väärtus tõepoolest puudub. Selline lähenemine teeb koodi halvasti loetavaks.

Tänapäeval kasutatakse hoopis teist lähenemist. Vea korral soovitatakse erindeid visata, kuna erindile saab ilmse nime anda ja soovi korral isegi mingi täpsustava sõnumi lisada. 

Enam ei soovitata tagastada ``null``'i ega kasutada seda argumendina.

**Don't pass null:** http://www.adamkoch.com/2017/08/25/dont-pass-null/

Miks ``null``'i tagastamine on halb? Võtame sellise näite:

.. code-block:: java

   public class Person {
       
       private String name;
       
       public Person(String name) {
           this.name = name;
       }
       
       public String getName() {
           return name;
       }
   
   }

Selle koodi järgi ei ole võimalik aru saada, et kas nimi puudumine on lubatud või mitte. Teistes keeltes (nt. Kotlin'is või C#'is) see probleem on lahendatud niimoodi, et on olemas ``nullable`` ja ``not nullable`` tüübid.

Näide C#'ist:

.. code-block:: c#

   private string firstName; // not-nullable
   private string? secondName; // nullable
   
   public void SomeMethod() {
       secondName = null; // ok
       firstName = null; // error
   }

Sellise lahenduse asemel tehti **alates Java versioonist 8** ``Optional`` tüüp, mida soovitatakse kasutada objekti puudumise korral.

Optional
--------

``Optional``'ist saab mõelda nagu konteinerist, kus saab olla kas 0 või 1 objekt ja selle kasutamine võimaldab väljendada selgelt, kas mingi väärtuse puudumine (``null``) on lubatud või mitte.

**Optional'i on õige kasutada ainult meetodi tagastatava tüübina.**

Õige:

.. code-block:: java

    public class Person {
        
        private String firstName;
        private String secondName;
        
        public String getFirstName() {
            return firstName;
        }
        
        public Optional<String> getSecondName() {
            return Optional.ofNullable(secondName);
        }
        
    }

See tähendab, et ``secondName`` võib ``null`` olla (ehk puududa) selles kontekstis. Nagu näete, *Optional* kasutab *List*'ile sarnast süntaksit. Te peate määrama, millist tüüpi objekt saab *Optional*'i sees olla. ``Optional<Tüüp>``

Halb:

.. code-block:: java

    public class Person {
        
        private String firstName;
        private Optional<String> secondName; // DON'T!
        
        public String getFirstName() {
            return firstName;
        }
        
        public Optional<String> getSecondName() {
            return secondName;
        }
        
    }
    
Halb:

.. code-block:: java

    public void someMethod(Optional<String> someString) { // DON'T!
    
    }
    
Kui teil on vaja näidata, et argument võib puududa, siis kasutage meetodite ülelaadimist (*overloading*).

Optional objekti loomine
------------------------

Kahjuks, kui meil meetod (nt ``getName()``) tagastab Optional tüüpi väärtuse, siis me ei saa välja ``name`` väärtust otseselt tagastada, sest välja ja meetodi tüübid on erinevad.

Näide.

.. code-block:: java

    public class Person {
        
        private String name;
        
        public Optional<String> getName() {
            return name;  // ERROR
        }
        
    }
    
Seepärast tuleb välja väärtust niiöelda *Optional*'i sisse *wrappida*. Selleks kasutatakse kolm staatilist meetodit Optional klassist:

- ``Optional.of(object)``, kus ``object`` on teie objekt, millel on sama tüüp, nagu on määratud *Optional*'ile. **NB! Saab kasutada ainult siis, kui olete 100% kindel, et objekt ei ole null!** Kui objekt saab olla ``null``, kasutage järgmist meetodit:

- ``Optional.ofNullable(object)``, kus ``object`` on teie objekt, millel on sama tüüp, nagu on määratud *Optional*'ile.

- ``Optional.empty()`` - tagastab alati tühja *Optional*'i. 

Kasutamine
----------

Kui meetod tagastab *Optional*'i, siis see on nagu hoiatus kasutajale, et objekt võib puududa ja selleks peab valmis olema.

Selleks, et kontrollida, kas *Optional* on tühi või see sisaldab objekti, tuleb kasutada ``isPresent()`` meetodit. (Alates Java 11-st on lisaks olemas meetod ``isEmpty()``).

.. code-block:: java

    Optional<String> personSecondNameOptional = person.getSecondName();
    if (personSecondNameOptional.isPresent()) {
        ...
    }
    
``get()`` meetodiga saab kätte väärtuse, mis on Optional'i sees:

.. code-block:: java

    Optional<String> personSecondNameOptional = person.getSecondName();
    if (personSecondNameOptional.isPresent()) {
        System.out.println(String.format("His/Her name is %s", personSecondNameOptional.get()));
    }
    
**NB! Kasutada get() ilma isPresent() on halb stiil!**

Saab ka kasutada funktsionaalset stiili (``ifPresent(...)`` meetod). Aga et kood oleks ilusam, soovitame kasutada ainult siis, kui käivitatakse ainult üks tegevus:

Hea:

.. code-block:: java

    person.getSecondName().ifPresent(secondName -> System.out.println(String.format("His/Her name is %s", secondName)));
    
Pigem halb:

.. code-block:: java

    person.getSecondName().ifPresent(secondName -> {
        System.out.println(String.format("His/Her name is %s", secondName));
        anotherMethodCall(secondName);
    });
    
Parem:

.. code-block:: java

   private void aMethod() {
        person.getSecondName().ifPresent(secondName -> methodWithSecondName(secondName));
        // or using method reference
        person.getSecondName().ifPresent(this::methodWithSecondName);
    }
    // ...
    
    private void methodWithSecondName(String secondName) {
        System.out.println(String.format("His/Her name is %s", secondName));
        anotherMethodCall(secondName);
    }

Miks on vaja kasutada?
-----------------------

Kujutame ette, et meil on rakendus, mis tagastab meile persooni andmed näiteks isikukoodi järgi:

.. code-block:: java

  Person getPersonById(String id) { .. }
  
Kui isikukoodiga persooni ei leita, tagastab meetod ``null``. Ja me tahame kasutada seda meetodit:

.. code-block:: java

  Person person = getPersonById("60101010111");
  System.out.println("Person name:" + person.getName());
  
Kui sellise isikukoodiga persooni ei ole, tekib ``NullPointerException``. 

Selleks, et viga vältida, peaksime enne printimist kontrollima ``person`` objekti sisu (``person != null``).

Selle asemel, et tagastada ``null`` meetodis ``getPersonById()``, kasutatakse ümbrist (*container*) ``Optional``. 
See annab meetodi kasutajale märku, et tagastatav väärtus võib olla ``null``.

.. code-block:: java

  Optional<Person> getPersonById(String id) { .. }
  
Ja nüüd saab seda kasutada nii:

.. code-block:: java

  Optional<Person> personOptional = getPersonById("60101010111");
  if (personOptional.isPresent()) {
      System.out.println("Person name:" + personOptional.get().getName());
  } else {
      System.out.println("Person does not exist!");
  }

Lisameetodid
------------

Lisaks ``isPresent()`` ja ``get()`` meetoditele, on *Optional*'il hulk teisi meetodeid:

Oletame, et meil on Optional<T>. T on mingi tüüp.

*[tagastatav tüüp]* *[meetodi nimi]* (*argumentide tüübid ja nimed*)

T orElse(T defaultObject)
"""""""""""""""""""""""""

Kui *Optional* ei ole tühi, siis tagastab selle objekti, mis on *Optional*'i sees. Muul juhul tagastab *defaultObject*'i.

.. code-block:: java

  String resolvedSecondName = person.getSecondName().orElse(""); 
  // If person.getSecondName returns non-empty Optional, then resolvedSecondName 
  // has the value from Optional, otherwise it is empty string.
  
T orElseThrow(Lambda that returns an exception)
"""""""""""""""""""""""""""""""""""""""""""""""

Kui *Optional* ei ole tühi, siis tagastab selle objekti, mis on *Optional*'i sees. Muul juhul viskab erindi.
  
.. code-block:: java

  String resolvedSecondName = person.getSecondName().orElseThrow(() -> new IllegalStateException("Second name is not specified")); 
  // If person.getSecondName returns empty Optional, then resolvedSecondName 
  // has the value from Optional, otherwise IllegalStateException is thrown.
  
T orElseThrow()
"""""""""""""""

**NB! Alates Java'st 10.**

Kui *Optional* ei ole tühi, siis tagastab selle objekti, mis on *Optional*'i sees. Muul juhul viskab NoSuchElementException erindi.

.. code-block:: java

  String resolvedSecondName = person.getSecondName().orElseThrow(); 
  // If person.getSecondName returns empty Optional, then resolvedSecondName 
  // has the value from Optional, otherwise NoSuchElementException is thrown.
  
Optional<T> filter(Predicate lambda)
""""""""""""""""""""""""""""""""""""

Filtreerib Optional'i mingi predikaadi järgi. Kui *Optional*'i sees olev objekt vastab sellele predikaadile, siis tagastatakse sama *Optional*, muul tuhul tagastatakse tühi *Optional*.

.. code-block:: java

    Optional<String> filteredSecondNameOptional = person.getSecondName()
        .filter(secondName -> secondName.startsWith("a"));
    
Kui nimi ei alga 'a' tähega, siis saame tühja Optional'i.

Optional<T2> map(Lambda)
""""""""""""""""""""""""
  
Konverteerib *Optional*'i sees oleva objekti teiseks (näiteks ka teiset tüüpi) objektiks.

.. code-block:: java

    Optional<Integer> secondNameLengthOptional = person.getSecondName()
        .map(secondName -> secondName.length());
        
Nüüd meil on *Optional*'i sees mitte sõne, vaid arv, mis on eelmise sõne pikkus. Või kui *Optional* oli tühi, siis see uus *Optional* on ka tühi.

Kombineerimine
""""""""""""""

Neid meetodeid saab kombineerida. See on näide Codera lähtekoodist:

``findEntity`` tagastab *Optional*'i.

.. code-block:: java

    public ResponseEntity<ExerciseCategory> findExerciseCategoryById(Long id) {
            return exerciseCategoryService.findEntity(id)
                    .map(ResponseEntity::ok)
                    .orElse(ResponseEntity.notFound().build());
    }

Kokkuvõte
---------

Nagu näha, annab ``Optional`` päris mitu eelist:

- võimaldab anda märku, et mõni tulemus võib puududa (n-ö ``null`` väärtus)
- peidab ära ``null`` kontrolli
- transformeerimine/teisendamine - me ei pea ``Optional`` tulemust kontrollima selleks, et filtreerida/muuta andmetüüpi vms. Ehk siis tavapäraselt oleks pidanud seal kohas alati kontrollima, kas väärtus on olemas, alles siis oleks saanud teisenduse teha.

Viiteid
-------

https://www.callicoder.com/java-8-optional-tutorial/

http://www.oracle.com/technetwork/articles/java/java8-optional-2175753.html

http://huguesjohnson.com/programming/java/java8optional.html (kriitika ``Optional`` kasutamise osas)

https://dzone.com/articles/optional-ispresent-is-bad-for-you (miks ``isPreset()`` kasutamine pole hea)
