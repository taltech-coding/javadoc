Builder klass
================================================
-----------------------------------------------------------------------------------------
Eriotstarbeline klass teiste keerukate klasside loomiseks
-----------------------------------------------------------------------------------------
Builder klass eraldab objekti loomise loogika originaalsest klassist.

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
-----------------------

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
---------------------------------------------

IntelliJ IDE-ga on võimalik olemasolevas koodis asendada konstruktori väljakutsumine Builder klassiga.

1. Vali kursoriga koodis koht, kus kutsutakse välja konstruktor.
2. Vali menüüs **Refactor -> Replace Constructor with Builder**
3. Avatud aknast vali sobivad seaded Builder klassi loomiseks.