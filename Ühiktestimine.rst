==============================
Ühiktestimine ehk Unit Testing
==============================
Test Driven Development
-----------------------

Ühiktestimine on seotud Test Driven Developmentiga, mille põhimõte on enne kirjutada testid ja pärast seda hakata implementeerima koodi mis läbib testid. Koodi loetakse siis valmis kui ei ole suutelie kirjutama teste mis kukkuksid meetodist läbi. 	Test class on eraldi class.

-------------------------

Test classi loomine
-------------------
- IntelliJ-s on võimalik autogenereerida test class kui vajutada *alt+enter* classi nime peal.
- Uuest aknast saab valida kuhu tehakse Test Class ning milliseid meetodeid testitakse.
- Tavaliselt on vaja lisada ka Dependancy vastavale testing versioonile, olgu selleks JUnit 5 või mõni muu.
- Seda saab kergelt teha kui vajutada *fix* nuppu ja valida esimene varijant.
- Teine võimalus lisada dependanci on File -> Project Setting -> Modules sealt valida module millele JUnit külge panna, siis paremalt poolt valida Dependancies ja rohelise nuppuga Junit-i külge panna.



Assertimine
-----------
Hea oleks kui kasutada *@BeforeEach* meetodi ees mis setupib kõik vajaliku. Seda *@BeforeEach* tehakse enne igat testi, niimodi saab kindel olla, et testid üksteist ei mõjuta.

Vastuste võrdlemiseks on mitu erinevat võimalust olemas.

- assertEquals(expected, actual)
- assertTrue()
- assertFalse()

.. code-block:: java

  public class Math {
  	public int addTwoNumbers(int a, int b) {
  		return a + b;
  	}

  	...
  }
.. code-block:: java

  public class MathTest {
  	private Math math;

  	@BeforeEach
  	public void setUp() {
  		this.math = new Math();
  	}

  	@Test
  	public void testAddingTwoNumbers() {
  		Assertions.assertEquals(4, math.addTwoNumbers(3, 1));
  	}

  	...
  }



**Ago ühiktestimise näide aastast 2016**

https://www.youtube.com/watch?v=dIjtTvc6-ME