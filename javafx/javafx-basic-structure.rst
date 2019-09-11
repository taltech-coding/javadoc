*JavaFX* Baasstruktuur
======================

*JavaFX* põhitõed saab selgeks lihtsa "*Hello World*" rakenduse abil.
Allpool olev kood loob rakenduse, mis kuvab kasutajaliidese, millel on nupp, sellele vajutades prinditakse konsooli "*Hello World*", 
tegevust saab korrata mitu korda.

.. image:: /_images/javafx_helloworld_ui.png

Koodinäide
----------

.. code-block:: java

    // Necessary imports

    import javafx.application.Application;
    import javafx.scene.Scene;
    import javafx.scene.control.Button;
    import javafx.scene.layout.StackPane;
    import javafx.stage.Stage;
    
    // The Main Class extends Application

    public class Main extends Application {
    
        // The main method starts the application

        public static void main(String[] args) {
            launch(args);
        }
        
        // The Application class method start() has to be overridden
        
        @Override
        public void start(Stage primaryStage) {
        
            // A new button is created
            Button button = new Button();

            // Text is added to the previously created button
            button.setText("Click here to print 'Hello World'");
            
            // This code sets an action to said button
            // Now on a button click "Hello World" is printed to the console 
            button.setOnAction(event -> System.out.println("Hello World"));
            
            // A Pane is created
            StackPane root = new StackPane();
            
            // The button is added to the pane
            root.getChildren().add(button);
            
            // This code creates a new scene with a fixed size of 300x300 pixels
            Scene scene = new Scene(root, 300, 300);
            
            // This text is shown at the top right-hand corner of the window (stage)
            primaryStage.setTitle("Hello World");
            
            // The scene is added to the stage
            primaryStage.setScene(scene);
            
            // This code shows the created application
            primaryStage.show();
        }


    }



Olulised põhitõed
-----------------

- *JavaFX* rakenduse põhiklass laienadab *javafx.application.Application* klassi.
- *start()* meetod käivitab rakenduse, tegemist on alguspunktiga kõikides *JavaFX* rakendustes.
- *JavaFX* rakendustes defineeritakse kasutajaliides *stage*'i ning *scene*'i abil.
- *stage* klass on *JavaFX*'is kõrgeima astme konteiner/ mahuti.
- *scene* klass on aga konteiner kogu kasutajaliidese sisule.

Kuidas infot säilitatakse?
--------------------------

- *JavaFX*'is säilitatakse *scene*'i hierarhilist sisu sõlmedest (*nodes*) koosneva graafina.
- Antud näites on juursõlmeks ehk *root node*'iks *StackPane* objekt.
- Juursõlm jälgib seda, kas *stage*'i suurust muudetakse ning muudab oma suurust vastavalt sellele.
- Antud juhul on *root node*'il üks *child node* - nupp.
- Nupul on tekst ning *event handler*, mille abil prinditakse tekst konsooli, kui nuppu vajutatakse.

.. image:: /_images/javafx_helloworld_scene_graph.png


JAR fail
--------

- *JavaFX* rakendus ei vaja *main()* meetodit, kui koodist tehakse JAR fail, mille hulka kuulub ka *javaFX Launcher*.
- JAR faili loomiseks saab kasutada *JavaFX Packager* tööriista.

Lisainfo
--------

Teisi kasulikke *JavaFX* näiteid leiab lingilt:
http://docs.oracle.com/javafx/2/get_started/jfxpub-get_started.htm



