===============
Kujutis ehk Map
===============
Map on andmekogum, kus on võtmete hulga igale elemendile vastavuss üks väärtuste hulga element. Kujutis sisaldendast endast kaheosalisi kirjeid, millest esimest komponenti nimetatakse võtmeks ja teist väärtuseks. Ühe võtmega elemente võib olla vaid üks. Seda kasutatakse juhul, kui o vaja kiiresti mingi võtme järgi üles leida teist väärtust. Võti on alati seotud väärtusega.

Enimlevinud on HashMap.

HashMap kirjeldatakse ära kujul : **HashMap<K, V> hashMap = new HashMap<K, V>;** kus K on viide võtme objektile ja V on viide väärtus objektile.

Olilusemad meetodid:

* map.put(K, V)<code> - väärtus <code>V lisatakse võtmega K kohale. Näiteks map.put("tere", 3); .
* map.size() - võti-väärtus seoste arv (võib mõelda ka kas lihtsalt võtmete arv või väärtuste arv).
* V map.get(K) - tagastab etteantud võtmega, mille andmetüüp on K, väärtuse, mille andmetüüp on V. K ja V andmetüübid on määratud HashMap'i loomise ajal. 

Üks kindel HashMapi näide tikumängu puhul et leida mitu "1" palli on.

.. code-block:: java
	
	import java.util.HashMap;
	import java.util.Iterator;
	import java.util.Map.Entry;
	 
	public class HashMapExample {
	 
		public static void main(String[] args) {
			HashMap<Integer, Integer> balls = new HashMap<Integer, Integer>();
	 
			// Putting elements into the map where we assign a certain key with a value
			balls.put(1, 3); // 3 balls with value 1
			balls.put(2, 12); // 12 balls with value 2
			balls.put(5, 10); // 10 balls with value 1
	 
			System.out.println(balls.size()); // prints out the number of keys in the hasmap
	 
			System.out.println(balls.get(2)); // prints out the number of values regarded with the key value of 2
			System.out.println(balls.get(3)); // prints out the number of values regarded with the key valvue of 3
	 
			// Printing out all elements
			// 1) for-each cycle of only values
			for (Integer count : balls.values()) {
				System.out.println(count);
			}
	 		// can't find out the keys this way

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
			// kwhen we want to increase the balls with key one by a single int.
			int count = balls.get(1);
			balls.put(1, count + 1); // overwriting the current value with a new one.
	 
			// in order to get all values we have to cycle through the map and add all values together
			int sum = 0;
			for (Entry<Integer, Integer> entry : balls.entrySet()) {
				sum += entry.getValue();
			}
			System.out.println("Palle kokku:" + sum);
		}
	}
