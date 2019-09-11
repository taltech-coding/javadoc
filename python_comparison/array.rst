.. |br| raw:: html

   <br />

   

Järjend, massiiv
================

+----------------------------------------------------------+-------------------------------------------------------------+
| Python                                                   | Java                                                        |
+==========================================================+=============================================================+
| Järjend                                                  | Massiiv                                                     |
+----------------------------------------------------------+-------------------------------------------------------------+
| Pythonis kasutame järjendit (*list*).                    | Javas kasutame massiivi (*array*). |br|                     |
|                                                          | Javas on eraldi olemas ka järjend (*List*).                 |
+----------------------------------------------------------+-------------------------------------------------------------+
| Järjendi loomine                                         | Massiivi loomine                                            |
+----------------------------------------------------------+-------------------------------------------------------------+
|                                                          |                                                             |
| .. code-block:: python                                   | .. code-block:: java                                        |
|                                                          |                                                             |
|     lst1 = []                                            |     int[] lst1;                                             |
|     lst2 = list()                                        |     int[] lst2 = null;                                      |
|     lst3 = [1, 2, 3]                                     |     int[] lst3 = new int[10];                               |
|                                                          |     int[] lst4 = {1, 2, 3};                                 |
| lst1, lst2 - tühjad järjendid |br|                       |                                                             |
| lst3 - koosneb arvudest 1, 2, 3.                         | lst1 - algväärtustamata massiiv. |br|                       |
|                                                          | lst2 - massiivi pole loodud. |br|                           |
|                                                          | lst3 - 10-elemendile massiiv täisarvudest |br|              |
|                                                          | (vaikimisi kõik väärtused on 0). |br|                       |
|                                                          | lst4 - 3-elemendiline massiiv, kus on arvud 1, 2, 3.        |
|                                                          |                                                             |
|                                                          | lst1 puhul tuleb enne selle muutuja kasutamist see |br|     |
|                                                          | algväärtustada.                                             |
|                                                          |                                                             |
|                                                          | lst2 saab kasutada, aga kuna objekti pole, siis |br|        |
|                                                          | ühtegi massiivi meetodit/muutujat selle kaudu kätte ei saa. |
|                                                          |                                                             |
+----------------------------------------------------------+-------------------------------------------------------------+
| Elemendi andmetüüp                                                                                                     |
+----------------------------------------------------------+-------------------------------------------------------------+
| Pythonis võib järjendisse lisada suvalist tüüpi andmeid: |                                                             |
|                                                          | Javas on massiivi puhul määratud andmetüüp. |br|            |
| .. code-block:: python                                   | Massiivi saab panna vaid seda tüüpi väärtusi.               |
|                                                          |                                                             |
|     lst = [1, "tere", {}, [1, 2]]                        | .. code-block:: java                                        |
|                                                          |                                                             |
|                                                          |     int[] arr = {1, 2, 10, -1, 3};                          |
|                                                          |                                                             |
|                                                          | Muud tüüpi väärtuse lisamine annaks vea.                    |
|                                                          |                                                             |
+----------------------------------------------------------+-------------------------------------------------------------+
| Elemendi väärtustamine, lisamine                                                                                       |
+----------------------------------------------------------+-------------------------------------------------------------+
|                                                          |                                                             |
| Pythonis saab elementi väärtustada järgmiselt:           | Javas elemendi väärtustamine:                               |
|                                                          |                                                             |
| .. code-block:: python                                   | .. code-block:: java                                        |
|                                                          |                                                             |
|     lst[1] = 12                                          |     lst[1] = 12;                                            |
|                                                          |                                                             |
| Python võimaldab järjendisse elemente juurde lisada:     | Javas massiiv on lõpliku pikkusega. |br|                    |
|                                                          | Kui massiiv deklareeritakse pikkusega 10, |br|              |
| .. code-block:: python                                   | siis seda enam muuta ei saa.                                |
|                                                          |                                                             |
|     lst.append(10)                                       | Seega uue elemendi lisamist juba täidetud |br|              |
|     lst.append(11)                                       | massiivi Javas teha ei saa.                                 |
|                                                          |                                                             |
+----------------------------------------------------------+-------------------------------------------------------------+
| Järjendi pikkus                                          | Massiivi pikkus                                             |
+----------------------------------------------------------+-------------------------------------------------------------+
|                                                          |                                                             |
| Pythonis saab küsida elementide arvu järjendis:          | Javas saab küsida massiivi pikkust:                         |
|                                                          |                                                             |
| .. code-block:: python                                   | .. code-block:: java                                        |
|                                                          |                                                             |
|     lst = []                                             |     int[] lst = new int[10];                                |
|     print(len(lst)) # 0                                  |     System.out.println(lst.length); // 10                   |
|     lst.append(1)                                        |     lst[0] = 1;                                             |
|     lst.append(2)                                        |     lst[1] = 2;                                             |
|     lst.append(3)                                        |     lst[2] = 3;                                             |
|     print(len(lst)) # 3                                  |     System.out.println(lst.length); // 10                   |
|                                                          |                                                             |
|                                                          | Sõltumata sellest, mitu elementi massiivis |br|             |
|                                                          | on väärtustatud, massiivi pikkus on alati sama |br|         |
|                                                          | (see, mis deklaratsioonis märgitud).                        |
|                                                          |                                                             |
+----------------------------------------------------------+-------------------------------------------------------------+


Loe massiivi kohta siit: :doc:`../data_structures/array`.

.. generated using "python3 rst_table.py array-helper.txt array.rst"
