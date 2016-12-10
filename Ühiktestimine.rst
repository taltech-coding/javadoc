==============================
Ühiktestimine ehk Unit Testing
==============================
Test Driven Development
-----------------------

Ühiktestimine on seotud Test Driven Development'iga (TDD), mille põhimõtteks on enne kirjutada testid ja pärast seda hakata implementeerima koodi, mis peab läbima kirjutatud testid. Kood on valmis siis, kui ei olda enam suutelised kirjutama uusi teste, millest kood saaks läbi kukkuda. Testklass on eraldi klass.

-------------------------

Test klassi loomine
-------------------
- IntelliJ-s on võimalik autogenereerida testklass kui vajutada *alt+enter* klassi nime peal.
- Uuest aknast saab valida kuhu tehakse Test Class ning milliseid meetodeid testitakse.
- Tavaliselt on vaja lisada ka Dependency vastavale testing versioonile, olgu selleks JUnit 5 või mõni muu.
- Seda saab kergelt teha kui vajutada *fix* nuppu ja valida esimene variant.
- Teine võimalus dependency lisamiseks on File -> Project Setting -> Modules, sealt valida moodul, millele JUnit külge panna, seejärel valida paremalt poolt Dependencies ja rohelise nuppuga lisada Junit.



Assert'imine
-----------
Hea oleks kui kasutada koodi alguses *@BeforeEach* meetodit, mis setup'ib kõik vajaliku. *@BeforeEach*'i tehakse enne igat testi, niimodi saab kindel olla, et testid üksteist ei mõjuta.

Vastuste võrdlemiseks on mitu erinevat võimalust:

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
