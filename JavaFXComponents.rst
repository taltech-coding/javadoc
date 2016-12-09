===================
JavaFX: komponendid
===================

(Näide, kus neid kasutatakse)

Label
=====

**Label** on võimaldab kuvada teksti. Erinevalt tekstiväljadest pole Label kasutaja poolt otse muudetav. Labelile saab külge panna ka pilte.

(pilt (figure))

.. code-block:: java

    // Tühi Label
    Label label1 = new Label();
    // Label, mis sisaldab teksti
    Label label2 = new Label("Search");
    // Label koos ikooniga
    Image image = new Image(getClass().getResourceAsStream("icon.jpg"));
    Label label3 = new Label("Search", new ImageView(image));

Kirjatüübi muutmine

.. code-block:: java

    label1.setFont(new Font("Arial", 30));

Värvi muutmine

.. code-block:: java

    label1.setTextFill(Color.web("#0076a3"));

Teksti murdmine, kui see on liiga pikk

    label1.setWrapText(true);

Nupud
=====

Button
------

(Loomine, tegevuse defineerimine)

Toggle button
-------------

(loomine

Väljad
======

Text field
----------

Password field
--------------

Valikute tegemine
=================

Radio button
------------

Checkbox
--------

Choice box
----------

Combobox
--------
