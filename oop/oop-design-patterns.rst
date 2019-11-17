Enimkasutatavad disainimustrid
==============================

Milleks vaja?
-------------
Disainimustrid on mõeldud korduvate probleemide efektiivseks lahendamiseks. Tõenäoliselt on keegi varem 
lahendanud sama probleemi mida soovid lahendada.

Disainimustrite kasutamise eelised:

- Kulub vähem aega probleemi lahendamiseks, sest keegi on disaininud selleks lahenduse, pole vaja hakata ise täiesti algusest probleemi lahendama.
- Disainimustrid on üldtundtud - rääkides inimestega, kes on disainimustritega kursis, on lihtsam seletada mida või kuidas teha, kuna ei pea seletama lahti oma eksootilist lahendust.
- Tõenäoliselt on disainimustri põhine lahendus elegantsem ja arusaadavam kui ise leiutatud lahendus.

Samas pole disainimustreid võimalik või mõistlik alati kasutada. Teatud olukordades võib see muuta koodi loetavust halvemaks, näiteks kui üritatakse kasutada mustrit
vales olukorras kus see pole kasutamiseks ette nähtud.  

Järgnevalt mõned näited enimkasutatavatest disainimustritest.

Singel (*Singleton*)
---------------------
Singli korral on klassist võimalik luua ainult üks objekt. Klassi konstruktor on privaatne ja uut objekti läbi konstruktori pole võimalik luua.
Singli objekti kasutamiseks luuakse selleks staatiline avalik meetod mille kaudu kontrollitakse, et alati on klassist ainult üks objekt.

.. code-block:: java

    public class Singleton {
        private static Singleton instance = null;
        public String value = "123";

        private Singleton() {}
    
        public static Singleton getInstance() {
            if (instance == null) {
                instance = new Singleton();
            }
            return instance;
        }
    }

    class Main {
        public static void main(String[] args) {
            Singleton newSingleton = new Singleton(); // doesn't work
            Singleton singleton = Singleton.getInstance();
            Singleton singleton2 = Singleton.getInstance();
            System.out.println(singleton.value); // 123
            System.out.println(singleton2.value); // 123
            singleton.value = "5";
            System.out.println(singleton.value); // 5
            System.out.println(singleton2.value); // 5
        }
    }

Tehase meetodid (*Static factory methods*)
------------------------------------------
Tehase meetodite muster võimaldab hoida konstruktori üleliigsest loogikast eraldatuna ehk konstruktori ülesanne on ainult uue objekti loomine. 
Lisaks võimaldavad tehase meetodite nimetused selgemalt väljendada mida luuakse võrreldes konstruktoriga kus nimetamine on piiratud. 

.. code-block:: java

    public class User {
    
        private static final Logger LOGGER = Logger.getLogger(User.class.getName());
        private final String name;
        private final String country;
    
        public User(String name, String country) {
            this.name = name;
            this.country = country;
        }
    
        public static User createWithLoggedInstantiationTime(String name, String country) {
            setLoggerProperties();
            LOGGER.log(INFO, "User created at : {0}", LocalTime.now());
            return new User(name, country);
        }
    
        public static User createWithDefaultCountry(String name) {
            return new User(name, "Poland");
        }
    
        private static void setLoggerProperties() {
            LOGGER.setLevel(ALL);
        }
    
        public static void main(String[] args) {
            User tim = createWithDefaultCountry("Tim");
            User tom = createWithLoggedInstantiationTime("Tom", "Germany");
        }
    }

Ehitaja (Builder)
-----------------
Eriotstarbeline klass teiste keerukate klasside loomiseks. Builder klass eraldab objekti loomise loogika originaalsest klassist.

Objektid võivad sisaldada palju välju, kõik ei pruugi alati olla initsialiseeritud ja seega muutub objekti
loomine keerukaks. Näiteks 10 muutujaga objekt, mida võib luua erinevates kombinatsioonides vajaks iga kombinatsiooni
loomiseks erinevat konstruktorit.

Builder on eraldiseisev klass, millele delegeeritakse objekti loomine. Builder sisaldab meetodeid
soovitud keeruka objekti väljade initsialiseerimiseks.
Erinevus tavalise *set()* meetodi ja Builderi meetodi vahel on see, et Builder tagastab meetodis iseennast,
mis teeb koodis võimalikuks kõikide Builder meetodite kokku aheldamise ühele reale.

.. code-block:: java

        public CarBuilder withEngine(Engine engine) {
            this.engine = engine;
            return this;
        }

.. code-block:: java

    CarBuilder
        ...
        .withEngine(new Engine())
        ...

Builderi meetodeid võib alustada *with* eesliitega erinevat tavapärasest *set* eesliitest,
et Builderi kasutamise tulemusena oleks kood mõistetavam.

Igas Builderis on ka *build()* meetod soovitud objekti loomiseks ja tagastamiseks, mis kutsutakse alati viimasena välja.

.. code-block:: java

    public Car build() {
        return new Car(model, name, color, country, engine, year, wheels, fuel);
    }

**Builder näide**

Car.java

.. code-block:: java

    public class Car {
        private String model;
        private String name;
        private Color color;
        private String country;
        private Engine engine;
        private Integer year;
        private Integer wheels;
        private String fuel;

        public Car(String model, String name, Color color, String country, Engine engine, Integer year, Integer wheels, String fuel) {
            this.model = model;
            this.name = name;
            this.color = color;
            this.country = country;
            this.engine = engine;
            this.year = year;
            this.wheels = wheels;
            this.fuel = fuel;
        }
        ...
        //getterid ja setterid
    }

CarBuilder.java

.. code-block:: java

    public class CarBuilder {
        private String model;
        private String name;
        private Color color;
        private String country;
        private Engine engine;
        private Integer year;
        private Integer wheels;
        private String fuel;

        public CarBuilder withModel(String model) {
            this.model = model;
            return this;
        }

        public CarBuilder withName(String name) {
            this.name = name;
            return this;
        }

        public CarBuilder withColor(Color color) {
            this.color = color;
            return this;
        }

        public CarBuilder withCountry(String country) {
            this.country = country;
            return this;
        }

        public CarBuilder withEngine(Engine engine) {
            this.engine = engine;
            return this;
        }

        public CarBuilder withYear(Integer year) {
            this.year = year;
            return this;
        }

        public CarBuilder withWheels(Integer wheels) {
            this.wheels = wheels;
            return this;
        }

        public CarBuilder withFuel(String fuel) {
            this.fuel = fuel;
            return this;
        }

        public Car build() {
            return new Car(model, name, color, country, engine, year, wheels, fuel);
        }
    }

Main.java

.. code-block:: java

    public class Main {
        public static void main(String[] args) {
            Car car = new CarBuilder()
                    .withName("Ford")
                    .withModel("Focus")
                    .withColor(Color.BLUE)
                    .withCountry("Germany")
                    .withEngine(new Engine())
                    .withYear(2019)
                    .withWheels(4)
                    .withFuel("diesel")
                    .build();
        }
    }

**Builderi loomine automaatselt IntelliJs**

IntelliJ IDE-ga on võimalik olemasolevas koodis asendada konstruktori väljakutsumine Builder klassiga.

1. Vali kursoriga koodis koht, kus kutsutakse välja konstruktor.
2. Vali menüüs **Refactor -> Replace Constructor with Builder**
3. Avatud aknast vali sobivad seaded Builder klassi loomiseks.


Strateegia (Strategy pattern)
-----------------------------
Strateegia võimaldab programmi tööajal muuta kasutatavat algoritmi (strateegiat).

.. code-block:: java

    public interface CompressionStrategy {
       void compress(List<Integer> values);
    }

    class ZipCompressionStrategy implements CompressionStrategy {
        public void compress(List<Integer> values) {
            System.out.println(values + " compressed as ZIP");
        }
    }

    class RarCompressionStrategy implements CompressionStrategy {
        public void compress(List<Integer> values) {
           System.out.println(values + " compressed as RAR");
        }
    }
    
    class CompressionContext {
        private CompressionStrategy strategy;
      
        public void setCompressionStrategy(CompressionStrategy strategy) {
           this.strategy = strategy;
        }
      
        public void createArchive(List<Integer> values) {
           strategy.compress(files);
        }
    }
    
    class Client {
        public static void main(String[] args) {
            CompressionContext context = new CompressionContext();
            context.setCompressionStrategy(new ZipCompressionStrategy());
            context.createArchive(asList(1, 2, 3)); // [1, 2, 3] compressed as ZIP
            context.setCompressionStrategy(new RarCompressionStrategy());
            context.createArchive(asList(1, 2, 3)); // [1, 2, 3] compressed as RAR
        }
    }

Olek (State pattern)
--------------------
Oleku muster delegeerib olekust sõlutvalt programmi käitumist.

.. code-block:: java


    public class Door {
        private boolean locked;
        private DoorState state;
    
        public Door(DoorState state){
            this.state = state;
        }
    
        public void execute(){
            state.execute(this);
        }
    
        public void setState(DoorState state){
            this.state = state;
        }
    
        public void setLocked(boolean locked){
            this.locked = locked;
        }
    
        public boolean isLocked(){
            return locked;
        }
    
        public static void main(String[] args) {
            Door door = new Door(new UnLockedDoorState());
            door.setState(new LockedDoorState());
            door.execute(); // door is locked
            door.setState(new UnLockedDoorState());
            door.execute(); // door is unlocked
        }
    }
    
    interface DoorState {
        void execute(Door door);
    }
    
    class LockedDoorState implements DoorState {
        public void execute(Door door){
            door.setLocked(true);
        }
    }
    
    class UnLockedDoorState implements DoorState {
        public void execute(Door door){
            door.setLocked(false);
        }
    }


Šabloonmeetod (Template pattern)
--------------------------------
Šabloonmeetod võimaldab erinevate objektide ühised meetodid defineerida üks kord ning ühes kohas, samas jättes abstraktseks meetodid mis sõltuvad objekti omadustest.

.. code-block:: java

    public abstract class Animal {
       public abstract void makeSound();
       public abstract void eat();
    
       public void doEveryday(){
          makeSound();
          eat();
       }
    
       public static void main(String[] args) {
          Animal cat = new Cat();
          Animal dog = new Dog();
          cat.doEveryday();
          dog.doEveryday();
       }
    }
    
    class Dog extends Animal {
       public void makeSound(){
          System.out.println("bark");
       }
       public void eat(){
          System.out.println("eat dog food");
       }
    }
    
    class Cat extends Animal {
       public void makeSound(){
          System.out.println("meow");
       }
       public void eat(){
          System.out.println("eat cat food");
       }
    }

Fassaad (Facade pattern)
------------------------
Peidab keerulise loogika kasutaja eest, pakkudes kasutajale lihtsustatud liidese.

.. code-block:: java

    class CPU {
        public void freeze() { }
        public void execute() { }
    }
    class HardDrive {
        public byte[] readData() {
            return new byte[]{};
        }
    }
    class Memory {
       public void loadData(byte[] data) { }
    }
    
    class ComputerFacade {
        private final CPU cpu;
        private final Memory ram;
        private final HardDrive hdd;
    
        public ComputerFacade() {
            this.cpu = new CPU();
            this.ram = new Memory();
            this.hdd = new HardDrive();
        }
    
        public void start() {
            cpu.freeze();
            ram.loadData(hdd.readData());
            cpu.execute();
        }
    }

    class Client {
        public static void main(String[] args) {
            ComputerFacade computer = new ComputerFacade();
            computer.start();
        }
    }

Adapter
-------
Kui rakenduse osad ei sobi omavahel kokku võib olla kasu Adapteri disainimustrist.
Adapteri kaudu konverteeritakse komponendi algne liides teiseks liideseks läbi vahepealse Adapter objekti.

.. code-block:: java

    public interface Vehicle {
        double getSpeed();
    }
    
    class LadaNiva implements Vehicle {
        @Override
        public double getSpeed() {
          return 56;
        }
    }
    
    interface VehicleAdapter {
        double getSpeed();
    }
    
    class VehicleAdapterImpl implements VehicleAdapter {
        private Vehicle vehicle;
    
        public VehicleAdapterImpl(Vehicle vehicle) {
            this.vehicle = vehicle;
        }
    
        @Override
        public double getSpeed() {
            return convertMphToKmh(vehicle.getSpeed());
        }
    
        private double convertMphToKmh(double mph) {
            return mph * 1.60934;
        }
    
        public static void main(String[] args) {
            Vehicle ladaNiva = new LadaNiva();
            VehicleAdapter ladaNivaAdapter = new VehicleAdapterImpl(ladaNiva);
            System.out.println(ladaNiva.getSpeed());
            System.out.println(ladaNivaAdapter.getSpeed());
        }
    }


Rohkem disainimustreid:
-----------------------
http://www.blackwasp.co.uk/gofpatterns.aspx
