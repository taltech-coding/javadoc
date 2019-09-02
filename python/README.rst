Pythoni võrdlustabelid
======================

Selles kasutas on lehed, kus võrreldakse kõrvuti Pythoni ja Java koodi. Kuna RST-formaadis on tabeli tegemine kergelt öeldes ebamugav, 
siis selleks on kaustas üks skript. Sellele saab ette anda natuke mugavamal kujul tabeli sisu ning see genereerib korrektse RST.

Käivitamine:

``python3 rst_table.py sisend.txt väljund.rst``

Sisendi kirjeldus
-----------------

Sisend üldiselt on tavaline RST. Tabeli lahtrid määratakse järgmiselt:

``.---`` tabeli algus

``===`` päise lahtri lõpp

``---`` tavalise lahtri lõpp

``---.`` tabeli lõpp

Näiteks
-------

Näited on siinsamas kaustas ``example-helper.txt`` ja ``example.rst``.

``example-helper.txt``:

::

    Lehe päis
    =========
    
    .---
    Python
    ===
    Java
    ===
    Pythoni kohta tekst
    ---
    Java kohta tekst
    ---
    Veel Pythoni kohta tekst
    
    .. code-block:: python
    
        def fun(tion):
            return 2
            
    ---
    Java koodinäide
    
    .. code-block:: java
    
        System.out.println("why so much trouble with print()?");
    ---.
    
    Peale tabelit saab veel mingi teksti panna, näiteks *siin* ja **siin**
    
Käivitame järgmise käsu:

``python3 rst_table.py example-helper.txt example.rst``

Tulemus. ``example.rst``:

:: 

    Lehe päis
    =========

    +--------------------------+--------------------------------------------------------------+
    | Python                   | Java                                                         |
    +==========================+==============================================================+
    | Pythoni kohta tekst      | Java kohta tekst                                             |
    +--------------------------+--------------------------------------------------------------+
    | Veel Pythoni kohta tekst | Java koodinäide                                              |
    |                          |                                                              |
    | .. code-block:: python   | .. code-block:: java                                         |
    |                          |                                                              |
    |     def fun(tion):       |     System.out.println("why so much trouble with print()?"); |
    |         return 2         |                                                              |
    |                          |                                                              |
    +--------------------------+--------------------------------------------------------------+


    Peale tabelit saab veel mingi teksti panna, näiteks *siin* ja **siin**

    .. generated using "python3 rst_table.py example-helper.txt example.rst"
    
Formaaditud kujul:

Lehe päis
=========

+--------------------------+--------------------------------------------------------------+
| Python                   | Java                                                         |
+==========================+==============================================================+
| Pythoni kohta tekst      | Java kohta tekst                                             |
+--------------------------+--------------------------------------------------------------+
| Veel Pythoni kohta tekst | Java koodinäide                                              |
|                          |                                                              |
| .. code-block:: python   | .. code-block:: java                                         |
|                          |                                                              |
|     def fun(tion):       |     System.out.println("why so much trouble with print()?"); |
|         return 2         |                                                              |
|                          |                                                              |
+--------------------------+--------------------------------------------------------------+


Peale tabelit saab veel mingi teksti panna, näiteks *siin* ja **siin**

.. generated using "python3 rst_table.py example-helper.txt example.rst"
