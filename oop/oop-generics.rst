Geneerilised tüübid
===================

*Generics* ehk geneerilised tüübid funktsionaalsust on võimalik kasutada alates Java 5-st. 
Geneerilised tüübid võimaldavad arendajatel luua geneerilisi algoritme, see tähendab, et näiteks teatud funktsiooni parameetriks saab korraga anda nii 
Boolean tüüpi kui Integer tüüpi järjendi. Lisaks tagab geneeriline tüüp kompileerimise ajal tüübikindluse ja ei nõua käsitsi tüübi määramist (*cast*).  

Geneerilist tüüpi märgitakse kujul **<Tüüp>**. Näited: List<String>, Map<String, Integer>.

Geneerilist tüüpi (või tüüpe) saab kasutada:

- Funktsioonis
- Klassis
- Konstruktoris
- Muutuja tüübina (Geneerilise klassi sees)
- Liideses

Tüübikindlus:
-------------
Antud näide ilma geneerilist tüüpi kasutamata kompileerub ja käivitub, aga saab programmi tööajal vea, kuna sõne "test" pole võimalik numbriks muuta:

.. code-block:: java
  
    List list = new ArrayList();
    list.add("test"); // A String that cannot be cast to an Integer
    Integer i = (Integer) list.get(0); // Run time error


Lisades järjendile juurde sõne tüübi, saame kompileerimise ajal vea. See tähendab, et rakendust pole võimalik isegi käivitada, kuna tuvastatakse, et tüübid ei ühildu:

.. code-block:: java

    List<String> list = new ArrayList<String>();
    list.add("test");
    Integer i = list.get(0); // type error, during compile time

Funktsioon:
-----------
Geneerilise funktsiooni definitsiooni näide:

.. code-block:: java

    public static <Type> List<Type> fromArrayToList(Type[] value) {
       return Arrays.stream(value).collect(Collectors.toList());
    }

Geneerilise tüübi kaudu massiivi konverteerimine järjendiks, olenemata mis tüüpi objektid on andmestruktuuride sees (geneerilise tüübina ei saa kasutada primitiivseid tüüpe):

.. code-block:: java

    public static <T> List<T> fromArrayToList(T[] a) {
       return Arrays.stream(a).collect(Collectors.toList());
    }
    public static void main(String[] args) {
       Integer[] integerArray = {1, 2, 3, 4, 5};
       Boolean[] booleanArray = {true, false, true};
       int[] intArray = {1, 2, 3, 4, 5};
       fromArrayToList(booleanArray); // works
       fromArrayToList(integerArray); // works
       fromArrayToList(intArray); // not possible, because primitive type
    }


Klass, konstruktor, muutuja:
----------------------------

.. code-block:: java

    public class Entry<K, V> {
    
        private final K key;
        private final V value;
        
        public Entry(K key, V value) {
            this.key = key;
            this.value = value;
        }
        
        public K getKey() {
           return key;
        }
        
        public V getValue() {
           return value;
        }
        
        public String toString() {
            return key + ", " + value;
        }
        
        public static void main(String[] args) {
            Entry<String, Integer> mike = new Entry<>("Mike", 100);
            System.out.println(mike); // Mike, 100
            System.out.println(mike.getKey()); // Mike
            System.out.println(mike.getValue()); // 100
        }
    
    }


Liides:
-------

.. code-block:: java

    public interface List<E> { 
        void add(E x);
    }

Tüüpide piiramine:
------------------
Tüübid:

- **T** - muutuja geneerilise tüübi määramiseks, võib olla suvaline muutuja, tavaliselt T-ga tähistatakse tüüpi.
- **?** - tundmatu tüüp (*wildcard*).

Võimalik on piirata geneerilisi tüüpe, näiteks tüüp peab olema Number klassi alamklass:

.. code-block:: java

    public static <T extends Number> List<T> fromArrayToList(T[] a) {
       return Arrays.stream(a).collect(Collectors.toList());
    }
    
    public static void main(String[] args) {
       Integer[] integerArray = {1, 2, 3, 4, 5};
       Boolean[] booleanArray = {true, false, true};
       fromArrayToList(integerArray); // works
       fromArrayToList(booleanArray); // not possible, because Boolean is not subClass of Number
    }

Järjendis olevate elementide tüüp peab olema Integer klassi ülemklass (Integer, Number, Object):

.. code-block:: java

    public static void addNumbers(List<? super Integer> list) {
        for (int i = 1; i <= 10; i++) {
            list.add(i);
        }
    }
    public static void main(String[] args) {
        List<Object> objects = new ArrayList<>();
        objects.add(4);
        objects.add(new Object());
        addNumbers(objects);
        System.out.println(objects); // [4, java.lang.Object@65b54208, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }

Lisades funktsiooni parameetriks järjendi tundmatu tüübiga (?), saab funktsiooni parameetriks anda ette järjendi suvalise tüübiga:

.. code-block:: java

    public static void usingWildCard(List<?> param) {}
    public static void usingObject(List<Object> param) {}

    public static void main(String[] args) {
        List<String> strings = new ArrayList<>();
        List<Integer> integers = new ArrayList<>();
        List<Object> objects = new ArrayList<>();

        usingWildCard(strings); // works
        usingWildCard(integers); // works
        usingWildCard(objects); // works

        usingObject(strings); // doesn't work
        usingObject(integers); // doesn't work
        usingObject(objects); // works
    }
