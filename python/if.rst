Tingimuslause
==============

Tingimuslausega saab kontrollida, kas mingit osa koodist käivitatakse.


+-------------------------------------------------+----------------------------------------+
| Python                                          | Java                                   |
+=================================================+========================================+
| Lihtne tingimuslause                            |                                        |
+-------------------------------------------------+----------------------------------------+
|                                                 |                                        |
| .. code-block:: python                          | .. code-block:: java                   |
|                                                 |                                        |
|     if boolean_condition:                       |     if (booleanCondition) {            |
|         do_something_if_true()                  |         doSomethingIfTrue();           |
|                                                 |     }                                  |
|                                                 |                                        |
+-------------------------------------------------+----------------------------------------+
| if-else                                                                                  |
+-------------------------------------------------+----------------------------------------+
|                                                 |                                        |
| .. code-block:: python                          | .. code-block:: java                   |
|                                                 |                                        |
|     if boolean_condition:                       |     if (booleanContidion) {            |
|         do_something_if_true()                  |         doSomethingIfTrue();           |
|     else:                                       |     } else {                           |
|         do_something_else()                     |         doSomethingElse();             |
|                                                 |     }                                  |
|                                                 |                                        |
+-------------------------------------------------+----------------------------------------+
| if-elseif-else                                                                           |
+-------------------------------------------------+----------------------------------------+
|                                                 |                                         
| .. code-block:: python                          | .. code-block:: java                    
|                                                 |                                         
|     if boolean_condition:                       |     if (booleanCondition) {             
|         do_something_if_true()                  |         doSomethingIfTrue();            
|     elif some_other_condition:                  |     } else if (otherCondition) {        
|         do_some_other_stuff()                   |         doSomeOtherThing();             
|     else:                                       |     } else {                            
|         do_something_else()                     |         doSomethingElse();              
|                                                 |     }                                   
|                                                 |                                         
|                                                 | Pikem if-elseif-elseif-else             
+-------------------------------------------------+----------------------------------------+
|                                                 |                                        |
|                                                 | .. code-block:: python                 |
|                                                 |                                        |
|                                                 |     month = 2                          |
|                                                 |                                        |
|                                                 |     if month == 1:                     |
|                                                 |         month_string = "January"       |
|                                                 |     elif month == 2:                   |
|                                                 |         month_string = "February"      |
|                                                 |     elif month == 3:                   |
|                                                 |         month_string = "March"         |
|                                                 |     elif month == 4:                   |
|                                                 |         month_string = "April"         |
|                                                 |     else:                              |
|                                                 |         month_string = "Invalid month" |
|                                                 |                                        |
|                                                 |     print(month_string)                |
|                                                 |                                        |
|                                                 |                                        |
+-------------------------------------------------+----------------------------------------+
|                                                 | Tingimus                                
| .. code-block:: java                            |                                         
|                                                 |                                         
|     int month = 2;                              |                                         
|     String monthString;                         |                                         
|                                                 |                                         
|     switch (month) {                            |                                         
|         case 1:  monthString = "January";       |                                         
|             break;                              |                                         
|         case 2:  monthString = "February";      |                                         
|             break;                              |                                         
|         case 3:  monthString = "March";         |                                         
|             break;                              |                                         
|         case 4:  monthString = "April";         |                                         
|             break;                              |                                         
|         default: monthString = "Invalid month"; |                                         
|             break;                              |                                         
|     }                                           |                                         
|                                                 |                                         
|     System.out.println(monthString);            |                                         
|                                                 |                                         
|                                                 |                                         
+-------------------------------------------------+----------------------------------------+
|                                                 | :code:`a and b`                        |
+-------------------------------------------------+----------------------------------------+
| :code:`a && b`                                  | :code:`a or b`                         |
+-------------------------------------------------+----------------------------------------+
| :code:`a || b`                                  | :code:`not a`                          |
+-------------------------------------------------+----------------------------------------+
| :code:`!a`                                      | Tõeväärtus                              
+-------------------------------------------------+----------------------------------------+
|                                                 | :code:`True`                           |
+-------------------------------------------------+----------------------------------------+
| :code:`true`                                    | :code:`False`                          |
+-------------------------------------------------+----------------------------------------+
| :code:`false`                                   |                                        |
+-------------------------------------------------+----------------------------------------+




.. generated using "python3 rst_table.py if_helper.txt if.rst"