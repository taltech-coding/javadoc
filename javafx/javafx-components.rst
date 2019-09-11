===================
JavaFX: komponendid
===================

Kasutajaliidesed koosnevad erinevatest komponentidest nagu tekstiväljad, nupud jne. Vaatame lähemalt põhilisi komponente, mida JavaFX võimaldab kasutada. Näidetest on välja jäetud kood, mis hõlmab *layout*'i loomist ja elementide lisamist sellele. Peatüki lõpus on antud suurem kasutajaliidese näide, mis kasutab **GridPane**'i, ning seda võib soovi korral kasutada mallina.

Label
=====

**Label** ehk silt võimaldab kuvada teksti. Erinevalt tekstiväljadest pole silt kasutaja poolt otse muudetav.

.. code-block:: java

    // Empty Label
    Label label1 = new Label();
    
    // Label with text
    Label label2 = new Label("Hello World");
    
    // Label with text and icon
    Image image = new Image(getClass().getResourceAsStream("search.png"));
    Label label3 = new Label("Search", new ImageView(image));
    
Tulemus:

.. image:: /_images/labels.png

Kasulikud meetodid
------------------

.. code-block:: java

    // Change text
    label1.setText("Hello World");
    
    // Change color
    label1.setTextFill(Color.BLUE);
    
    // Change font
    label1.setFont(new Font("Arial", 25));
    
    // Wrap text
    label1.setWrapText(true);
    
    // Add image
    Image img = new Image(getClass().getResourceAsStream("search.png"));
    label1.setGraphic(new ImageView(img));
    
    // Change gap between image and text
    label1.setGraphicTextGap(5.5);
    
    // Position image relative to text
    label1.setContentDisplay(ContentDisplay.TOP);

**NB!** Samu meetodeid on võimalik kasutada ka mitme järgneva komponendi puhul.

Button
======

**Button** ehk nupp on komponent, mille vajutamisel kasutaja poolt peaks käivituma mingi funktsioon.

.. code-block:: java

    Button button1 = new Button();
    Button button2 = new Button("Click here!");

    Image imageSearch = new Image(getClass().getResourceAsStream("search.png"));
    Button button3 = new Button("Cancel", new ImageView(imageSearch));

Tulemus:

.. image:: /_images/buttons.png

Nupuvajutuse töötlemine
-----------------------

.. code-block:: java

    button2.setOnAction((ActionEvent e) -> {
        button1.setText("Text!");
    });

Button klass sisaldab samuti kõiki meetodeid, mis olid eelnevalt välja toodud Label klassi juures.

Toggle button
=============

**Toggle button** ehk tumblernupp on nupp, millel on kaks olekut –  ta võib olla valitud või mitte. Selliseid nuppe saab lisada gruppidesse nii, et igas grupis võib korraga valitud olla maksimaalselt üks nupp.

.. code-block:: java

    ToggleButton tb1 = new ToggleButton();
    ToggleButton tb2 = new ToggleButton("Press me");

    Image image = new Image(getClass().getResourceAsStream("icon.png"));
    ToggleButton tb3 = new ToggleButton("Press me instead", new ImageView(image));

Tulemus:

.. image:: /_images/toggle_button.png

Ka tumblernuppude jaoks kehtivad Labeli juures kirjeldatud meetodid.

Grupi loomine
-------------

Nuppude grupi puhul saab juhtida programmi tööd vastavalt sellele, milline nupp on hetkel valitud. Valitud nupu saab kätte meetodi **getSelectedToggle** abil.

.. code-block:: java

    final ToggleGroup group = new ToggleGroup();

        ToggleButton tb1 = new ToggleButton("Button A");
        tb1.setToggleGroup(group);
        
        // Make button selected by default
        tb1.setSelected(true);

        ToggleButton tb2 = new ToggleButton("Button B");
        tb2.setToggleGroup(group);

        ToggleButton tb3 = new ToggleButton("Button C");
        tb3.setToggleGroup(group);

        Button button = new Button("Which button is pressed?");

        Label label = new Label();

        button.setOnAction((ActionEvent e) -> {
            ToggleButton pressedButton = (ToggleButton) group.getSelectedToggle();
            if (pressedButton != null) {
                label.setText(pressedButton.getText());
            } else {
                label.setText("No buttons are pressed");
            }
        });

Tulemus:

.. image:: /_images/toggle_group.png

Radio button
============

**Radio button** ehk raadionupp sarnaneb oma käitumiselt tumblernuppudele – neid kasutatakse samuti grupina, kus kasutaja peab valima vaid ühe. Erinevalt tumblernupust peab üks raadionupp grupis alati valitud olema.

.. code-block:: java

    RadioButton rb1 = new RadioButton();
    RadioButton rb2 = new RadioButton("Select me");

Tulemus:

.. image:: /_images/radio_button.png

Grupeerimine ja valiku töötlemine käib samuti ToggleGroup objekti kaudu. Kasutada saab kõiki eelpoolnimetatud meetodeid. Raadionupul pole konstruktorit, millega saab pildi lisada, kuid setGraphic meetodiga saab seda sellegipoolest teha.

Checkbox
========

**Checkbox** ehk märkeruut võimaldab üheaegselt valida rohkem kui ühe valiku grupis.

.. code-block:: java

    CheckBox cb1 = new CheckBox();
    CheckBox cb2 = new CheckBox("Box 2");

Checkboxi väärtus võib olla määratud või määramata. Selleks, et väärtus oleks algul määramata, tuleb kasutata meetodit **setIndeterminate**.

.. code-block:: java

    CheckBox cb3 = new CheckBox("Box 3");

    cb1.setAllowIndeterminate(true); // Enables the user to set indeterminate value
    cb1.setSelected(false);          // Not selected
    cb2.setIndeterminate(true);      // Undefined
    cb3.setSelected(true);           // Selected

Tulemus:

.. image:: /_images/checkbox.png

Väärtuse saab kätte, kasutades meetodit **isSelected**:

.. code-block:: java

    CheckBox checkBox = new CheckBox();
    Button button = new Button("Is the box checked?");
    Label label = new Label("");

    button.setOnAction((ActionEvent e) -> {
        if (checkBox.isSelected()) {
            label.setText("Checked");
        } else {
            label.setText("Not checked");
        }
    });

Choice box
==========

**Choice box** on lihtne *drop-down* valikute nimekiri. Lisada saab ainult teksti ning element on mõeldud kasutamiseks väiksema arvu valikute korral.

.. code-block:: java

    ChoiceBox cb = new ChoiceBox();
    cb.setItems(FXCollections.observableArrayList(
        "New Document",
        "Open ",
        new Separator(),                            // Optional element for separating groups
        "Save",
        "Save as")
    );
    
    // Alternatiivne viis elemente lisada
    cb.getItems().addAll(
        "New Document",
        "Open ",
        new Separator(),
        "Save",
        "Save as"
    );

Kasutamise demonstreerimiseks võib lisada sellise koodijupi:

.. code-block:: java

    Button button = new Button("What is the value?");
    Label label = new Label("");

    cb.setItems(FXCollections.observableArrayList(
            "New Document",
            "Open ",
            new Separator(),                            // Optional element for separating groups.
            "Save",
            "Save as")
    );

    button.setOnAction((ActionEvent e) -> {
        String chosenValue = cb.getValue().toString();
        label.setText(chosenValue);

    });

Nupu vajutamisel kuvatakse ekraanil valitud elemendi väärtus.

.. image:: /_images/choicebox.png

Combobox
========

**Combobox** ehk liitboks on samuti valikukast, kuid on pikkade nimekirjade puhul mõistlikum kui ChoiceBox.

.. code-block:: java

    final ComboBox comboBox = new ComboBox();
    comboBox.getItems().addAll(
            "Option 1",
            "Option 2",
            new Separator(),
            "Option 3"
    );

Välimuselt on ChoiceBox ja ComboBox peaaegu identsed. Kui elemente on rohkem, tekib ComboBoxile veoriba:

.. image:: /_images/combobox.png

Text field
==========

Tekstiväli võimaldab küsida kasutajalt sisendit tekstina.

.. code-block:: java

    TextField textField = new TextField();
    
    // Text field with predetermined content. Will be returned by the getText method even if user doesn't change it.
    TextField textField2 = new TextField("Your text here");

Kasulikud meetodid
------------------

.. code-block:: java

    // Get field content
    String userText = textField.getText();
    
    // Change field content
    textField.setText("Your text here");
    
    // Clear the field
    textField.clear();
    
    // Change font
    textField.setFont("Arial", 30);
    
    // Add prompt text. This text is not returned by the getText method and disappears when user starts typing.
    textField.setPromptText("Enter your first name.");

Tulemus:

.. image:: /_images/textfield.png

Password field
==============

Parooliväli erineb tavalisest tekstiväljast selle poolest, et tema sisu on varjatud. Kui me soovime enne parooli sisestamist kuvada mingit teksti, tuleb kindlasti kasutada meetodit **setPromptText**, kuna setText sisestab algteksti samuti varjatud kujul.

.. code-block:: java

    PasswordField passwordField1 = new PasswordField();
    passwordField1.setText("Your password here");        // Bad!!!!
    PasswordField passwordField2 = new PasswordField();
    passwordField2.setPromptText("Your password");       // Correct

Tulemus:

.. image:: /_images/password.png

Kõik tekstivälja meetodid töötavad samamoodi ka paroolivälja puhul.

Kasutajaliidese näidis (registreerimisvorm)
===========================================

.. image:: /_images/registration_form.png

.. code-block:: java

    import javafx.application.Application;
    import javafx.event.ActionEvent;
    import javafx.geometry.Insets;
    import javafx.scene.Group;
    import javafx.scene.Node;
    import javafx.scene.Scene;
    import javafx.scene.control.*;
    import javafx.scene.layout.GridPane;
    import javafx.scene.layout.Region;
    import javafx.stage.Stage;

    public class Main extends Application {
        public static void main(String[] args) {
            launch(args);
        }

        @Override
        public void start(Stage stage) {
            Group root = new Group();
            stage.setTitle("Registration form example");
            Scene scene = new Scene(root);

            // You can replace these components with the ones in other examples to test them
            TextField textFieldEmail = new TextField();
            PasswordField passwordField1 = new PasswordField();
            PasswordField passwordField2 = new PasswordField();
            passwordField2.setPromptText("Please retype your password");
            RadioButton radioButtonMale = new RadioButton("M");
            RadioButton radioButtonFemale = new RadioButton("F");
            ToggleGroup genderToggleGroup = new ToggleGroup();
            radioButtonFemale.setToggleGroup(genderToggleGroup);
            radioButtonMale.setToggleGroup(genderToggleGroup);
            radioButtonMale.setSelected(true);
            ChoiceBox choiceBoxUniversity = new ChoiceBox();
            choiceBoxUniversity.getItems().addAll("TTÜ", "TLÜ", "TÜ");
            Button registerButton = new Button("Register");

            CheckBox checkBoxEmailUpdates = new CheckBox("I would like to receive email updates");
            checkBoxEmailUpdates.setWrapText(true);

            GridPane grid = new GridPane();
            grid.setVgap(10);
            grid.setHgap(4);

            // If you replaced any components before, you must also replace the following lines (see JavaFX: Layouts)
            grid.add(new Label("Email: "), 0, 0);
            grid.add(textFieldEmail, 1, 0, 2, 1);
            grid.add(new Label("Password: "), 0, 1);
            grid.add(passwordField1, 1, 1, 2, 1);
            grid.add(passwordField2, 1, 2, 2, 1);
            grid.add(new Label("Gender: "), 0, 3);
            grid.add(radioButtonMale, 1, 3);
            grid.add(radioButtonFemale, 2, 3);
            grid.add(new Label("University: "), 0, 4);
            grid.add(choiceBoxUniversity, 1, 4, 2, 1);
            grid.add(checkBoxEmailUpdates, 0, 5, 3, 1);
            grid.add(registerButton, 1, 6, 2, 1);

            registerButton.setOnAction((ActionEvent e) -> {
                String userPassword = passwordField1.getText();
                if (userPassword.equals(passwordField2.getText())) {
                    String userEmail = textFieldEmail.getText();
                    String userUniversity = choiceBoxUniversity.valueProperty().getValue().toString();
                    String userGender;
                    String emailsAllowed;
                    if (radioButtonMale.isSelected()) {
                        userGender = "Male";
                    } else {
                        userGender = "Female";
                    }
                    if (checkBoxEmailUpdates.isSelected()) {
                        emailsAllowed = "emails allowed";
                    } else {
                        emailsAllowed = "emails not allowed";
                    }
                    System.out.println("User " + userEmail + " registered with password "
                            + userPassword + " (" + userGender + ", " + userUniversity + ", " + emailsAllowed + ")");
                } else {
                    grid.add(new Label("Passwords do not match!"), 0, 7, 3, 1);
                    System.out.println("Registration failed: passwords not equal");
                }
            });

            for (Node element: grid.getChildren()) {
                if (element instanceof TextField) {
                    ((Region) element).setMinWidth(300.0);
                }
            }

            root.getChildren().add(grid);
            stage.setScene(scene);
            stage.show();
        }
    }
