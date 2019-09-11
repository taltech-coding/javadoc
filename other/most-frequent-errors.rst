Korduma kippuvad vead OOP ülesannetes
=====================================

Kui teie kood töötab, siis see on hea. Kuid meie eesmärk on õpetada teid kirjutama mitte ainult töötavat, vaid ka ilusat ja puhast koodi, mida on lihtsam hiljem parandada ja täiendada. Siin on toodud kõige tihedamad vead, mida tehakse vaba OOP ülesannetes.

Klassid ei ole jagatud pakettideks
----------------------------------

Esineme asi, mida me näeme, kui teeme teie ülesande lahti, on see, kuidas teie projekt on struktueeritud. Üldiselt on paketid mõeldud selleks, et vältida nimede kokkupõrget *(name collision)*, aga neid kasutatakse ka selleks, et jagada projekti plokkideks. **Teie klassid peavad olema loogiliselt pakettideks jagatud.** Kindlasti ei tasu iga klassi jaoks luua eraldi paketti. Näiteks ``Room`` ja ``RoomType`` saavad küll olla ühes paketis nimega ``room``. Aga kui te panete klasse ``Room`` ja ``OrderProcessor`` ühte paketti, siis see on juba kahtlane.

Sellest tasub mõelda juba enne koodi kirjutamist, sest järgmine viga on pakettidega tihedalt seotud.

Nähtavused
----------

**Väljade nähtavused peavad olema võimalikult madalad.** 

OOP disaini järgi peavad klassid teineteisest teadma võimalikult vähe. Üks oluline printsiip OOP disainis on kapseldamine (``encapsulation``), mille järgi on kõikidel väljadel nähtavus ``private`` ning nendele saab ligi läbi getteri/setteri. Kõik väljad ei pea tingimata olema ``private``. Kui teil on vaja muuta välja väärtust alamklassis, siis võib panna väljale nähtavus ``protected`` või ``package-private`` (kui ülem- ja alamklassid on ühes paketis). **Aga ärge pange kunagi väljadele nähtavust** ``public`` **!** ``public``'ud saavad olla ainult ``static final`` muutujad ja selle tingimusega, et te kasutate neid teistes klassides.

IntelliJ analüüsib teie koodi ja kui väljal/meetodil on liiga kõrge nähtavus, siis ta kohe värvib seda kollaseks ning ütleb, et nähtavus võiks olla madalam.

.. image:: /_images/visibility_error.png

Nimed
-----

Meetodite/muutujate/klasside nimetamine on ka oluline asi. Nimed peavad olema võimalikult selged, et teised inimesed (kes ei pruugi olla arendajad) saaks ka nendest aru. Ärge kasutage lühendeid, kui need pole tuntud. 

Head muutujate nimed: ``price``, ``priceInDollars``, ``currentValue``

Halvad muutujate nimed: ``p``, ``pricedollars``, ``cur``

**Nimetamise konventsioon:** https://ained.ttu.ee/javadoc/CodeStyle.html?highlight=nimed

**Üldised reeglid:**

* **Paketi nimi:** ainult väikesed tähed lubatud. Kui sisaldab mitu sõna, siis neid kirjutatakse kokku.

Näited: ``student``, ``taltech``, ``superhero``, ``studyprogramme``

* **Klassi nimi:** peab olema nimisõna. Tuleb vältida üldiseid nimesid nagu "Processor", "Parser", "Converter" jms. 

Näited: ``Account``, ``RoomPriceCalculator``, ``ComplexNumber``, ``EmployeeDataProcessor``.

* **Meetodi nimi:** peab sisaldama tegusõna. 

Näited: ``save``, ``delete``, ``getCurrentPrice``, ``findLastRecord``, ``isActive``.

* **Liideste nimed:** peab olema kas nimisõna (kui kasutate liidest nagu ülemtüüpi) või omadussõna. 

Näited: ``Comparable``, ``Fixable``, ``Drawable`` või ``Engine``, ``CoffeeMachine``, ``StudyProgramm``.

Liidese nimi peab olema abstraktsem kui selle liidese implementatsioonil:

Liidese nimi: ``CoffeeMachine`` -> Implementatsioonide nimed: ``AutomaticCoffeeMachine``, ``StandardCoffeeMachine``

* **Erindi (exception) nimi:** nimi järgi peab olema lihtne aru saada, mis probleemiga on tegu. **Lõpus peab olema sõna** ``Exception`` **.**

Näited: ``CannotMakeCoffeeException``, ``NoMoreActionsAllowedException``, ``GotIncorrectOutputFromAPIException``

* **Testi nimi:** peab olema selline, et kui see failib, siis kohe saab aru miks. 

Halvad nimed: ``testGetAge``, ``createPerson``, ``testBuyItem``

Paremad nimed: ``testThrowsExceptionIfPersonIsNot18YearsOld``, ``testTicketIsFreeIfClientIsAChild``, ``testNoMoreActionsIfMoneyIsGone``, ``testMoneyIsTakenWhenItemIsBought``

Siin (https://dzone.com/articles/7-popular-unit-test-naming) on välja toodud mõned nimetamise konventsioonid. Valige see, mis teile kõige rohkem meeldib ja kasutage seda igalpool.

Tüübid klassidena vs enumiga
----------------------------

Kui ülesandes on antud realiseerida mõnda objekti alamtüüpe ja mõnel alamtüübil on lisaomadus, mida teistel pole, siis realiseerige need klassidena. 

Näide: Hotellis on kahte tüüpi toad: tavaline tuba ja ärituba. Äritoal on punane nupp, millega saab personaali tuppa kutsuda.

Halb:

.. code-block:: java
	
	public class HotelRoom {
		private HotelType type;
		
		...
		
		public void callStaff() {
			if (type == BUSINESS_ROOM) {
				...
			}
		}
	}

Parem näide:

.. code-block:: java

	public class HotelRoom {
		...
	}

	public class BusinessRoom extends HotelRoom {
		public void callStaff() {
			...
		}
	}
	
Alamtüübid peavad olema realiseeritud niimoodi, et uue tüübi lisamiseks poleks vaja vana koodi ümber kirjutada.

**Enum'it saab kasutada siis, kui tüübist ei sõltu olemasolev funktsionaalsus ning ei ole vaja uut funktsionaalsust lisada.**

Näide: Seadme kohta peab olema võimalik teada saada tema tüüpi.

.. code-block:: java

	public class Device {
		private DeviceType deviceType;
	}
	
	public enum DeviceType {
		SMARTPHONE, LAPTOP, TABLET;
	}
	
*  Kui teie teete enumiga ja näete oma koodis sellist asja:

.. code-block:: java
	
	public class HotelRoom {
		private int roomSize;
		private RoomType roomType;
		private boolean hasAdditionalBed; // only for luxury room
	
		public int getPrice() {
			if (roomType == BUSINESS) {
				price = 0.8 * roomSize;
			} else if (roomType == LUXURY) {
				price = 0.9 * roomSize + (hasAdditionalBed ? 10 : 0);
			} else {
				price = roomSize;
			}
		}
	}
	
Siis te ilmselt teete midagi valesti.

Parem lahendus:

.. code-block:: java

	public abstract class HotelRoom {
		int roomSize;
		
		public abstract int getPrice();
	}
	
	public class StandardRoom extends HotelRoom {	
	
		@Override
		public int getPrice() {
			return roomSize;
		}
	}
	
	public class BusinessRoom extends HotelRoom {
	
		@Override
		public int getPrice() {
			return 0.8 * roomSize;
		}
	}
	
	public class LuxuryRoom extends HotelRoom {
		
		private boolean hasAdditionalBed;
		
		@Override
		public int getPrice() {
			return 0.9 * roomSize + (hasAdditionalBed ? 10 : 0);
		}
	}

Integer vs int, Float vs float, Boolean vs boolean jne
------------------------------------------------------

Igal primitiivsel tüübil Javas on olemas oma analoog klassina:

* int -> Integer
* double -> Double
* float -> Float
* boolean -> Boolean
* char -> Character

Kui teil on valik, kas kasutada primitiivset andmetüüpi või selle klassi, siis väga suure tõenääosusega peate kasutama ikkagi primitiivset andmetüüpi.

Kui kasutate klasse primitiivse tüübi asemel, siis peate silmas pidama:

* Objekt võib olla ``null``.
* Objekte ei soovitata võrrelda == operaatoriga.

Need klassid on põhimõtteliselt *wrapper*'id:

.. code-block:: java

	public class Integer {
		private int value;
		...
	}

Ainuke koht, kus saab kasutada ainult primitiivsete tüüpide klasse on Generic'ud. Näiteks listid, mapid, optionalid jms. Te ei saa kirjutada nt ``List<int>`` ja peate kirjutama ``List<Integer>``.

Implementatsiooni kasutamine liidese asemel tüübina
---------------------------------------------------

Klass peab olema disainitud niimoodi, et teised klassid teaks nii vähe kui võimalik sellest, kuidas see klass sisemiselt töötab. (*abstraheerimine*) Kui te valite välja või meetodi tüübiks liidese implementatsiooni liidese asemel, siis te rikute seda reeglit. Lisaks tekib teil probleeme, kui te hiljem otsustate implementatsioon vahetada teise vastu. Teiste sõnadega annab liidese kasutamine tüübina teile rohkem vabadust. 

Halb:

.. code-block:: java

	public class Student {
	    private ArrayList<Grade> grades = new ArrayList<>();
	    private HashMap<String, Integer> grants = new HashMap<>();
	    
	    public ArrayList<Grade> getGrades() {
	    	return grades;
	    }
	    
	    public HashMap<String, Integer> getGrants() {
	    	return grants;
	    }
	    
	}

Parem:

.. code-block:: java

	public class Student {
	    private List<Grade> grades = new ArrayList<>();
	    private Map<String, Integer> grants = new HashMap<>();
	    
	    public List<Grade> getGrades() {
	    	return grades;
	    }
	    
	    public Map<String, Integer> getGrants() {
	    	return grants;
	    }
	    
	}
	
**Erand: Implementatsioon sobib välja tüübiks, kui te kasutate selle implementatsiooni spetsiifilisi meetodeid. Getteri tüübiks jätke pigem liides.**

.. code-block:: java

	public class Student {
	    private ArrayList<Grade> grades = new ArrayList<>();
	    
	    public void doSmartThings() {
	    	...
		// List<...> does not have ensureCapacity method. Only ArrayList<...> does. 
		//  If grades list type was just List<Grade>, then you would need to cast 
		// grades to ArrayList<Grade> to call this method.
		grades.ensureCapacity(...);
		...
	    }
	    
	    public List<Grade> getGrades() {
	    	return grades;
	    }
	    
	}
