Stream
======

Stream ehk voog on andmete liikumise kanal. Igast kollektsioonist saab moodustada voo, mille peal on võimalik opereerida kasutades Stream API't. Selle kasutamine suurendab loetavust ja vähendab boilerplate. Sellega kaob vajadus tsüklite järele.

Streamil on kahte tüüpi operatsioone:

- **Intermediate** operatsioonid on laisad ja tagastavad uue striimi. Näiteks :code:`filter()` kasutamine ei hakka kohe midagi filtreerima, vaid loob uue voo. Uut voogu läbides näeb seal ainult predikaadile vastavaid ehk filtreeritud elemente.
- **Terminal** operatsioonid on entusiastlikud ja võivad voo läbi käia tekitades mingit kõrvalmõju või saades kätte mingi tulemuse. Sellised on näiteks :code:`collect()` ja :code:`sum()`. Peale terminal operatsiooni ei saa striimi enam kasutada.

Näited intermediate operatsioonidest
------------------------------------

:code:`.filter()` tagastab uue striimi, mis sisaldab ainult elemente, mis vastavad `predikaadile <https://docs.oracle.com/javase/8/docs/api/java/util/function/Predicate.html>`_. seejärel loeb :code:`.count()` kokku elementide arvu.

.. code-block:: java

	long numbersHigherThanFive = Stream.of(7, 2, 3, 5, 6)
	                .filter(n -> n > 5)
	                .count();
	        System.out.println(numbersHigherThanFive); // 2

:code:`.map()` rakendab etteantud funktsiooni igale elemendile. Vaata ka :code:`mapToInt()`, :code:`mapToLong()` ja :code:`mapToDouble()`

.. code-block:: java

    List<Integer> words = Stream.of("a", "ab", "abc")
            .map(s -> s.length()) // with method reference .map(String::length)
            .collect(Collectors.toList());

:code:`.peek()` hea vahend debug info kogumiseks jaoks.

.. code-block:: java

    List<String> names = Stream.of("Bob", "tim", "Alice")
            .filter(s -> Character.isUpperCase(s.charAt(0)))
            .peek(s -> System.out.println(s)) // with method reference .peek(System.out::println)
            .map(s -> s.toUpperCase()) // with method reference .map(String::toUpperCase)
            .collect(Collectors.toList());

:code:`.distinct()` jätab :code:`equals()` alusel alles ainult unikaalsed elemendid. :code:`.limit()` paneb piiri elementide arvule. :code:`.sorted()` sorteerib elemendid kasvavas järjestuses.

.. code-block:: java

    List<Integer> numbers = Stream.of(3, 2, 4, 4, 4, 1)
            .distinct()
            .limit(3)
            .sorted()
            .collect(Collectors.toList());


Näited terminal operatsioonidest
--------------------------------

:code:`.forEach()` opereerib igal elemendil voos sarnaselt tavalise :code:`for` loopiga.

.. code-block:: java

	Stream.of("a", "b").forEach(e -> System.out.println(e)); // .forEach(System.out::println)

:code:`.reduce()` kombineerib voo elemendid :code:`BinaryOperator` alusel.

.. code-block:: java

	int sum = IntStream.of(7, 3).reduce(0, (a, b) -> a + b);

:code:`collect()` loob voost mingi kollektsiooni (näiteks listi).

.. code-block:: java

    List<String> filtered = Stream.of("ok", "yup")
            .filter(s -> s.startsWith("o"))
            .collect(Collectors.toList());


:code:`max()` ja :code:`min()` leiavad vastavalt maksimaalse ja minimaalse väärtuse.

.. code-block:: java

    OptionalInt max = IntStream.of(6, 7, 8).max();
    OptionalInt min = IntStream.of(6, 7, 8).min();

:code:`.anyMatch()`, :code:`allMatch()`, :code:`noneMatch()` vaatavad voos vähemalt ühe elemendi, kõike elementide või mitte ühtegi elemendi vastavust predikaadile.

.. code-block:: java

    List<String> days = Arrays.asList("Saturday", "Monday", "Friday", "Sunday");

    boolean anyDayStartWithS = days.stream().anyMatch(s -> s.startsWith("S"));
    boolean allStartWithM = days.stream().allMatch(s -> s.startsWith("M"));
    boolean noneStartWithY = days.stream().noneMatch(s -> s.startsWith("Y"));

    Optional<String> anyString = days.stream().findAny();


-------

Java 8 Streams walkthrough/cheat sheet:

http://files.zeroturnaround.com/pdf/zt_java8_streams_cheat_sheet.pdf

Dokumentatsioon:

https://docs.oracle.com/javase/8/docs/api/java/util/stream/package-summary.html
