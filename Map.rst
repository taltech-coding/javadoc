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

Üks kindel HashMapi näide.

.. code-block:: java
	
	import java.util.HashMap;
	import java.util.Iterator;
	import java.util.Map.Entry;
	 
	public class HashMapExample {
	 
		public static void main(String[] args) {
			// tikumängu näide. mitu "1" palli meil on?
			HashMap<Integer, Integer> balls = new HashMap<Integer, Integer>();
	 
			// lisame elemendi. määrame võtme ja väärtuse
			balls.put(1, 3); // palle "1" on meil 3 tükki
			balls.put(2, 12); // palle "2" on meil 12 tükki
			balls.put(5, 10); // palle "5" on meil 10 tükki
	 
			System.out.println(balls.size());
	 
			System.out.println(balls.get(2)); // mitu palli "2" meil on
			System.out.println(balls.get(3)); // mitu palli "3" meil on?
	 
			// kuidas printida välja kõik elemendid?
			// 1) for-each tüüpi tsükkel ainult väärtustest
			for (Integer count : balls.values()) {
				System.out.println(count);
			}
			// aga nii ei saa me teada, mis number palli kohta mingi kogus käib
	 
			// 2) for-each tüüpi tsükkel võtmest ja väärtusest
			for (Entry<Integer, Integer> entry : balls.entrySet()) {
				System.out.println(entry.getKey() + ": " + entry.getValue());
			}
	 
			// iteraator
			Iterator<Entry<Integer, Integer>> it = balls.entrySet().iterator();
			while (it.hasNext()) {
				Entry<Integer, Integer> entry = it.next();
				System.out.println(entry.getKey() + ": " + entry.getValue());
			}
	 
			// kui tahame lisada ühe "4" palli (praegu neid pole üldse):
			balls.put(4, 1);
			// kui tahame lisada ühe "1" palli (suurendame pallide arvu):
			int count = balls.get(1);
			balls.put(1, count + 1); // kirjutame uue väärtuse, mis on ühe võrra suurem
	 
			// kuidas lugeda kokku, mitu palli meil on?
			// peame kõik väärtused läbi käima ja kokku liitma
			int sum = 0;
			for (Entry<Integer, Integer> entry : balls.entrySet()) {
				sum += entry.getValue();
			}
			System.out.println("Palle kokku:" + sum);
		}
	}