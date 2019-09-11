*JavaFX* Animatsioonid
======================

*JavaFX*'is on kaht tüüpi animatsioone:

- *transition*'id ehk üleminekud
- *timeline* ehk ajatelje animatsioonid

Nii *Timeline* kui ka *Transition* on *javafx.animation.Animation* klassi alamklassid.

*Transitions*
-------------

Üleminekud annavad võimaluse animatsioonide loomisel kasutada *JavaFX* sisest *timeline*'i. Üleminekute abil on võimalik luua mitmeid animatsioone, mis võivad oma loomult olla käivitatavad, kas paralleelselt või järjestikuliselt. 

*Fade*'i ehk hajumisega üleminek
---------------------------------

*Fade* üleminek muudab etteantud aja vältel ühe *node*'i läbipaistmatust. Antud näites luuakse punane ristkülik,
millele rakendatakse hajumisega üleminekut. Loodav *FadeTransition* kestab 3 sekundit ehk 3000 millisekundit. Selle aja vältel muudetakse meetodite *setFromValue* ning *setToValue* abil *opacity* väärtust 1 kuni 0.1. Meetod *setCycleCount* määrab mitu korda animatsiooni korratakse, antud näites tehakse seda lõpmatu arv kordi, *setAutoReverse* aga mängib animatsiooni kõigepealt nii, nagu see koodi on kirjutatud, kuid enne sama animatsiooni kordamist, tehakse läbi ka sellele üleminekule vastupidine animatsioon. Lõpuks käivitatakse *fade transition* *play()* meetodiga.

.. code-block:: java

    final Rectangle rectangle = new Rectangle(10, 10, 100, 100);
    rectangle.setFill(Color.RED);
    
    //...
    
    FadeTransition ft = new FadeTransition(Duration.millis(3000), rectangle);
    ft.setFromValue(1.0);
    ft.setToValue(0.1);
    ft.setCycleCount(Timeline.INDEFINITE);
    ft.setAutoReverse(true);
    ft.play();


*Path*'iga ehk teekonnaga üleminek
-----------------------------------

.. image:: /_images/javafx_path_transition.png

*Path*'iga üleminek liigutab graafi sõlme mööda määratud teed ühest otsast teise etteantud aja vältel. Järgnev kood liigutab oranži ümarate nurkadega ristkülikut, mööda loodud teed.

Meetodid *setArcHeight()* ning *setArcWidth()* muudavad vastavalt ristküliku nurkade vertikaal- ning horisontaaldiameetrit.
Seejärel luuakse uus *path*, meetodi *getElements().add()* abil teele lisada erinevaid omadusi, näiteks määratakse *MoveTo*'ga antud näites koordinaat, kuhu kujund liigub, ning objekt *CubicCurveTo* lisab teekonda kurvi.

Lõpuks luuakse uus *PathTransition*, mis kestab neli sekundit, sellele lisatakse *setPath()* meetodi abil eelnevalt loodud tee ning
setNode() abil oranž ristkülik. Meetod *setOrientation* määrab kuidas riskülik teel liigub, *ORTHOGONAL_TO_TANGENT* paneb ristküliku jälgima teel olevaid kurve ning vastavalt sellele muutub kujundi keskristsirge kaldenurk. Animatsiooni korratakse ka vastupidises järjekorras ning kogu tsüklit korratakse lõpmatu arv kordi.


.. code-block:: java

    final Rectangle rectangle = new Rectangle (0, 0, 40, 40);
    rectangle.setArcHeight(10);
    rectangle.setArcWidth(10);
    rectangle.setFill(Color.ORANGE);
    
    //...
    
    Path path = new Path();
    path.getElements().add(new MoveTo(20,20));
    path.getElements().add(new CubicCurveTo(380, 0, 380, 120, 200, 120));
    path.getElements().add(new CubicCurveTo(0, 120, 0, 240, 380, 240));
    
    PathTransition pathTransition = new PathTransition();
    pathTransition.setDuration(Duration.millis(4000));
    pathTransition.setPath(path);
    pathTransition.setNode(rectangle);
    pathTransition.setOrientation(PathTransition.OrientationType.ORTHOGONAL_TO_TANGENT);
    pathTransition.setCycleCount(Timeline.INDEFINITE);
    pathTransition.setAutoReverse(true);
    pathTransition.play();

Paralleelne üleminek
--------------------

.. image:: /_images/javafx_parallel_transition.png

Paralleelne üleminek paneb tööle mitu *transition*'it samaaegselt.
Meetoditega *setTranslateX()* ning *setTranslateY()* antakse tumesinisele ristkülikule ette esialgsed koordinaadid. Antud näites pannakse korraga tööle tervelt neli erinevat üleminekut, mille hulgas on ka eelnevalt vaadeldud *FadeTransition*. Lisaks sellele luuakse ka üleminekutel põhinevad animatsioonid, mis muudavad risküliku suurust (*ScaleTransition*),  asukohta (*TranslateTransition*) ning
*RotateTransition* paneb risküliku pöörlema. Selleks, et kõik erinevad üleminekud korraga tööle panna luuakse uus *ParallelTransition* objekt, millele lisatakse kõik huvipakkuvad üleminekud.


.. code-block:: java

    Rectangle rectangle = new Rectangle(10,200,50, 50);
    rectangle.setArcHeight(15);
    rectangle.setArcWidth(15);
    rectangle.setFill(Color.DARKBLUE);
    rectangle.setTranslateX(50);
    rectangle.setTranslateY(75);
    
    //...
    
        FadeTransition fadeTransition = 
            new FadeTransition(Duration.millis(3000), rectangle);
        fadeTransition.setFromValue(1.0f);
        fadeTransition.setToValue(0.3f);
        fadeTransition.setCycleCount(2);
        fadeTransition.setAutoReverse(true);
        
        TranslateTransition translateTransition =
            new TranslateTransition(Duration.millis(2000), rectangle);
        translateTransition.setFromX(50);
        translateTransition.setToX(350);
        translateTransition.setCycleCount(2);
        translateTransition.setAutoReverse(true);
        
        RotateTransition rotateTransition = 
            new RotateTransition(Duration.millis(3000), rectangle);
        rotateTransition.setByAngle(180f);
        rotateTransition.setCycleCount(4);
        rotateTransition.setAutoReverse(true);
        
        ScaleTransition scaleTransition = 
            new ScaleTransition(Duration.millis(2000), rectangle);
        scaleTransition.setToX(2f);
        scaleTransition.setToY(2f);
        scaleTransition.setCycleCount(2);
        scaleTransition.setAutoReverse(true);
        
        ParallelTransition parallelTransition = new ParallelTransition();
        parallelTransition.getChildren().addAll(
                fadeTransition,
                translateTransition,
                rotateTransition,
                scaleTransition
        );
        
        parallelTransition.setCycleCount(Timeline.INDEFINITE);
        parallelTransition.play();


Järjestikune üleminek
---------------------

Järjestikuse ehk *sequential* ülemineku korral pannakse mitu erinevat animatsiooni üksteise järel tööle, selleks tuleb luua *SequentialTransition* objekt, millele on tarvis lisada kõik *transition*'id, mida soovitakse kujundile, pildile vms rakendada. Seda illustreerib järgnev koodinäide:

.. code-block:: java

    Rectangle rectangle = new Rectangle(25,25,50,50);
    rectangle.setArcHeight(15);
    rectangle.setArcWidth(15);
    rectangle.setFill(Color.CRIMSON);
    rectangle.setTranslateX(50);
    rectangle.setTranslateY(50);

    //...

        FadeTransition fadeTransition = 
            new FadeTransition(Duration.millis(1000), rectangle);
        fadeTransition.setFromValue(1.0f);
        fadeTransition.setToValue(0.3f);
        fadeTransition.setCycleCount(1);
        fadeTransition.setAutoReverse(true);
 
        TranslateTransition translateTransition =
            new TranslateTransition(Duration.millis(2000), rectangle);
        translateTransition.setFromX(50);
        translateTransition.setToX(375);
        translateTransition.setCycleCount(1);
        translateTransition.setAutoReverse(true);
 
        RotateTransition rotateTransition = 
            new RotateTransition(Duration.millis(2000), rectangle);
        rotateTransition.setByAngle(180f);
        rotateTransition.setCycleCount(4);
        rotateTransition.setAutoReverse(true);
 
        ScaleTransition scaleTransition = 
            new ScaleTransition(Duration.millis(2000), rectangle);
        scaleTransition.setFromX(1);
        scaleTransition.setFromY(1);
        scaleTransition.setToX(2);
        scaleTransition.setToY(2);
        scaleTransition.setCycleCount(1);
        scaleTransition.setAutoReverse(true);

        SequentialTransition sequentialTransition = new SequentialTransition();
        sequentialTransition.getChildren().addAll(
            fadeTransition,
            translateTransition,
            rotateTransition,
            scaleTransition);
        sequentialTransition.setCycleCount(Timeline.INDEFINITE);
        sequentialTransition.setAutoReverse(true);

        sequentialTransition.play();



*Timeline* animatsioonid
------------------------

.. image:: /_images/javafx_timeline.png

Animatsioone iseloomustab objektide omaduste, näiteks suuruse, asukoha ning värvi muutumine ajas. *Timeline*'i abil saab neid omadusi muuta erinevatel ajahetkedel vastavalt enda soovidele. *JavaFX* toetab ka *key frame* animatsiooni, mis lubab määrata alg- ning lõppkaadri, millel on kindlad ajahetked, nende kahe staadiumi vahele jäävaid olulisi kaadreid on samuti võimalik deklareerida, selle alusel saab automaatselt kuvada animatsioone, mida võib vastavalt enda tahtele, kas peatada, uuesti käivitada, panna tööle vastupidises suunas või korrata.
Järgnevas koodinäites on *timeline*, mille abil animeeritakse punase ristküliku liikumist kahesaja piksli võrra paremale, animatsiooni kestuseks on 500 millisekundit.

.. code-block:: java

    final Rectangle rectangle = new Rectangle(100, 50, 100, 50);
    rectangle.setFill(Color.RED);
        
    //...
    
    final Timeline timeline = new Timeline();
    timeline.setCycleCount(Timeline.INDEFINITE);
    timeline.setAutoReverse(true);
    final KeyValue kv = new KeyValue(rectangle.xProperty(), 300);
    final KeyFrame kf = new KeyFrame(Duration.millis(500), kv);
    timeline.getKeyFrames().add(kf);
    timeline.play();

``Timeline`` objekti võib kasutada ka selleks, et peals teatud aja möödumist käivitada mingi kood. Selleks saab kasutada ``KeyValue`` asemel meetodit, mis käivitatakse peale aja lõppedes:

.. code-block:: java

    Timeline timeline = new Timeline();
    timeline.getKeyFrames().add(
            new KeyFrame(
                    Duration.millis(1000),
                    event -> {
                        System.out.println("Another second has passed");
                    }
            )
    );
    timeline.setCycleCount(Timeline.INDEFINITE);
    timeline.play();

Eelnev näide prindib iga sekundi tagant välja vastava teksti.
