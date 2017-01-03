===============
Kujutis ehk Map
===============
Map on andmekogum, kus on võtmete hulga igale elemendile vastavuses üks väärtuste hulga element. Kujutis sisaldab kaheosalisi kirjeid, millest esimest komponenti nimetatakse võtmeks ja teist väärtuseks. Ühe võtmega elemente võib olla vaid üks. Seda kasutatakse juhul, kui on vaja kiiresti mingi võtme järgi üles leida teist väärtust. Võti on alati seotud väärtusega.

Enimlevinud on HashMap.

HashMap kirjeldatakse ära kujul : **HashMap<K, V> hashMap = new HashMap<K, V>;** kus K on viide võtme objektile ja V on viide väärtuse objektile.

Olulisemad meetodid:

* map.put(K, V)<code> - väärtus <code>V lisatakse võtmega K kohale. Näiteks map.put("tere", 3); .
* map.size() - võti-väärtus seoste arv (võib mõelda ka kas lihtsalt võtmete arv või väärtuste arv).
* V map.get(K) - tagastab etteantud võtmega (mille andmetüüp on K) seotud väärtuse (mille andmetüüp on V). K ja V andmetüübid on määratud HashMap'i loomise ajal. 

Üks HashMapi näide.

.. code-block:: java
	
	import java.util.HashMap;
	import java.util.Iterator;
	import java.util.Map.Entry;
	 
	public class HashMapExample {
	 
		public static void main(String[] args) {
			HashMap<Integer, Integer> balls = new HashMap<Integer, Integer>();
	 
			// Putting elements into the map where we assign a certain key with a value
			//	The first argument is the key and second argument is value
			balls.put(1, 3);
			balls.put(2, 12);
			balls.put(5, 10);
			
	 		// Prints out the number of keys in the hashmap
			System.out.println(balls.size());
	 
	 		// Prints out the number of values regarded with the key value of 2
			System.out.println(balls.get(2)); 
	 
			// Printing out all elements
			// 1) for-each cycle of only values
			// 	You can't find out the keys this way
			for (Integer count : balls.values()) {
				System.out.println(count);
			}
	 		

			// 2) for-each cycle of both keys and values
			for (Entry<Integer, Integer> entry : balls.entrySet()) {
				System.out.println(entry.getKey() + ": " + entry.getValue());
			}

			// 2.5) Lambda, only usable in Java 8 or newer
			// There in no need to create an Entry<>
			map.forEach( (k, v) -> System.out.println("Key: " + k + " : Value: " + v));
	 
			// iterator
			Iterator<Entry<Integer, Integer>> it = balls.entrySet().iterator();
			while (it.hasNext()) {
				Entry<Integer, Integer> entry = it.next();
				System.out.println(entry.getKey() + ": " + entry.getValue());
			}
	 
			// adding a single ball with key 4 and value 1 (currently not added):
			balls.put(4, 1);
			// when we want to increase the value of balls with key 1 by a single int.
			int count = balls.get(1);
			balls.put(1, count + 1); // overwriting the current value with a new one.
	 
			// in order to get all values we have to cycle through the map and add all values together
			// this again can be done in any of the previously mentioned ways.
			int sum = 0;
			for (Entry<Integer, Integer> entry : balls.entrySet()) {
				sum += entry.getValue();
			}
			System.out.println("Palle kokku:" + sum);
		}
	}
