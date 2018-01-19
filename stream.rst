Stream
======

Stream ehk voog on andmete liikumise kanal. Igast kollektsioonist saab moodustada voo, mille peal on võimalik opereerida kasutades Stream API'd. Selle kasutamine suurendab loetavust ja vähendab boilerplate. Sellega kaob vajadus tsüklite järele.

Streamil on kahte tüüpi opertsioone:

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

Näited terminal operatsioonidest
--------------------------------

// TODO

-------

Java 8 Streams walkthrough/cheat sheet:

http://files.zeroturnaround.com/pdf/zt_java8_streams_cheat_sheet.pdf

Dokumentatsioon:

https://docs.oracle.com/javase/8/docs/api/java/util/stream/package-summary.html
