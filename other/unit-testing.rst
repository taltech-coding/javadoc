===============================
Üksustestimine ehk Unit Testing
===============================

Definitsioon
-------------

Üksustestimist (*unit testing*) saab kirjeldada väga mitmel moel. Testimise eesmärk üldisemalt on tagada mingi komponendi või süsteemi toimimine vastavalt nõuetele. Üksustestimise puhul on testitav komponent üks "üksus" (*unit*) suuremast süsteemist. See, mida täpsemalt "üksuse" all mõeldakse, pole rangelt defineeritud. Mõnikord on "üksus" terve klass, teinekord üks funktsioon/meetod jne. "Üksust" võib proovida defineerida kui kõige väiksemat iseseisvalt töötavat (sõltumatut) tarkvara osa. Testimisega kontrollitakse, kas see "üksus" töötab erinevates olukordades korrektselt. Selleks kirjutatakse üksustestid. Kui kõik testid õnnestuvad, siis arvatavasti üksus töötab korrektselt (eeldab, et testid on piisavad). Selliselt saab kõik tarkvara väiksed komponendid läbi kontrollida. Kui komponendid töötavad, saab neid hakata kombineerima (et kokku panna suurem komponent ja lõpuks terve tarkvara). Kui mõni test ebaõnnestub, tuleb vastav komponent kõigepealt korda teha.

Tuleb tähele panna, et see, kui testid õnnestuvad, ei tähenda tingimata seda, et komponent töötab 100% õigesti. Testide õnnestumine näitab seda, et komponent töötab täpselt nii, nagu üksustestides kirjeldatud.

.. image:: /_images/unit_testing_good_code_bad_tests.png

Testide kirjutamine
---------------------

Javas kirjutatakse tavaliselt ühe klassiga seotud testid ühte eraldi testklassi. Kui näiteks testitav klass on :code:`Calculator`, siis testid kirjutatakse :code:`CalculatorTest` klassi. Testklass koosneb erinevatest testmeetoditest. Iga meetod võiks reeglina testida ühte konkreetset olukorda. Testitulemusi vaadatakse testmeetodite kaupa. Seega, kui üks meetod testib mitut erinevat situatsiooni, siis testitulemustest ei ole üheselt selge, millises olukorras test ebaõnnestub. Kui testime näiteks meetodit, mis leiab kahe arvu jagatise, siis oleks mõistlik testida eraldi 0-ga jagamist. Kui 0-ga jagamine panna kokku näiteks 1-ga jagamisega, näeme vaid seda, et test ebaõnnestub, aga me ei tea täpset põhjust (tulemuste täpsemal uurimisel on seda võimalik näha). Seega sellises olukorras võiks pigem kirjutada eraldi meetodid:

- 0-jagamise kohta (3 / 0)
- 1-ga jagamise kohta (3 / 1)
- 0 jagamise kohta (0 / 3)
- 0 / 0 kohta
- mingi "tavaline" jagamine, kus jagatav on suurem kui jagaja (6 / 4)
- "tavaline", kus jagatav on väiksem kui jagaja (4 / 6)
- "tavaline", kus jagatav ja jagaja on võrdsed (7 / 7)

Samas meetod, kus kontrollime 0-ga jagamist, võime teha mitu sarnast testi: 4 / 0, 10 / 0. Samamoodi üks "tavaline" meetod võib sisaldada teste: 6 / 4, 123 / 13, 7 / 6. Need erinevad konkreetsed jagatised testivad siiski sama "probleemi" või olukorda.

Kuidas testimine töötab
------------------------

Testimisel kasutatakse *assert*-meetodeid. Neid meetodeid on erinevaid (nendest on juttu allpool), aga kõik nad kontrollivad mingit väärtust. Kui kontroll õnnestub, siis see meetod ei tee midagi (testmeetodi käivitamine jätkub). Kui kontroll ei õnnestu, tekib viga (erind ehk *exception*). Sellise vea puhul lõpetatakse testmeetodi jooksutamine (kui seda viga kinni ei püüta) ning nimetatud test ebaõnnestub. Kui testmeetod töötab lõpuni (ja viga ei teki), on test õnnestunud.

*Test Driven Development*
-------------------------

Üks levinud viis testide kasutamiseks on *Test Driven Development* (TDD), mille põhimõtteks on enne kirjutada testid ja pärast seda hakata implementeerima koodi, mis peab läbima kirjutatud testid. Kood on valmis siis, kui ei suudeta kirjutada uusi teste, millest kood saaks läbi kukkuda.

-------------------------

Testklassi loomine
-------------------
- *IntelliJ*-s on võimalik autogenereerida testklass kui vajutada *alt+enter* klassi nime peal.
- Uuest aknast saab valida kuhu tehakse *Test Class* ning milliseid meetodeid testitakse.
- Tavaliselt on vaja lisada ka *Dependency* vastavale kasutatavale testimisraamistikule, olgu selleks *TestNG*, *JUnit5* või mõni muu.
- Seda saab kergelt teha kui vajutada *fix* nuppu ja valida esimene variant.
- Teine võimalus *dependency* lisamiseks on *File* -> *Project Setting* -> *Modules*, sealt valida moodul, millele testi *library* külge panna, seejärel valida paremalt poolt *Dependencies* ja rohelise nuppuga lisada testi *library*.

Testimise näide
---------------

Toome näite, kus testitav meetod :code:`solve` on :code:`QuadraticEquationSolver` klassis. Koodinäide:

.. code-block:: java

    public class QuadraticEquationSolver {
        public static double[] solve(double a, double b, double c) {
            double d = b * b - 4 * a * c;
            if (d > 0) {
                return new double[]{(-b + Math.sqrt(d)) / 2 / a, (-b - Math.sqrt(d)) / 2 / a};
            } else if (d == 0) {
                return new double[]{-b / 2 / a};
            } else {
                return null;
            }
        }
    }


Järgnev on terivlik koodinäide junit4 raamistikuga testimise jaoks:

.. code-block:: java

    import org.junit.Test;

    import static org.junit.Assert.*;

    public class QuadraticEquationSolverTest {

        @Test
        public void testNoSolutions() {
            assertNull("Solver fails in case there are no solutions.",
                    QuadraticEquationSolver.solve(1, 1, 1));
        }

        @Test
        public void testOneSolution() {
            assertArrayEquals("Solver fails in case there is one solution.",
                    new double[]{1}, QuadraticEquationSolver.solve(1, -2, 1), 0.001);
        }

        @Test
        public void testTwoSolutions() {
            assertArrayEquals("Solver fails in case there are two solutions.",
                    new double[]{-1, 3}, QuadraticEquationSolver.solve(-1, 2, 3), 0.001);
        }
    }

Nagu näitest näha, testitakse kolme erinevat olukorda:

- ruutvõrrandil pole ühtegi lahendit
- ruutvõrrandil on vaid üks lahend
- ruutvõrrandil on kaks lahendit

Kasutatud on :code:`assertArrayEquals` meetodit, mis kontrollib, kas kaks etteantud massiivi on samade väärtustega,
kusjuures väärtusi kontrollitakse väikese lubatud veaga (*delta*). *double* tüüpi andmeid on alati mõistlik kontrollida väikese lubatud veaga. Antud juhul 0.001 tähendab seda, et arvud 5.0003 ja 5.0007 loetakse samaks.

Testimise näide instantsi puhul
--------------------------------
Eelmine näide oli staatilise meetodi kohta. Toome teise näite, kus testime objekti (mitte staatilist) meetodit. Selleks, et me saaksime välja kutsuda objekti meetodit, peame kõigepealt looma objekti.

Hea oleks kui kasutada koodi alguses *@BeforeMethod* meetodit, mis seadistab kõik vajaliku. *@BeforeMethod* käivitatakse enne igat testi. Seega saab sellega mugavalt luua näiteks vajaliku instantsi.

Vastuste võrdlemiseks on mitu erinevat võimalust:

- *assertEquals(expected, actual)*
- *assertTrue()*
- *assertFalse()*

Siin on näide ühest klassist, mille meetodit :code:`isValid` me tahame testida. See pole 100% korrektne lahendus.

.. code-block:: java

  public class DateValidator {
      public boolean isValidDate(String date) {
          if (date == null) {
              return false;
          }
          if (!date.contains(".")) {
              return false;
          }
          String[] parts = date.split("\\.");
          if (parts.length != 2) {
              return false;
          }
          try {
              int day = Integer.parseInt(parts[0]);
              int month = Integer.parseInt(parts[1]);
              if (day < 1 || day > 31) {
                  return false;
              }
              if (month < 1 || month > 12) {
                  return false;
              }
              if (month == 2 && day > 28) {
                  return false;
              }
          } catch (NumberFormatException e) {
              return false;
          }
          return true;
      }
  }

Allpool olev testklassis kasutatakse *TestNG* raamistikku (kuigi ka *JUnit* võimaldab kõike seda sama ja 90% koodist on täpselt sama).

.. code-block:: java
  
  // Imports allow to use shortened versions of @Test, @BeforeMethod annotations
  import org.testng.annotations.BeforeMethod;
  import org.testng.annotations.Test;
  
  // Import allows to use shortened version of assertEquals
  import static org.testng.Assert.*;
  
  
  public class DateValidatorTest {
      private DateValidator dateValidator;
  
      @BeforeMethod
      public void setUp() throws Exception {
          this.dateValidator = new DateValidator();
      }
  
      @Test
      public void testIsValidDate() throws Exception {
          assertEquals(true, dateValidator.isValidDate("01.01"));
      }
  
      @Test
      public void testIsValidDateTooLargeDay() throws Exception {
          assertEquals(false, dateValidator.isValidDate("33.01"));
      }
  
      @Test
      public void testIsValidTooLargeMonth() throws Exception {
          assertEquals(false, dateValidator.isValidDate("03.21"));
      }
  
      @Test
      public void testIsValidTooSmallMonth() throws Exception {
          assertEquals(false, dateValidator.isValidDate("03.00"));
      }
  
      @Test
      public void testIsValidTooSmallDay() throws Exception {
          assertEquals(false, dateValidator.isValidDate("00.02"), "Error Message");
      }
      @Test
      public void testIsValidTooShortDay() throws Exception {
          assertTrue(dateValidator.isValidDate("01.2"));
      }
      @Test
      public void testIsValidTooShortMonth() throws Exception {
          assertTrue(dateValidator.isValidDate("1.02"));
      }
      @Test
      public void testIsValidTooShortMonthAndDay() throws Exception {
          assertTrue(dateValidator.isValidDate("1.2"));
      }
  
      @Test
      public void testIsValidTooLargeDay() throws Exception {
          assertEquals(false, dateValidator.isValidDate("33.02"));
      }
  
      @Test
      public void testIsValidFebruaryLastDay() throws Exception {
          assertEquals(true, dateValidator.isValidDate("28.02"));
      }
  
      @Test
      public void testIsValidFebruaryLastDayPlusOne() throws Exception {
          assertEquals(false, dateValidator.isValidDate("29.02"));
      }
  
      @Test
      public void testIsValidDateIncorrectInput() throws Exception {
          assertEquals(false, dateValidator.isValidDate("a"));
          assertEquals(false, dateValidator.isValidDate("a.a"));
          assertEquals(false, dateValidator.isValidDate("1:1"));
      }
  }
  
:code:`BeforeMethod` (JUnitis on :code:`Before`) annotatsiooniga meetod loob meile uue instantsi :code:`DateValidator` klassist. Seega me ei pea igas testmeetodis seda tegema.

Eelnevas koodinäites on kasutatud mitmes kohas *assertEquals* koos true/false võrdlusega. Õigem oleks kasutada kohe kas *assertTure* või *assertFalse* (paaris kohas on seda tehtud ka).
  
.. image:: /_images/unit_testing.png


**Test NG Documentatsioon** http://testng.org/doc/documentation-main.html

**Kas unit testimine on väärt seda** http://stackoverflow.com/questions/67299/is-unit-testing-worth-the-effort

**Ühiktestimise näide aastast 2016** : https://www.youtube.com/watch?v=dIjtTvc6-ME
