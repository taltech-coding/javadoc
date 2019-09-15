.. |br| raw:: html

   <br />

   

Sõnastik - Kujutis
==================

Kirjeldus
---------

Kujutise andmetüüp lubab hoiustada erinevaid elemente võtme - väärtuste paaridena. Javas on ka võimalik (ning rangelt soovituslik) kujutise loomisel määrata tema võtme ning väärtuste objekti tüübid.

+----------------------------------------------------------+-------------------------------------------------------------+
| Python                                                   | Java                                                        |
+==========================================================+=============================================================+
| Sõnastik                                                 | Kujutis                                                     |
+----------------------------------------------------------+-------------------------------------------------------------+
|                                                          |                                                             |
| .. code-block:: python                                   | .. code-block:: java                                        |
|                                                          |                                                             |
|     dict = {                                             |     Map dict = new Hashmap();                               |
|         key1: value1,                                    |     dict.put(key1, value1);                                 |
|         key2: value2                                     |     dict.put(key1, value1);                                 |
|     }                                                    |                                                             |
|                                                          |                                                             |
+----------------------------------------------------------+-------------------------------------------------------------+
| Elementide sisestamine                                                                                                 |
+----------------------------------------------------------+-------------------------------------------------------------+
|                                                          |                                                             |
| .. code-block:: python                                   | .. code-block:: java                                        |
|                                                          |                                                             |
|     dict = {}                                            |     Map dict = new Hashmap();                               |
|     dict["hello"] = "world"                              |     dict.put("hello", "world");                             |
|     dict["three"] = 3                                    |     dict.put("three", 3);                                   |
|                                                          |                                                             |
|     dict["hello"] # => world                             |     dict.get("hello"); // => world                          |
|                                                          |                                                             |
+----------------------------------------------------------+-------------------------------------------------------------+
| Elementide kättesaamine                                                                                                |
+----------------------------------------------------------+-------------------------------------------------------------+
|                                                          |                                                             |
| .. code-block:: python                                   | .. code-block:: java                                        |
|                                                          |                                                             |
|     dict = {                                             |     Map dict = new Hashmap();                               |
|         "hello": "world",                                |     dict.put("hello", "world");                             |
|         "three": 3                                       |     dict.put("three", 3);                                   |
|     }                                                    |                                                             |
|                                                          |     dict.get("hello"); // => world                          |
|     dict["hello"] # => world                             |                                                             |
|                                                          |                                                             |
+----------------------------------------------------------+-------------------------------------------------------------+
| Võtme-väärtuse paari eemaldamine                                                                                       |
+----------------------------------------------------------+-------------------------------------------------------------+
|                                                          |                                                             |
| .. code-block:: python                                   | .. code-block:: java                                        |
|                                                          |                                                             |
|     dict = {                                             |     Map dict = new Hashmap();                               |
|         "hello": "world",                                |     dict.put("hello", "world");                             |
|         "three": 3                                       |     dict.put("three", 3);                                   |
|     }                                                    |                                                             |
|                                                          |     dict.remove("hello");                                   |
|     del dict["hello"]                                    |                                                             |
|                                                          |                                                             |
+----------------------------------------------------------+-------------------------------------------------------------+
| Võtme olemasolu kontrollimine                                                                                          |
+----------------------------------------------------------+-------------------------------------------------------------+
|                                                          |                                                             |
| .. code-block:: python                                   | .. code-block:: java                                        |
|                                                          |                                                             |
|     dict = {                                             |     Map dict = new Hashmap();                               |
|         "hello": "world",                                |     dict.put("hello", "world");                             |
|         "three": 3                                       |     dict.put("three", 3);                                   |
|     }                                                    |                                                             |
|                                                          |     dict.containsKey("hello") // => true                    |
|     print("hello" in dict.keys()) # => True              |                                                             |
|                                                          |                                                             |
+----------------------------------------------------------+-------------------------------------------------------------+
| Objekitüüpide määramine                                                                                                |
+----------------------------------------------------------+-------------------------------------------------------------+
|                                                          |                                                             |
| Python lubab alati sõnastikku igat tüüpi objekte lisada. | .. code-block:: java                                        |
|                                                          |                                                             |
|                                                          |     Map<String, String> dict = new Hashmap();               |
|                                                          |     // dict-i saab lisada vaid String tüüpi key-value paare.|
|                                                          |     dict.put("hello", "world");                             |
|                                                          |     dict.put("three", "3");                                 |
|                                                          |                                                             |
+----------------------------------------------------------+-------------------------------------------------------------+
