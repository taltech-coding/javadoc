Muutuja ja primitive tüüp
===========================

Java ja Pythoni peamine vahe on see, et Python on *dynamically typed language* aga Java on
*statically typed language*. See tähendab seda, et Pythonis ei pea määrama muutujale andmetüüpi
enne koodi jooksutamist.

Javas on kahte tüüpi muutujaid: *primitive* ja *object*. Primitive tüüpi muutujaid
kasutavad vähem mälu ja on üldiselt kiiremad. Samas ei saa neid kasutada kõikides kohtades.
Kergem on võrrelda kahte *int* tüüpi muutujat, kui kahte *Integer* tüüpi.

+-----------------------------------------+------------------------------------------+
| Python                                  | Java                                     |
+=========================================+==========================================+
| Pythonis arvu loomine:                  | Javas erinevaid tüüpe arvude loomiseks:  |
|                                         |                                          |
| .. code-block:: python                  | .. code-block:: java                     |
|                                         |                                          |
|     a = 10                              |     int a = 10;                          |
|     b = 10.0                            |     double b = 10.0;                     |
|     c = 127                             |     byte c = 127;                        |
|     d = 1000;                           |     short d = 1000;                      |
|     e = 10000000000                     |     float e = 1000000000;                |
|                                         |                                          |
+-----------------------------------------+------------------------------------------+
| Pythonis sõne tüüpi muutuja loomine:    | Javas sõne tüüpi muutuja loomine:        |
|                                         |                                          |
| .. code-block:: python                  | .. code-block:: java                     |
|                                         |                                          |
|     string1 = "This is a string, "      |     String string1 = "This is a string"; |
|     string2 = 'this is also a string, ' |     String string2 = new String();       |
|     string3 = str("as is this.")        |                                          |
|                                         |                                          |
+-----------------------------------------+------------------------------------------+
| Pythonis boolean tüüpi muutuja loomine: | Javas boolean tüüpi muutuja loomine:     |
|                                         |                                          |
| .. code-block:: python                  | .. code-block:: java                     |
|                                         |                                          |
|     is_present = True                   |     boolean isPresent = true;            |
|     was_there = False                   |     boolean wasThere = false;            |
|                                         |                                          |
+-----------------------------------------+------------------------------------------+


Javas esinevate *primitive* muutujate vaikeväärtused ja min/max väärtused:

+-----------+---------------+-----------------------------------------+--------------------------------------------------------+
| Andmetüüp | Vaikeväärtus  | Minimaalne võimalik väärtus             | Maksimaalne võimalik väärtus                           |
+===========+===============+=========================================+========================================================+
| byte      | 0             | -128                                    | 127                                                    |
+-----------+---------------+-----------------------------------------+--------------------------------------------------------+
| short     | 0             | -32768                                  | 32767                                                  |
+-----------+---------------+-----------------------------------------+--------------------------------------------------------+
| int       | 0             | -2\ :sup:`-31`                          | 2\ :sup:`31`-1                                         |
+-----------+---------------+-----------------------------------------+--------------------------------------------------------+
| long      | 0L            | -2\ :sup:`63`                           | 2\ :sup:`63`-1                                         |
+-----------+---------------+-----------------------------------------+--------------------------------------------------------+
| float     | 0.0f          | 4 baiti                                 | 4 baiti                                                |
+-----------+---------------+-----------------------------------------+--------------------------------------------------------+
| double    | 0.0d          | 8 baiti                                 | 8 baiti                                                |
+-----------+---------------+-----------------------------------------+--------------------------------------------------------+
| char      | "\u0000"      | \u0000 või 0                            | \uffff või 65535                                       |
+-----------+---------------+-----------------------------------------+--------------------------------------------------------+
| boolean   | false         | puudub                                  | puudub                                                 |
+-----------+---------------+-----------------------------------------+--------------------------------------------------------+



.. generated using "python3 table-generator.py pvs-java-variable.txt variable-and-primitive.rst"
