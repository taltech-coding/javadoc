Stream
======

Stream ehk voog on andmete liikumise kanal. Igast kollektsioonist saab moodustada voo, mille peal on võimalik opereerida kasutades Stream API'd. Selle kasutamine suurendab loetavust ja vähendab boilerplate. Sellega kaob vajadus tsüklite järele.

Streamil on kahe tüüpi opertsioone:
- Intermediate operatsioonid on laisad ja tagastavad uue striimi. Näiteks `filter()` kasutamine ei hakka kohe midagi filtreerima, vaid loob uue voo, mis läbi käies sisaldab ainult filtreeritud elemente.
- Terminal operatsioonid on entusiastlikud ja võivad voo läbi käia tekitades mingit kõrvalmõju või saades kätte mingi tulemuse. Sellised on näiteks Stream.forEach() ja IntStream.sum(). Peale terminal operatsiooni ei saa striimi enam kasutada.

Näited intermediate operatsioonidest
------------------------------------

// TODO

Näited terminal operatsioonidest
--------------------------------

// TODO

-------

Java 8 Streams walkthrough/cheat sheet:

http://files.zeroturnaround.com/pdf/zt_java8_streams_cheat_sheet.pdf

Dokumentatsioon:

https://docs.oracle.com/javase/8/docs/api/java/util/stream/package-summary.html
