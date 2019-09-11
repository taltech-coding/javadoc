Tingimuslause
==============

Tingimuslausega saab kontrollida, kas mingit osa koodist käivitatakse.


+----------------------------------------+-------------------------------------------------+
| Python                                 | Java                                            |
+========================================+=================================================+
| Lihtne tingimuslause                   |                                                 |
+----------------------------------------+-------------------------------------------------+
|                                        |                                                 |
| .. code-block:: python                 | .. code-block:: java                            |
|                                        |                                                 |
|     if boolean_condition:              |     if (booleanCondition) {                     |
|         do_something_if_true()         |         doSomethingIfTrue();                    |
|                                        |     }                                           |
|                                        |                                                 |
+----------------------------------------+-------------------------------------------------+
| if-else                                                                                  |
+----------------------------------------+-------------------------------------------------+
|                                        |                                                 |
| .. code-block:: python                 | .. code-block:: java                            |
|                                        |                                                 |
|     if boolean_condition:              |     if (booleanContidion) {                     |
|         do_something_if_true()         |         doSomethingIfTrue();                    |
|     else:                              |     } else {                                    |
|         do_something_else()            |         doSomethingElse();                      |
|                                        |     }                                           |
|                                        |                                                 |
+----------------------------------------+-------------------------------------------------+
| if-elseif-else                                                                           |
+----------------------------------------+-------------------------------------------------+
|                                        |                                                 |
| .. code-block:: python                 | .. code-block:: java                            |
|                                        |                                                 |
|     if boolean_condition:              |     if (booleanCondition) {                     |
|         do_something_if_true()         |         doSomethingIfTrue();                    |
|     elif some_other_condition:         |     } else if (otherCondition) {                |
|         do_some_other_stuff()          |         doSomeOtherThing();                     |
|     else:                              |     } else {                                    |
|         do_something_else()            |         doSomethingElse();                      |
|                                        |     }                                           |
|                                        |                                                 |
+----------------------------------------+-------------------------------------------------+
| Pikem if-elseif-elseif-else                                                              |
+----------------------------------------+-------------------------------------------------+
|                                        |                                                 |
| .. code-block:: python                 | .. code-block:: java                            |
|                                        |                                                 |
|     month = 2                          |     int month = 2;                              |
|                                        |     String monthString;                         |
|     if month == 1:                     |                                                 |
|         month_string = "January"       |     switch (month) {                            |
|     elif month == 2:                   |         case 1:  monthString = "January";       |
|         month_string = "February"      |             break;                              |
|     elif month == 3:                   |         case 2:  monthString = "February";      |
|         month_string = "March"         |             break;                              |
|     elif month == 4:                   |         case 3:  monthString = "March";         |
|         month_string = "April"         |             break;                              |
|     else:                              |         case 4:  monthString = "April";         |
|         month_string = "Invalid month" |             break;                              |
|                                        |         default: monthString = "Invalid month"; |
|     print(month_string)                |             break;                              |
|                                        |     }                                           |
|                                        |                                                 |
|                                        |     System.out.println(monthString);            |
|                                        |                                                 |
|                                        |                                                 |
+----------------------------------------+-------------------------------------------------+
| Ternary operator                                                                         |
+----------------------------------------+-------------------------------------------------+
| >>> "true" if True else "false"        |                                                 |
| 'true'                                 | .. code-block:: java                            |
|                                        |                                                 |
| >>> 'true' if False else 'false'       |     jshell> true ? "true" : "false"             |
| 'false'                                |     $1 ==> "true"                               |
|                                        |                                                 |
|                                        | .. code-block:: java                            |
|                                        |                                                 |
|                                        |     jshell> false ? "true" : "false"            |
|                                        |     $2 ==> "false"                              |
|                                        |                                                 |
+----------------------------------------+-------------------------------------------------+
| Tõeväärtus                                                                               |
+----------------------------------------+-------------------------------------------------+
| :code:`True`                           | :code:`true`                                    |
+----------------------------------------+-------------------------------------------------+
| :code:`False`                          | :code:`false`                                   |
+----------------------------------------+-------------------------------------------------+
| Tingimus                                                                                 |
+----------------------------------------+-------------------------------------------------+
| :code:`a and b`                        | :code:`a && b`                                  |
+----------------------------------------+-------------------------------------------------+
| :code:`a or b`                         | :code:`a || b`                                  |
+----------------------------------------+-------------------------------------------------+
| :code:`not a`                          | :code:`!a`                                      |
+----------------------------------------+-------------------------------------------------+




.. generated using "python3 rst_table.py if-helper.txt if.rst"
