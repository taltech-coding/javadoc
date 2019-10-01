SOLID
=====

SOLID on 5 objekt-orienteeritud programmeerimise printsiipi, mis aitavad kirjutada koodi, mis on kergemini hallatav ja laiendatav.
Iga täht selles lühendis tähistab ühte printsiipi:

- **S** The Single-Responsibility Principle
- **O** The Open/Closed Principle
- **L** The Liskov Substitution Principle
- **I** The Interface-Segregation Principle
- **D** The Dependency-Inversion Principle

The Single-Responsibility Principle
-----------------------------------

*A class should have only one reason to change.*

Ühel klassil peaks olema üks konkreetne ülesanne.

The Open/Closed Principle
-------------------------

*Entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.*

Klassid tuleb struktureerida selliselt, et neid saab uue funktsionaalsuse vajadusel mugavalt laiendada (*open for extensions*). 
Samas seda osa koodist, mis on juba kirjutatud, ei tohiks kunagi muuta (välja arvatud vigade parandamiseks) (*closed for modifications*).

The Liskov Substitution Principle
---------------------------------

*Child classes should never break the parent class type definitions.*

Alamklassid tuleb kirjeldada nii, et objekti kasutaja jaoks ei ole vahet, kui kasutusse antakse alamklassi tüüpi objekt.
Kui alamklass teeb midagi sellist, mida ülemklassist ei eeldaks, siis see on selle printsiibi rikkumine.

The Interface-Segregation Principle
-----------------------------------

*No client should be forced to depend on methods it does not use.*

Liidese kasutaja ei pea sõltuma meetoditest, mida otseselt vaja ei lähe. Liidesed, kus on palju meetodeid, jagatakse väiksemateks.

The Dependency-Inversion Principle
-----------------------------------

*High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend upon details. Details should depend upon abstractions.*

Tarkvarakomponendid peaksid sõltuma abstraktsioonidest, mitte konkreetsetest klassidest.

Viiteid
-------

`https://en.wikipedia.org/wiki/SOLID_(object-oriented_design) <https://en.wikipedia.org/wiki/SOLID_(object-oriented_design)>`_

https://vimeo.com/111041651

Koodinäiteid:

https://github.com/mikeknep/SOLID

https://github.com/bsferreira/solid
