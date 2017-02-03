.. |br| raw:: html

   <br />

Sõned
============

Sõnede võrdlus kahes keeles.

+---------------------------------------------+--------------------------------------------------+
| Python                                      | Java                                             |
+=============================================+==================================================+
| **Sõne loomine**                            |                                                  |
+---------------------------------------------+--------------------------------------------------+
| Pythonis on sõne loomiseks mitu võimalust:  |                                                  |
|                                             | Javas saab sõne luua vaid jutumärkide abil.      |
| .. code-block:: python                      |                                                  |
|                                             | .. code-block:: java                             |
|     s = "tere" # kahekordsed jutumärgid     |                                                  |
|     s = 'tere' # ühekordsed jutumärgid      |     String s = "tere";                           |
|     # kolm jutumärki                        |     String s2 = new String();                    |
|     s = """tere"""                          |                                                  |
|     s = '''tere'''                          | Reavahetust saab kasutada järgmiselt:            |
|     s = str("tere")                         |                                                  |
|                                             | .. code-block:: java                             |
| Kõik annavad sama tulemuse.                 |                                                  |
|                                             |     String s3 = "tere\bsiin\non\reavahetused";   |
| Kolme jutumärgiga eraldatud sõne |br|       |                                                  |
| korral saab sõnes kasutada ka reavahetusi.  |                                                  |
|                                             |                                                  |
| .. code-block:: python                      |                                                  |
|                                             |                                                  |
|     s = """tere                             |                                                  |
|     siin                                    |                                                  |
|     on                                      |                                                  |
|     reavahetused"""                         |                                                  |
|                                             |                                                  |
+---------------------------------------------+--------------------------------------------------+
| **Sõne ühendamine**                         |                                                  |
+---------------------------------------------+--------------------------------------------------+
| Pythonis sõne muuta ei saa. |br|            | Javas ei saa sõne samuti muuta.                  |
| "Muutmiseks" tuleb teha uus sõne. |br|      |                                                  |
| Sõnede ühendamiseks saab kasutada liitmist: | Sõnede ühendamine:                               |
|                                             |                                                  |
| .. code-block:: python                      | .. code-block:: java                             |
|                                             |                                                  |
|     s = "üks" + "teine"                     |     String s = "tere" + "tulemast";              |
|     s = "üks" + " " + "teine"               |     String s2 = "tere " + "tulemast";            |
|                                             |                                                  |
| Sõne ühendamine teist tüüpi väärtusega:     | Javas saab sõnele numbreid liita mugavamalt:     |
|                                             |                                                  |
| .. code-block:: python                      | .. code-block:: java                             |
|                                             |                                                  |
|     s = "number:" + str(nr)                 |     int nr = 3;                                  |
|                                             |     String s = "Number: " + nr;                  |
|                                             |                                                  |
+---------------------------------------------+--------------------------------------------------+
| **Sõne funktsioonid**                       |                                                  |
+---------------------------------------------+--------------------------------------------------+
|                                             | .. code-block:: java                             |
| .. code-block:: python                      |                                                  |
|                                             |     String s = "teretulemast";                   |
|     s = "teretulemast"                      |     s.substring(s.length());                     |
|     len(s) # 12                             |                                                  |
+---------------------------------------------+--------------------------------------------------+
| .. code-block:: python                      |                                                  |
|                                             | .. code-block:: java                             |
|     s = "teretulemast"                      |                                                  |
|     s[4:] # tulemast                        |     String s = "teretulemast";                   |
|     s[:4] # tere                            |     s.substring(4);                              |
|     s[5:7] # ul                             |     s.substring(0, 4);                           |
|     s[-3:] # ast                            |     s.substring(5, 7);                           |
|                                             |     s.substring(s.length() - 3);                 |
+---------------------------------------------+--------------------------------------------------+
| Pythonis üks sümbol sõnest on sõne |br|     |                                                  |
| (mille pikkus on 1):                        | Javas on üks sümbol sõnest *char* tüüpi. |br|    |
|                                             | char tüüpi väärtus kirjutatakse ühekordsete |br| |
| .. code-block:: python                      | jutumärkide (ülakomad) vahele.                   |
|                                             |                                                  |
|     s = "tere"                              | .. code-block:: java                             |
|     first = s[0] # "t"                      |                                                  |
|     c = 'a' # just a string                 |     String s = "tere";                           |
|                                             |     char first = s.charAt(0); // 't'             |
|                                             |     char c = 'a';                                |
+---------------------------------------------+--------------------------------------------------+
|                                             |                                                  |
| .. code-block:: python                      | .. code-block:: java                             |
|                                             |                                                  |
|     s = "teretulemast"                      |     String s = "teretulemast";                   |
|     s.find("tere") # 0                      |     s.indexOf("tere");                           |
|     s.find("e") # 1                         |     s.indexOf("e");                              |
|     s.find("e", 4) # 7                      |     s.indexOf("e", 4);                           |
|     s.find("o") # -1                        |     s.indexOf("o");                              |
+---------------------------------------------+--------------------------------------------------+