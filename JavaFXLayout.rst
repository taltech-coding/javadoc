==============
JavaFX: Layout
==============

**Layout** konteinerid ehk paanid (*panes*) võimaldavad komponente (scene graphi) sees erineval viisil paigutada. Soovitud struktuuri saamiseks võib erinevaid paane üksteise sisse panna. Kui akna suurust muudetakse, muudavad paanid automaatselt enda komponentide mõõtmeid ja paiknemist.

HBox, VBox
==========

**Hbox** ja **VBox** võimaldavad komponente paigutada üksteise kõrvale (Hbox) või üksteise alla (VBox).

.. code-block:: java

    Label sudokuLabel = new Label("Sudoku");
    Button startButton = new Button("Start");

    startButton.setPrefWidth(150);
    sudokuLabel.setFont(new Font("SegoeUI", 20));

    HBox hbox = new HBox();
    // Hbox hbox = new HBox(sudokuLabel, startButton);
    hbox.getChildren().addAll(sudokuLabel, startButton);

    hbox.setPadding(new Insets(10, 10, 10, 10));
    hbox.setSpacing(15);

.. image:: images/Hbox.PNG

.. code-block:: java

    Label crosswordsLabel = new Label("Crosswords");
    Label memoryLabel = new Label("Memory");

    crosswordsLabel.setFont(new Font("SegoeUI", 15));
    memoryLabel.setFont(new Font("SegoeUI", 15));

    VBox vbox = new VBox(crosswordsLabel, memoryLabel);

    vbox.setPadding(new Insets(10, 10, 10, 10));
    vbox.setPrefWidth(150);
    vbox.setSpacing(5);

    vbox.setAlignment(Pos.CENTER);

    group.getChildren().add(vbox);

.. image:: images/Vbox.PNG

GridPane
========

**GridPane** loob ruudustiku, mille ruutudesse komponente paigutatakse. Meetodi **setGridLinesVisible** abil saab kuvada abijooni, mis aitavad hinnata, kas ruudustiku abil üles ehitatud paigutus näeb korrektne välja.

.. code-block:: java

    Label highScoreLabel = new Label("High scores");
    highScoreLabel.setFont(new Font("SegoeUI", 20));

    HashMap<String, Integer> times = new HashMap<>();
    times.put("Peeter Paan", 390);
    times.put("Pipi Pikksukk", 235);

    GridPane gridPane = new GridPane();
    gridPane.setPadding(new Insets(10, 10, 10, 10));
    gridPane.setVgap(5);
    gridPane.setHgap(10);

    gridPane.add(highScoreLabel, 0, 0, 2, 1);

    int row = 1;
    for (String name: times.keySet()) {
        gridPane.add(new Label(name), 0, row);
        String scoreString = times.get(name).toString();
        gridPane.add(new Label(scoreString), 1, row);
        row++;
    }

.. image:: images/Gridpane.PNG


FlowPane
========

**FlowPane** sarnaneb Hbox'i ja VBox'iga – ka seal paigutatakse elemente järjestikku kas horisontaalselt või vertikaalselt sõltuvalt paani orientatsioonist. Vahe on selles, et kui elemendid ei mahu kõik järjestikku, jätkab FlowPane nende paigutamist uuelt realt (või uuest veerust).

.. code-block:: java

    FlowPane flowPane = new FlowPane();
    flowPane.setPrefWidth(200);
    // Add some images
    for (int i = 0; i < 9; i++) {
        ImageView img = new ImageView(new Image(getClass().getResourceAsStream("smallyellowbox.png")));
        flowPane.getChildren().add(img);
        ImageView img2 = new ImageView(new Image(getClass().getResourceAsStream("bigredbox.png")));
        flowPane.getChildren().add(img2);
    }

.. image:: images/Flowpane.PNG

TilePane
========

**TilePane** toimib samamoodi nagu FlowPane, kuid elemendid paigutatakse ruudustikku, kus kõik ruudud on võrdse suurusega. Ruudu suurus on vaikimisi suurima elemendi suurus, kuid seda saab eraldi määrata ka meetodi **setPrefTileWidth** abil.

.. code-block:: java

    TilePane tilePane = new TilePane();

   //tilePane.setPrefTileHeight(50);
   //tilePane.setPrefTileWidth(50);

    tilePane.setPrefWidth(200);


    for (int i = 0; i < 9; i++) {
        ImageView img = new ImageView(new Image(getClass().getResourceAsStream("smallyellowbox.png")));
        tilePane.getChildren().add(img);
        ImageView img2 = new ImageView(new Image(getClass().getResourceAsStream("bigredbox.png")));
        tilePane.getChildren().add(img2);
    }

   // tilePane.setPrefColumns(3);

.. image:: images/Tilepane.PNG

StackPane
=========

**StackPane** paigutab kõik komponendid üksteise peale. Nii on võimalik näiteks kujunditest ja tekstist kokku panna ikoone.

.. code-block:: java

    StackPane stackPane = new StackPane();
    // Smiley icon
    ImageView icon = new ImageView(new Image(getClass().getResourceAsStream("icon.png")));
    // Use yellow box image as the background
    ImageView iconBackground = new ImageView(new Image(getClass().getResourceAsStream("smallyellowbox.png")));
    // Add background first because otherwise the smiley will be hidden underneath it
    stackPane.getChildren().addAll(iconBackground, icon);
    stackPane.setPadding(new Insets(10, 10, 10, 10));

    group.getChildren().addAll(stackPane);

.. image:: images/Stackpane.PNG

AnchorPane
==========

**AnchorPane** võimaldab komponente enda keskele, mõne serva või nurga külge ankurdada.

.. code-block:: java

    Label timeLabel = new Label("00:00");
    timeLabel.setFont(new Font("SegoeUI", 12));

    AnchorPane anchorPane = new AnchorPane();
    anchorPane.setPrefSize(300, 200);
    anchorPane.getChildren().add(timeLabel);

    AnchorPane.setBottomAnchor(timeLabel, 8.0);
    AnchorPane.setRightAnchor(timeLabel, 8.0);

.. image:: images/Anchorpane.PNG

BorderPane
==========

**BorderPane** jaotab akna viieks piirkonnaks, kuhu komponente saab paigutada:

.. image:: images/Borderpane.PNG

Lisada võib nii komponente (Label, Button jne) kui ka Layout objekte.

Kasutame BorderPane'i, et ühendada mõned eelnevalt loodud Layout'id ühtseks kasutajaliideseks.