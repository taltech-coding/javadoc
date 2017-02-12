Tingimuslause
==============

Tingimuslausega saab kontrollida, kas mingit osa koodist käivitatakse.


+--------------------------------+----------------------------------+
| Python                         | Java                             |
+================================+==================================+
| Lihtne tingimuslause           |                                  |
+--------------------------------+----------------------------------+
|                                |                                  |
| .. code-block:: python         | .. code-block:: java             |
|                                |                                  |
|     if boolean_condition:      |     if (booleanContidion) {      |
|         do_something_if_true() |         doSomethingIfTrue();     |
|                                |     }                            |
|                                |                                  |
+--------------------------------+----------------------------------+
| if-else                                                           |
+--------------------------------+----------------------------------+
|                                |                                  |
| .. code-block:: python         | .. code-block:: java             |
|                                |                                  |
|     if boolean_condition:      |     if (booleanContidion) {      |
|         do_something_if_true() |         doSomethingIfTrue();     |
|     else:                      |     } else {                     |
|         do_something_else()    |         doSomethingElse();       |
|                                |     }                            |
|                                |                                  |
+--------------------------------+----------------------------------+
| if-elseif-else                                                    |
+--------------------------------+----------------------------------+
|                                |                                  |
| .. code-block:: python         | .. code-block:: java             |
|                                |                                  |
|     if boolean_condition:      |     if (booleanContidion) {      |
|         do_something_if_true() |         doSomethingIfTrue();     |
|     elif bome_other_condition: |     } else if (otherCondition) { |
|         do_some_other_stuff()  |         doSomeOtherThing();      |
|     else:                      |     } else {                     |
|         do_something_else()    |         doSomethingElse();       |
|                                |     }                            |
|                                |                                  |
+--------------------------------+----------------------------------+
| Tingimus                                                          |
+--------------------------------+----------------------------------+
| :code:`a and b`                | :code:`a && b`                   |
+--------------------------------+----------------------------------+
| :code:`a or b`                 | :code:`a || b`                   |
+--------------------------------+----------------------------------+
| :code:`not a`                  | :code:`!a`                       |
+--------------------------------+----------------------------------+




.. generated using "python3 rst_table.py if_helper.txt"
