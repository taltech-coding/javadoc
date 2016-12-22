====================
JavaFX Event handler
====================
JavaFX-is on iga tegevus mingi notifikatsioon. Kui kasutaja vajutab mingit nuppu, klahvi, liigutab hiirt või teeb teisi tegevusi, antakse välja *evente*. Event handleritega saab nendele ligi ning lisada mingile klahvile funktsionaalsust. 

Event
-----
Event kujutab endast midagi huvipakkuvat programmile: näiteks hiire liigutamist või klahvi vajutamist. JavaFX-is on event kas *javafx.event.Event* class või mingi selle alamklass. JavaFX-is on suhteliselt palju erinevaid evente, näiteks: *DragEvent, KeyEvent, MouseEvent, ScrollEvent* ja palju teisi. On võimalik ka ise enda evente defineerida kui laiendada Event classi.

Evendi tüüpe on kolm tükki.

- KEY_PRESSED
- KEY_RELEASED
- KEY_TYPED

Koodi näide, kus tehakse nupp, mille vajutamisel prindib "Hello World": 

.. code-block:: java

	// Requires proper imports!

	public class YourApplication extends Application {
	 
	    /**
	     * @param args the command line arguments
	     */
	    public static void main(String[] args) {
	        Application.launch(args);
	    }
	    
	    @Override
	    public void start(Stage primaryStage) {
	        primaryStage.setTitle("Hello World");
	        Group root = new Group();
	        Scene scene = new Scene(root, 300, 250);
	        Button btn = new Button();
	        btn.setLayoutX(100);
	        btn.setLayoutY(80);
	        btn.setText("Hello World");

	        btn.setOnAction(new EventHandler<ActionEvent>() {
	 
	            public void handle(ActionEvent event) {
	                System.out.println("Hello World");
	            }
	        });

	        root.getChildren().add(btn);
	        primaryStage.setScene(scene);
	        primaryStage.show();
	    }
	}

Seal koodis on pikalt välja kirjutatud .setOnAction ja kuidas see töötab, kuid seda on võimalik kirjutada ka lambdaga. 

.. code-block:: java

	// Without Lambda
	btn.setOnAction(new EventHandler<ActionEvent>() 
	    public void handle(ActionEvent event) {
	        System.out.println("Hello World");
	    }
	});

.. code-block:: java

	// With Lambda (Lambdas are future)
	btn.setOnAction(event -> System.out.println("Hello World"));

Lambdadega saab kirjutada ka terveid funktsioone, mitte ainult ühte käsku, nagu järgmises koodi näites on näha. Koodis on tetrise mängu kood, kui vajutada start nuppu.

.. code-block:: java
	
	start.setOnMouseClicked(event -> {
            if (!gameStarted) {
                startGameDropTimeline();
                gameStarted = true;
            }
        });

Event handlerile hea õpetus : http://docs.oracle.com/javafx/2/events/jfxpub-events.htm
Erinevad evendid : http://docs.oracle.com/javafx/2/events/convenience_methods.htm
