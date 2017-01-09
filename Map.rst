===============
Kujutis ehk Map
===============
Map on andmekogum, kus on võtmete hulga igale elemendile vastavuses üks väärtuste hulga element. Kujutis sisaldab kaheosalisi kirjeid, millest esimest komponenti nimetatakse võtmeks ja teist väärtuseks. Ühe võtmega elemente võib olla vaid üks. Seda kasutatakse juhul, kui on vaja kiiresti mingi võtme järgi üles leida teist väärtust. Võti on alati seotud väärtusega.

Enimlevinud on HashMap.

HashMap kirjeldatakse ära kujul : **HashMap<K, V> hashMap = new HashMap<K, V>();** kus K ja V on andmetüübid.

K - Key
V - Value

Olulisemad meetodid:

* map.put(K, V) - väärtus V lisatakse võtmega K kohale. Näiteks map.put("tere", 3); .
* map.size() - võti-väärtus seoste arv (võib mõelda ka kas lihtsalt võtmete arv või väärtuste arv).
* map.get(K) - tagastab etteantud võtmega (mille andmetüüp on K) seotud väärtuse (mille andmetüüp on V). K ja V andmetüübid on määratud HashMap'i loomise ajal. 

Üks HashMapi näide.

.. code-block:: java

	import java.util.HashMap;
    import java.util.Iterator;
    import java.util.Map.Entry;
    
    public class ReadFile {
    
        public static void main(String[] args) {
            HashMap<String, Integer> ingrediants = new HashMap<String, Integer>();
    
            // Putting elements into the map where we assign a key with a value.
            //      The first argument is key and second argument is the value corresponding to the key.
            ingrediants.put("Carrots", 100);
            ingrediants.put("Apple", 60);
            ingrediants.put("Strawberry", 40);
    
            // Prints out the number of keys in the HashMap.
            System.out.println("HashMap size: " + ingrediants.size());
    
            // Prints out the value of the given key of Carrots.
            System.out.println("Amount of Carrots: " + ingrediants.get("Carrots"));
    
    
            // Printing out all elements.
            // 1) for-each cycle of only values. You cannot get the keys this way.
            for (Integer amount : ingrediants.values()) {
                System.out.println(amount);
            }
    
            // 2) for-each cycle of both keys and values
            for (Entry<String, Integer> entry : ingrediants.entrySet()) {
                System.out.println(entry.getKey() + " : " + entry.getValue());
            }
    
            // 3) Lambda, only usable in Java 8 or newer
            ingrediants.forEach((k, v) -> System.out.println("Key: " + k + " : Value: " + v));
    
            // 4) Iterator
            Iterator<Entry<String, Integer>> iterator = ingrediants.entrySet().iterator();
            while (iterator.hasNext()) {
                Entry<String, Integer> entry = iterator.next();
                System.out.println(entry.getKey() + " : " + entry.getValue());
            }
    
            // Adding new ingredient which has yet to be added.
            ingrediants.put("Pear", 20);
            // Increasing the amount of values;
            int oldAmount = ingrediants.get("Pear");
            int newAmount = oldAmount + 20;
            ingrediants.replace("Pear", newAmount);
            System.out.println("Pear : " + ingrediants.get("Pear"));
    
            // In order to get the total amount of ingredients we have to cycle through the list
            //      and add all values together.
            // This can be done in any of the previously mentioned ways.
            int sum = 0;
            for (Entry<String, Integer> entry : ingrediants.entrySet()) {
                sum += entry.getValue();
            }
            System.out.println("Ingredients total: " + sum);
        }
    }
