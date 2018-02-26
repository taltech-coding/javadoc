Optional
========

Kokkuvõte
----------

``Optional`` võimaldab väljendada selgelt, kas mingi väärtuse puudumine (``null``) on lubatud või mitte.

Deklareerimine:

``Optional<Person> owner``

See tähendab, et ``Person`` võib ``null`` olla (ehk puududa) selles kontekstis.

Tühi ``Optional``
""""""""""""""""""

.. code-block:: java

  Optional<Person> owner = Optional.empty();
  
Mitte-tühi
""""""""""

.. code-block:: java

  Person person = new Person("Mati", "Pärnu");
  Optional<Person> ownerOptional = Optional.of(person);
  
Väärtus võib olla ``null``
""""""""""""""""""""""""""

.. code-block:: java

  Optional<Person> ownerOptional = Optional.ofNullable(person);
  

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

Selle asemel, et tagastada ``null`` meetodis ``getPersonById``, kasutatakse ümbrist (*container*) ``Optional``. 
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
  
Viiteid
-------

https://www.callicoder.com/java-8-optional-tutorial/

http://www.oracle.com/technetwork/articles/java/java8-optional-2175753.html

http://huguesjohnson.com/programming/java/java8optional.html (kriitika ``Optional`` kasutamise osas)
