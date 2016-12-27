*JavaFX* Baasstruktuur
======================

*JavaFX* põhitõed saab selgeks lihtsa "*Hello World*" rakenduse abil.
Allpool olev kood loob rakenduse, mis kuvab kasutajaliidese, millel on nupp, sellele vajutades prinditakse konsooli "*Hello World*", 
tegevust saab korrata mitu korda.

.. image:: https://s27.postimg.org/941g09jur/Screenshot_75.png

Oluline on meeles pidada, et klass, mis käivitab *JavaFX* rakenduse laiendab *Application* klassi,
seega peab selles klassis olema ka *start()* meetod, mis võtab endale sisendiks *Stage* objekti.
Rakendus käivitatakse *main* meetodis väljakutse *launch(args)* abil.


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


Teisi kasulikke *JavaFX* näiteid leiab lingilt:
http://docs.oracle.com/javafx/2/get_started/jfxpub-get_started.htm


