==============
JavaFX: Layout
==============

**Layout** konteinerid ehk paanid (*panes*) võimaldavad komponente (scene graphi) sees erineval viisil paigutada. Soovitud struktuuri saamiseks võib erinevaid paane üksteise sisse paigutada. Kui akna suurust muudetakse, tegelevad paanid automaatselt komponentide suuruse ja asukoha muutmisega.

HBox, VBox
==========

**Hbox** ja **VBox** võimaldavad komponente paigutada üksteise kõrvale (Hbox) või üksteise alla (VBox).

BorderPane
==========

**BorderPane** jaotab akna viieks piirkonnaks, kuhu komponente saab paigutada:

+--------------------------+
|           Top            |
+------+-----------+-------+
|      |           |       |
|      |           |       |
| Left |   Center  | Right |
|      |           |       |
|      |           |       |
+------+-----------+-------+
|          Bottom          |
+--------------------------+

StackPane
=========

**StackPane** paigutab kõik komponendid üksteise peale. Nii on võimalik näiteks kujunditest ja tekstist kokku panna ikoone.

GridPane
========

**GridPane** loob ruudustiku, mille ruutudesse komponente paigutatakse. Meetodi **setGridLinesVisible** abil saab kuvada abijooni, mis aitavad hinnata, kas ruudustiku abil üles ehitatud paigutus näeb korrektne välja.

FlowPane
========

**FlowPane** sarnaneb Hbox'i ja VBox'iga – ka seal paigutatakse elemente järjestikku kas horisontaalselt või vertikaalselt sõltuvalt paani orientatsioonist. Vahe on selles, et kui elemendid ei mahu kõik järjestikku, jätkab FlowPane nende paigutamist uuelt realt (või uuest veerust).

TilePane
========

**TilePane** toimib samamoodi nagu FlowPane, kuid elemendid paigutatakse ruudustikku, kus kõik ruudud on võrdse suurusega.

AnchorPane
==========

**AnchorPane** võimaldab komponente enda keskele, mõne serva või nurga külge ankurdada.