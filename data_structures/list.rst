==============
Loend ehk List
==============
Loend on korrastatud andmekogum, mis tähendab, et see säilitab elementide järjekorra. Kui lisada elemendid loendisse, siis hiljem on nad lugemisel täpselt samas järjekorras kui sisestamisel.

Javas on mitmeid erinevaid loendeid, kuid enim kasutatavad on *Arraylist*  ning *List*.

ArrayList
---------
ArrayList on dünaamiline masiiv. See töötab enamjaolt nagu massiiv, kuid selle pikkus on dünaamiline. Kui massiivis peab loomisel teadma, kui suur ta on, siis *ArrayList*'is ei ole seda tarvis teada. Loend suureneb ise vastavalt vajadusele.

ArrayList vs LinkedList
-----------------------

Nii ArrayList kui ka LinkedList on kaks enimkasutatud listi tüüpi, mõlemal on omad eelised.
- **ArrayList** - ArrayListi on parem kasutada, kui võtta elemente suvalises järjekorras
- **LinkedList** - LinkedListi on parem kasutada, kui on vaja kiirelt lisada või eemaldada järjest listi elemente.

Koodinäide, kuidas ArrayListi lisada asju ja sellega töödelda.

.. code-block:: java

	import java.util.ArrayList;
  	
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
	 	
			System.out.println(arrayList.get(1)); // 2 (value is found by index)
	 	
			arrayList.remove(1); // element with given index is removed
			// The rest of the list is shifted:
			// List: 1, 3, 4
	 	
			arrayList.add(1, 2); // Adding value 2 into the index 1.
			// All elements are again shifted:
			// List: 1, 2, 3, 4
	 	
			arrayList.set(1, 7); // Switching the value of the given index:
			// List: 1, 7, 3, 4
 	
			arrayList.clear(); // Clear the entire list
			
			// loome arrayList'i elementidega 1..10
			for (int i = 0; i < 10; i++) {
				arrayList.add(i + 1);
			}

			// Printing out the values of list.
			for (int i = 0; i < arrayList.size(); i++) {
				System.out.println(arrayList.get(i));
			}
 		}
	}


Eelmises näites käidi List läbi tavalise for-loopiga.
Siin on veel mõned viisid, kuidas Listi läbi käia ja seda töödelda:


.. code-block:: java

	// 1) for-each cycle of only values
	for (Integer value : arraylist) {
		System.out.println(value);
	}

	// 2) Lambda, only usable in Java 8 or newer
	map.forEach(integer -> System.out.println(integer));

	// 3) iterator, needs to import java.util.Iterator
   	Iterator<Integer> iterator = arrayList.iterator();
   	while (iterator.hasNext()) {
   	    Integer integer = iterator.next();
   	    System.out.println(integer);
   	}


Listi sorteerimiseks võib muidugi ka ise programmi kirjutada, kuid see on juba Javasse ka sisse ehitatud. Selleks on *Collections.sort(listName)*. Kui tahta alguses mingeid asju listi lisada, saab kasutada ka *Arrays.asList()*.

.. code-block:: java

	import java.util.ArrayList;
	import java.util.Collections;

	public class SortingExample {
		public static void main (String[] args) {
			// Creates a list if given Integers
			ArrayList<Integer> arraylist = new Arraylist<>(Arrays.asList(9,1,8,2,7,3,6,4,5));
			Collections.sort(arraylist); // Sorts the list in ascending order
			System.out.println(arraylist.toString()); // [1, 2, 3, 4, 5, 6, 7, 8, 9]
		}
	}

