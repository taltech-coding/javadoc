==============
Loend ehk List
==============
Loend on korrasatud andmekogum, mis tähendab, et see säilitab järjekorra. Kui lisada elemendid loendisse, siis hiljem on nad lugemisel täpselt samasjärjekorras kui nad sisestati.

Javas on suht palju erinevail loendeid, kuid enim kasutatav on *Arraylist*  ja *List*.

ArrayList
---------
ArrayList on dünaamiline masiiv. See tõõtab enamjaolt nagu massiiv, kuid pikkus on dünaamiline. Kui massiivis pidi teadma kui suur oli vaja lisada siis ArrayListis ei ole vaa teada. Loend suureneb ise vastavalt vajadusele

.. code-block:: java

  	public class ArrayListExample {
  		public static void main(String[] args) {
 	 		ArrayList<Integer> arrayList = new ArrayList<Integer>();
	 		arrayList.add(1);
			arrayList.add(2);
			System.out.println(arrayList.size()); // 2
	 	
			arrayList.add(3);
			arrayList.add(4);
			// loend: 1, 2, 3, 4
			System.out.println(arrayList.size()); // 4
	 	
			System.out.println(arrayList.get(1)); // 2
	 	
			arrayList.remove(1); // element indeksiga 1 eemaldatakse
			// ülejäänud loendi elemendid liigutatakse ühe võrra ettepoole:
			// loend: 1, 3, 4
	 	
			arrayList.add(1, 2); // lisame elemendi "2" positsioonile 1
			// kõik elemendid indeksiga 1 või suuremad nihutatakse ühe võrra edasi:
			// loend: 1, 2, 3, 4
	 	
			arrayList.set(1, 7); // asendame elemendi väärtuse positsioonil 1:
			// loend: 1, 7, 3, 4
 	
			arrayList.clear(); // tühjendame
			// arrayList 1..10
			for (int i = 0; i < 10; i++) {
				arrayList.add(i + 1);
			}

			// prindime välja
			for (int i = 0; i < arrayList.size(); i++) {
				System.out.println(arrayList.get(i));
			}
 		}
	}
