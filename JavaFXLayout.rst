==============
JavaFX: Layout
==============

**Layout** konteinerid ehk paanid (*panes*) võimaldavad komponente (scene graphi) sees erineval viisil paigutada. Soovitud struktuuri saamiseks võib erinevaid paane üksteise sisse panna. Kui akna suurust muudetakse, muudavad paanid automaatselt enda komponentide mõõtmeid ja paiknemist.

HBox, VBox
==========

**Hbox** ja **VBox** võimaldavad komponente paigutada üksteise kõrvale (Hbox) või üksteise alla (VBox).

StackPane
=========

**StackPane** paigutab kõik komponendid üksteise peale. Nii on võimalik näiteks kujunditest ja tekstist kokku panna ikoone.

.. image:: images/Stackpane.PNG

GridPane
========

**GridPane** loob ruudustiku, mille ruutudesse komponente paigutatakse. Meetodi **setGridLinesVisible** abil saab kuvada abijooni, mis aitavad hinnata, kas ruudustiku abil üles ehitatud paigutus näeb korrektne välja.

.. image:: images/Gridpane.PNG

FlowPane
========

**FlowPane** sarnaneb Hbox'i ja VBox'iga – ka seal paigutatakse elemente järjestikku kas horisontaalselt või vertikaalselt sõltuvalt paani orientatsioonist. Vahe on selles, et kui elemendid ei mahu kõik järjestikku, jätkab FlowPane nende paigutamist uuelt realt (või uuest veerust).

.. image:: images/Flowpane.PNG

TilePane
========

**TilePane** toimib samamoodi nagu FlowPane, kuid elemendid paigutatakse ruudustikku, kus kõik ruudud on võrdse suurusega. Ruudu suurus on vaikimisi suurima elemendi suurus, kuid seda saab eraldi määrata ka meetodi **setPrefTileWidth** abil.

.. image:: images/Tilepane.PNG

AnchorPane
==========

**AnchorPane** võimaldab komponente enda keskele, mõne serva või nurga külge ankurdada.

.. image:: images/Anchorpane.PNG

BorderPane
==========

**BorderPane** jaotab akna viieks piirkonnaks, kuhu komponente saab paigutada:

.. image:: images/Borderpane.PNG

Lisada võib nii komponente (Label, Button jne) kui ka Layout objekte.

Kasutame BorderPane'i, et ühendada mõned eelnevalt loodud Layout'id ühtseks kasutajaliideseks.