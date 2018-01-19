variable and primitive type
===================

Java ja Pythoni peamine vahe on see, et Python on *dynamically typed language* aga Java on
*statically typed language*. See tähendab seda, et Pythonis ei pea määrama muutujale andmetüüpi
enne koodi jooksutamist.

Javas on kahte tüüpi muutujaid: *primitive* ja *object*. Primitive tüüpi muutujaid
kasutavad vähem mälu ja on üldiselt kiiremad. Samas ei saa neid kasutada kõikides kohtades.
Kergem on võrrelda kahte *int* tüüpi muutujat, kui kahte *Integer* tüüpi.

+-----------------------------------------+------------------------------------------+
| Python                                  | Java                                     |
+=========================================+==========================================+
| Pythonis arvu loomine:                  | Javas erinevad kõik need.                |
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
| Pythonis string tüüpi muutuja loomine:  | Javas string tüüpi muutuja loomine:      |
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


Javas esinevate *primitive* muutujate vaikeväärtused:

+------------------------+---------------+
| Data Type              | Default Value |
+========================+===============+
| byte                   | 0             |
+------------------------+---------------+
| short                  | 0             |
+------------------------+---------------+
| int                    | 0             |
+------------------------+---------------+
| long                   | 0L            |
+------------------------+---------------+
| float                  | 0.0f          |
+------------------------+---------------+
| double                 | 0.0d          |
+------------------------+---------------+
| char                   | "\u0000"      |
+------------------------+---------------+
| String (or any object) | null          |
+------------------------+---------------+
| boolean                | false         |
+------------------------+---------------+


.. generated using "python3 table_generator.py PvsJava_variable.txt variable-and-primitive.rst"
