========================
Java projekti ülesehitus
========================

Kirjeldus
---------

Java projekt koonseb tüüpiliselt ühest kaustast, kus asub java lähtekood. Organiseerimise mõttes ei asu aga lähtekood otse *src* kaustas, vaid nad paigutatakse eraldi pakettidesse (kaustadesse), mis seovad sarnase käitumismustriga klasse.

Näide
-----

.. image:: /_images/project_structure.png

Antud projektis on 2 paketti ja 4 klassi. *Animal* paketis on loomade klassid (sinna saab neid ka lisada) ning *person* paketis asub inimese klass. *Main* klassi kasutame koodi jooksutamiseks.
Näeme, et *Main* klass ei paikne paketis. Väikeste projektide puhul on see OK, kuid üldjuhul peetakse seda halvaks harjumuseks. Kood peaks ikkagi jagunema pakettideks, millest igaühe nimi on unikaalne. Antud näites võiks *Main* klass paikneda näiteks paketis nimega *main*.

.. code-block:: java

    package animal;

    import person.Person;

    public class Animal {

        private String name;
        private int numberOfLegs;
        private Person owner;

        public Animal(String name, int numberOfLegs, Person owner) {
            this.name = name;
            this.numberOfLegs = numberOfLegs;
            this.owner = owner;
        }

        public String getName() {
            return name;
        }

        public int getNumberOfLegs() {
            return numberOfLegs;
        }

        public String getOwner() {
            return owner.getName();
        }
    }

Animal klassis saab vastavalt parameetritele nö teha uue looma. Ette tuleb anda nimi, jalgade arv ning omanik. NB! Omanik ei ole String-tüüpi, vaid Person-objekt.

.. code-block:: java

    package animal;

    import person.Person;

    public class Dog extends Animal {
        private int numberOfTeeth;
        public Dog(String name, int numberOfLegs, Person owner, int numberOfTeeth) {
            super(name, numberOfLegs, owner);
            this.numberOfTeeth = numberOfTeeth;
        }

        public int getNumberOfTeeth() {
            return numberOfTeeth;
        }
    }

Dog klass laieneb Animal klassi. Põhimõtteliselt on Dog klass Animal klassi alamklass. Kuna Dog on ka loom, siis saab Animal klassis põhiomadused paika panna ning igasugu erinevusi saab Dog klassis implementeerida jättes alles Animal klassi omadused. Selles näites lisasime hammaste arvu.

.. code-block:: java

    package person;

    public class Person {
        private String name;
        private int age;

        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }

        public String getName() {
            return name;
        }

        public int getAge() {
            return age;
        }
    }

Person klassis saab teha inimesi, andes ette nime ja vanuse. Inimestel on loomulikult ka muid parameetreid, mis iseloomustaksid teda paremini, aga selles näites kasutame vaid nime ning vanust.

.. code-block:: java

    import animal.Animal;
    import animal.Dog;
    import person.Person;

    public class Main {

        public static void main(String[] args) {
            Person tiit = new Person("Tiit", 1);
            Animal loom = new Animal("Loom", 5, tiit);
            Dog dog = new Dog("Rex", 4, tiit, 30);

            System.out.println("Nimi: " + tiit.getName() + 
                    ", vanus: " + tiit.getAge());
            System.out.println("Nimi: " + loom.getName() + 
                    ", jalgade arv: " + loom.getNumberOfLegs() + 
                    ", omanik: " + loom.getOwner());
            System.out.println("Nimi: " + dog.getName() + 
                    ", jalgade arv: " + dog.getNumberOfLegs() + 
                    ", omanik: " + dog.getOwner() +
                    ", hammaste arv: " + dog.getNumberOfTeeth());
        }
    }

Main klassis loome objektid ning väljastame konsooli soovitava info.

Main klassi tööle pannes saame:

.. code-block:: java

    Nimi: Tiit, vanus: 1
    Nimi: Loom, jalgade arv: 5, omanik: Tiit
    Nimi: Rex, jalgade arv: 4, omanik: Tiit, hammaste arv: 30


