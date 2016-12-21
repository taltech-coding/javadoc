==============================
Ühiktestimine ehk Unit Testing
==============================
*Test Driven Development*
-----------------------

Ühiktestimine on seotud *Test Driven Development*'iga (TDD), mille põhimõtteks on enne kirjutada testid ja pärast seda hakata implementeerima koodi, mis peab läbima kirjutatud testid. Kood on valmis siis, kui ei olda enam suutelised kirjutama uusi teste, millest kood saaks läbi kukkuda. Testklass on eraldi klass.

-------------------------

Testklassi loomine
-------------------
- *IntelliJ*-s on võimalik autogenereerida testklass kui vajutada *alt+enter* klassi nime peal.
- Uuest aknast saab valida kuhu tehakse *Test Class* ning milliseid meetodeid testitakse.
- Tavaliselt on vaja lisada ka *Dependency* vastavale testing versioonile, olgu selleks *TestNG*, *JUnit5* või mõni muu.
- Seda saab kergelt teha kui vajutada *fix* nuppu ja valida esimene variant.
- Teine võimalus *dependency* lisamiseks on *File* -> *Project Setting* -> *Modules*, sealt valida moodul, millele testi *library* külge panna, seejärel valida paremalt poolt *Dependencies* ja rohelise nuppuga lisada testi *library*.



*Assert*'imine
-----------
Hea oleks kui kasutada koodi alguses *@BeforeMethod* meetodit, mis *setup*'ib kõik vajaliku. *@BeforeMethod*'i tehakse enne igat testi, niimodi saab kindel olla, et testid üksteist ei mõjuta.

Vastuste võrdlemiseks on mitu erinevat võimalust:

- *assertEquals(expected, actual)*
- *assertTrue()*
- *assertFalse()*

All pool on tehtud Ago *Junit* testi järgi, kuid all olev kood on *TestNG*-ga tehtud.

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

*Test class*'is on kasutusel erinevaid viise testimiseks. Seal on kasutusel nii *assertTrue*, kui ka *assertEquals*. Lisaks on veel kasutusel *assertEquals*, kus on ette antud eraldi *error message*, mida kuvatakse kui test kukub läbi.

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


**Ago ühiktestimise näide aastast 2016** : https://www.youtube.com/watch?v=dIjtTvc6-ME
