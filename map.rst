===============
Kujutis ehk Map
===============

Map on andmekogum, kus on võtmete hulga igale elemendile vastavuses üks väärtuste hulga element. Kujutis sisaldab kaheosalisi kirjeid, millest esimest komponenti nimetatakse võtmeks ja teist väärtuseks. Võtmete seas ei tohi olla korduvaid elemente. Kujutist kasutatakse juhul, kui on vaja kiiresti mingi võtme järgi üles leida vastavat väärtust. Võti on alati seotud ühe väärtusega.

Enimlevinud on HashMap, kuid on ka teisi (LinkedHashMap, TreeMap - vt allpool näiteid).

HashMap kirjeldatakse kujul : **Map<K, V> map = new HashMap<>();** kus K ja V on andmetüübid.

K - Key, võtme andmetüüp. Kõik võtmed selles kujutises peavad olema seda andmetüüpi.

V - Value, väärtuse andmetüüp. Kõik väärtused selles kujutises peavad olema seda andmetüüpi.

Nii võti kui väärtus kumbki ei saa olla primitiivset andmetüüpi. Selleks, et kasutada täisarve, tuleb kasutada andmetüüpi Integer jne. Kujutise loomisel määratakse ära nii võtme kui väärtuse andmetüübid. Loodavasse kujutise objekti saab lisada vaid algselt määratud andmetüüpe.

Olulisemad meetodid:

* :code:`map.put(K key, V value)` - väärtus *value* (andmetüüp V) lisatakse võtmega *key* (andmetüüp K) kohale. Näiteks :code:`map.put("tere", 3);` .
* ``map.putIfAbsent(K key, V value)`` - kui sellist võtit kujutises ei ole, lisatakse võtmele ``key`` väärtus ``value``.
* :code:`map.size()` - võti-väärtus seoste arv (võib mõelda ka kas lihtsalt võtmete arv või väärtuste arv).
* :code:`map.get(Object key)` - tagastab etteantud võtmega *key* (mille andmetüüp on K, kui lubatakse kõiki Object alamtüüpi objekte - need kõik tagastavad ``null``) seotud väärtuse (mille andmetüüp on V). K ja V andmetüübid on määratud Map'i loomise ajal. Näiteks :code:`Integer count = map.get("tere");`.
* ``map.getOrDefault(Object key, V defaultValue)`` - kui etteantud võtmega ``key`` väärtust ei ole, tagastatakse ``defaultValue``. Muul juhul töötab nagu ``map.get(Object K)``.

Näide, kuidas loendada elemente (võti on element, väärtus on selle elemendi kogus):

.. code-block:: java

    import java.util.Map;
    import java.util.HashMap;
    import java.util.List;
    
    public class CountNames {
    
        public static Map<String, Integer> getNameCounts(List<String> names) {
            Map<String, Integer> map = new HashMap<>();
            for (String name : names) {
                // key = name, value = existing value + 1
                // if currently there is not existing value, 
                // then 0 is used (and 0 + 1 => 1)
                map.put(name, map.getOrDefault(name, 0) + 1);
            }
            return map;
        }
    
        public static void main(String[] args) {
            System.out.println(getNameCounts(List.of("Lee", "Mati", "Kati", "Lee", "Kati", "Lee")));
            // {Lee=3, Kati=2, Mati=1}
        }
    }

Üks *HashMap*'i näide:

.. code-block:: java

    import java.util.Map;
    import java.util.HashMap;
    import java.util.Iterator;
    import java.util.Map.Entry;
    
    public class ReadFile {
    
        public static void main(String[] args) {
            Map<String, Integer> ingredients = new HashMap<>();
    
            // Putting elements into the map where we assign a key with a value.
            //      The first argument is key and second argument is the value corresponding to the key.
            ingredients.put("Carrots", 100);
            ingredients.put("Apple", 60);
            ingredients.put("Strawberry", 40);
    
            // Prints out the number of keys in the HashMap.
            System.out.println("HashMap size: " + ingredients.size());
    
            // Prints out the value of the given key of Carrots.
            System.out.println("Amount of Carrots: " + ingredients.get("Carrots"));
    
    
            // Printing out all elements.
            // 1) for-each cycle of only values. You cannot get the keys this way.
            for (Integer amount : ingredients.values()) {
                System.out.println(amount);
            }
    
            // 2) for-each cycle of both keys and values
            for (Entry<String, Integer> entry : ingredients.entrySet()) {
                System.out.println(entry.getKey() + " : " + entry.getValue());
            }
    
            // 3) Lambda, only usable in Java 8 or newer
            ingredients.forEach((k, v) -> System.out.println("Key: " + k + " : Value: " + v));
    
            // 4) Iterator
            Iterator<Entry<String, Integer>> iterator = ingredients.entrySet().iterator();
            while (iterator.hasNext()) {
                Entry<String, Integer> entry = iterator.next();
                System.out.println(entry.getKey() + " : " + entry.getValue());
            }
    
            // Adding new ingredient which has yet to be added.
            ingredients.put("Pear", 20);
            // Increasing the amount of values;
            int oldAmount = ingredients.get("Pear");
            int newAmount = oldAmount + 20;
            ingredients.replace("Pear", newAmount);
            System.out.println("Pear : " + ingredients.get("Pear"));
    
            // In order to get the total amount of ingredients we have to cycle through the list
            //      and add all values together.
            // This can be done in any of the previously mentioned ways.
            int sum = 0;
            for (Entry<String, Integer> entry : ingredients.entrySet()) {
                sum += entry.getValue();
            }
            System.out.println("Ingredients total: " + sum);
        }
    }

Java Documentation for HashMap: https://docs.oracle.com/javase/8/docs/api/java/util/HashMap.html

Erinevad *Map* implementatsioonid
---------------------------------

Lisaks HashMap'ile on võimalik kasutada veel LinkedHashMap ja TreeMap objekte. Vaatame nende vahet näidete abil.

.. code-block:: java

    import java.util.HashMap;
    import java.util.Map;

    public class DifferentMapsExample {
        public static void main(String[] args) {
            Map<String, Integer> map = new HashMap<>();
            String text = "first second third some more words and more first words";
            for (String word : text.split(" ")) {
                Integer count = map.get(word);
                if (count == null) {
                    map.put(word, 1);
                } else {
                    map.put(word, count + 1);
                }

            }
            System.out.println(map);
        }
    }
    
See kood annab tulemuseks:

.. code-block:: console

    {some=1, third=1, more=2, and=1, words=2, first=2, second=1}
    
Ehk siis **HashMap** ei garanteeri mingit kindlat võti-väärtus paaride järjestust (kuigi päris juhuslik see ka pole).
    
Kui me eelnevas koodis asendame HashMap TreeMap vastu, saame tulemuseks:

.. code-block:: console

    {and=1, first=2, more=2, second=1, some=1, third=1, words=2}
    
Ehk siis **TreeMap** sorteerib võti-väärtus paarid võtme järgi kasvavalt.

Kui eelnevas koodis asendada HashMap LinkedHashMap vastu, saame tulemuseks:

.. code-block:: console

    {first=2, second=1, third=1, some=1, more=2, words=2, and=1}
    
Ehk siis **LinkedHashMap** hoiab võti-väärtus paare selles järjekorras, kuidas need kujutisse lisatakse.

Koodinäite puhul on hea tähele panna, et kuna muutuja lõime liidese *Map* kaudu (mitte otse *HashMap* vms), siis on võimalik ka väikese vaevaga muuta kasutatavat implementatsiooni (algses koodis *HashMap*, aga saab muuta *TreeMap*'iks või *LinkedHashMap*'iks).

Mõned näited *stream* API-ga
-------------------------------

.. code-block:: java

    import java.util.ArrayList;
    import java.util.HashMap;
    import java.util.List;
    import java.util.Map;
    import java.util.function.Function;
    import java.util.stream.Collectors;

    public class MapLambdas {
        public static void main(String[] args) {
            Map<String, Integer> wordCounts = new HashMap<>();

            List<String> words = new ArrayList<>();
            words.add("one");
            words.add("two");
            words.add("one");
            words.add("three");
            words.add("four");
            words.add("one");
            words.add("four");
            words.add("one");
            words.add("four");
            words.add("four");

            wordCounts = words.stream()
                    .collect(
                            // group by the value itself
                            Collectors.groupingBy(Function.identity(),
                            // count values, add 1 for every found value
                            Collectors.summingInt(e -> 1))
                    );
            System.out.println(wordCounts);
            
            // we will get:
            // {four=4, one=4, three=1, two=1}

            List<String> popularWords = wordCounts.entrySet()
            
                    // take the stream from the set of Entry objects
                    .stream()
                    
                    // here we filter. e is the Entry.
                    // we take Entry objects where value > 2
                    .filter(e -> e.getValue() > 2)
                    
                    // here we map Entry object to the key
                    // that way we get only the key for every entry
                    .map(e -> e.getKey())
                    
                    // here we collect it to list
                    .collect(Collectors.toList());
                    
            System.out.println(popularWords);
            
            // we will get:
            // [four, one]
        }
    }
    
Mitme väärtuse hoidmine ühe võtme all
--------------------------------------

Kui tavapäraselt saab kujutises ühe võtme all hoida ühte väärtust, siis kasutades täiendavat andmestruktuuri, saab ühe võtme alla lisada ka mitu väärtust. Järgmises näites kasutatakse kujutist, kus võti on tudengi perenimi ja väärtus on järjent kõikidest sellistest Student objektidest, kellel selline perenimi on.

.. code-block:: java

    import java.util.ArrayList;
    import java.util.HashMap;
    import java.util.List;
    import java.util.Map;

    /**
     * An example how to use a map with several values for one key.
     */
    public class StudentsByLastname {

        // here we keep list of students by last name
        private Map<String, List<Student>> studentsByLastname = new HashMap<>();

        // this could be public class in Student.java file.
        // for this example we have used inner class.
        class Student {
            private String name;
            public Student(String name) {
                this.name = name;
            }
            public String getLastName() {
                String[] names = name.split(" ");
                return names[names.length - 1];
            }

            @Override
            public String toString() {
                return name;
            }
        }

        // main method could also be in some other file.
        // for this example, we have implemented it here.
        public static void main(String[] args) {

            StudentsByLastname students = new StudentsByLastname();
            students.addStudent("Mati Kaal");
            students.addStudent("Kati Kaal");
            students.addStudent("Malle Kaal");
            students.addStudent("Robert Keel");
            students.addStudent("Guido Keel");

            System.out.println(students.getStudentsByLastname());
        }

        /**
         * Adds a new student by name.
         *
         * A new student object is created and added
         * to the list based on the last name.
         * @param name The full name of the student.
         */
        public void addStudent(String name) {
            Student student = new Student(name);
            String lastname = student.getLastName();
            // get the current value
            List<Student> students = studentsByLastname.get(lastname);
            if (students == null) {
                // no students found
                // let's create an empty list
                students = new ArrayList<>();
                // and add the current student there
                students.add(student);
                studentsByLastname.put(lastname, students);
            } else {
                // we have have some students already
                // let's just add the current student
                students.add(student);
            }
        }

        /**
         * Returns a map of students by last name.
         *
         * @return Map where key is last name and value is a list of student objects by that last name.
         */
        public Map<String, List<Student>> getStudentsByLastname() {
            return studentsByLastname;
        }
    }

    
Lisalugemist Map liidese kohta: https://docs.oracle.com/javase/tutorial/collections/interfaces/map.html
