===================
JavaFX: komponendid
===================

(Näide, kus neid kasutatakse)

Label
=====

**Label** võimaldab kuvada teksti. Erinevalt tekstiväljadest pole Label kasutaja poolt otse muudetav.

.. code-block:: java

    // Tühi Label
    Label label1 = new Label();
    // Label, mis sisaldab teksti
    Label label2 = new Label("Hello World");
    // Label koos ikooniga
    Image image = new Image(getClass().getResourceAsStream("search.jpg"));
    Label label3 = new Label("Search", new ImageView(image));

Kasulikud meetodid

.. code-block:: java

    // Teksti muutmine
    label1.setText("Hello World");
    // Värvi muutmine
    label1.setTextFill();
    // Kirjatüübi muutmine
    label1.setFont("Arial", 25)
    // Teksti murdmine, kui see on liiga pikk
    label1.setWrapText(true);
    // Ikooni või pildi lisamine
    label1.setGraphic(new Image(getClass().getResourceAsStream("icon.jpg")))
    // Pildi ja teksti vahelise tühimiku muutmine
    label1.setGraphicTextGap(5.5)
    // Pildi asukoha valimine teksti suhtes
    label1.setContentDisplay(ContentDisplay.TOP);

Button
======

.. code-block:: java

    Button button1 = new Button();
    Button button2 = new Button("Click here!");

    Image imageCancel = new Image(getClass().getResourceAsStream("cancel.png"));
    Button button3 = new Button("Cancel", new ImageView(imageCancel));

Nupuvajutuse töötlemise näide

.. code-block:: java

    button2.setOnAction((ActionEvent e) => {
        label.setText("Accepted");
    });

Button klass sisaldab samuti kõiki meetodeid, mis olid eelnevalt välja toodud Label klassi juures.

Toggle button
=============

*Toggle button* ehk tumblernupp on nupp, millel on kaks olekut –  ta võib olla valitud või mitte. Selliseid nuppe saab lisada gruppidesse nii, et igas grupis võib korraga valitud olla maksimaalselt üks nupp.

.. code-block:: java

    ToggleButton tb1 = new ToggleButton();
    ToggleButton tb2 = new ToggleButton("Press me");

    Image image = new Image(getClass().getResourceAsStream("icon.png"));
    ToggleButton tb3 = new ToggleButton("Press me", new ImageView(image));

Grupi loomine

.. code-block:: java

    final ToggleGroup group = new ToggleGroup();

    ToggleButton tb1 = new ToggleButton("Minor");
    tb1.setToggleGroup(group);
    tb1.setSelected(true);                         // Kui tahame, et üks oleks vaikimisi valitud

    ToggleButton tb2 = new ToggleButton("Major");
    tb2.setToggleGroup(group);

    ToggleButton tb3 = new ToggleButton("Critical");
    tb3.setToggleGroup(group);

Ka tumblernuppude jaoks kehtivad Labeli juures kirjeldatud meetodid. Lisaks saab nuppude grupi puhul juhtida programmi tööd vastavalt sellele, milline nupp on hetkel valitud:

(Kasutamise näide)

Radio button
============

Raadionupud sarnanevad oma käitumiselt tumblernuppudele, kuna neid kasutatakse samuti grupina, kus kasutaja peab valima vaid ühe. Erinevalt tumblernupust peab üks raadionupp grupis alati valitud olema.

.. code-block:: java

    RadioButton rb1 = new RadioButton();
    RadioButton rb2 = new RadioButton("Select me");

    Image image = new Image(getClass().getResourceAsStream("ok.png"));
    RadioButton rb3 = new RadioButton("Press me", new ImageView(image));

Grupeerimine ja valiku töötlemine käib sarnaselt eelnevale Toggle Group objekti kaudu. Kasutada saab kõiki eelpoolnimetatud meetodeid.

(Kasutamise näide)

Checkbox
========

**Checkbox** ehk märkeruut võimaldab üheaegselt valida rohkem kui ühe valiku grupis.

.. code-block:: java

    CheckBox cb1 = new CheckBox();
    CheckBox cb2 = new CheckBox("Second");

    Image image = new Image(getClass().getResourceAsStream("picture.jpg"));
    CheckBox tb3 = new CheckBox("Selection 1", new ImageView(image));

Checkbox'il on kaks olekut: **defined** ja **undefined**. Selleks, et olekuks määrata undefined, tuleb kasutata meetodit **setIndeterminate**.

.. code-block:: java

    cb2.setSelected(false);     // pole valitud
    cb2.setIndeterminate(true); // määramata
    cb2.setSelected(true);      // on valitud

(Kasutamise näide koos nupuga)

Choice box
==========

**Choice box** on lihtne *drop-down* valikute nimekiri. Lisada saab ainult teksti ning element on mõeldud kasutamiseks väiksema arvu valikute korral.

.. code-block:: java

    ChoiceBox cb = new ChoiceBox();
    cb.setItems(FXCollections.observableArrayList(
        "New Document",
        "Open ",
        new Separator(),                            // Valikuline element gruppide eraldamiseks
        "Save",
        "Save as")
    );
    // Alternatiivne viis elemente lisada
    cb.getItems().addAll(
        "Option 4",
        "Option 5",
        "Option 6"
    );

(kasutamise näide

Combobox
========

**Combobox** on nagu Choice box, kuid on pikkade nimekirjade puhul mõistlikum valik. Lisaks on võimalik seadistada Combobox nii, et kasutaja saab ise väärtusi lisada.

.. code-block:: java

    final ComboBox comboBox = new ComboBox();
    comboBox.getItems().addAll(
        "Option 4",
        "Option 5",
        "Option 6"
    );

(Väärtuste lisamise näide + kasutamise näide)

Text field
==========

Tekstiväli võimaldab küsida kasutajalt sisendit tekstina.

.. code-block:: java

    TextField textField = new TextField();
    // Ettemääratud sisuga tekstiväli. Seda teksti loetakse kasutaja sisendiks, kui ta seda ei muuda.
    TextField textField2 = new TextField("Your text here");

Kasulikud meetodid

.. code-block:: java

    // Sisendi lugemine
    String userText = textField.getText();
    // Teksti muutmine
    textField.setText("Your text here");
    // Välja tühjendamine
    textField.clear();
    // Kirjatüübi muutmine
    textField.setFont("Arial", 30);
    // Juhendava teksti lisamine. Seda teksti ei loeta kui kasutaja sisendit.
    textField.setPromptText("Enter your first name.");

Password field
==============

Parooliväli erineb tavalisest tekstiväljast selle poolest, et tema sisu on varjatud. Kui me soovime enne parooli sisestamist kuvada mingit teksti, tuleb kindlasti kasutada meetodit **setPromptText**, kuna setText sisestab algteksti samuti varjatud kujul.

.. code-block:: java

    PasswordField passwordField = new PasswordField();
    passwordField.setPromptText("Your password");

Kõik tekstivälja meetodid töötavad samamoodi ka paroolivälja puhul.


