Tingimuslause
--------------

Tingimuslaused on laused, mis käivitavad koodi vastavalt tingimusele. Vabas vormis võib tingimuslauset esitada "kui <tingimus>, siis <väide>". See tähendab, et kui <tingimus> on täidetud, siis <väide> kehtib.

Tingimus (*condition*) on boolean-tüüpi väärtus (*true*/*false*). Javas on kahte liiki tingimuslauseid:

- *if*-lause, et valida kahe valiku vahel;
- *switch*-lause, et valida mitme alternatiivi vahel.

*if-then* lause
--------------

*if-then* lause on kõige lihtsam tingimuslause. See ütleb programmile, et täida mingit käsku ainult siis, kui tingimus vastab tõele. Juhul kui tingimus ei vasta tõele, siis läheb programm kohe *if-then* lause lõppu. 

Süntaks:

.. code-block:: java

  if (condition) {
      then-statement;
  }
  
Näide:
  
.. code-block:: java

  int x = 6;

  if (x < 5) {
      System.out.println("x is smaller than 5"); // Program excecutes this line only when x is smaller than 5
  }
 
*if-then-else* lause
------------------

if-then-else lause annab veel täiendava valiku käivitamiseks, kui tingimus ei vasta tõele. Kui esimene tingimus ei vasta tõele, siis täidetakse *else*-käsk. 

Süntaks:

.. code-block:: java

  if (condition) {
      then-statement;
  } else if (condition) {
      else-if-statement;
  } else {
      else-statement;
  }
  
Näide:

.. code-block:: java

  class Example {
    public static void main(String[] args) {
    
        int testScore = 78;
        char grade;

        if (testScore >= 90) {
            grade = 'A';
        } else if (testScore >= 80) {
            grade = 'B';
        } else if (testScore >= 70) {
            grade = 'C';
        } else if (testScore >= 60) {
            grade = 'D';
        } else {
            grade = 'F';
        }
        System.out.println("Grade = " + grade);
     } 
  }

Programmi väljund on: :code:`Grade = C`

Programmis on näha, et testScore võib korraga täita mitut tingimust: 78 >= 70 ja 78 >= 60. Kui üks tingimus on täidetud, siis programm ei vaata enam järgmisi tingimusi.


Tingimus *if*-lauses
-----------------------

Tingimus (*condition*) võib olla näiteks:

- muutuja, mis on boolean-tüüpi:

.. code-block:: java

    boolean finished;
    ...
    if (finished) {
        ...
           
- primitiivsete andmetüüpide võrdlemine (==, !=, >, <, >=, või <=):
 
.. code-block:: java

    int a, b, c;
    ...
    if (a > b + c) {
        ...
     
- meetodi väljakutse, mis tagastab *boolean*-tüüpi väärtuse:
 
.. code-block:: java

    String answer;
    ...
    if (answer.equalsIgnoreCase("YES")) {
        ...
        
- keerukam lause, kasutades !, && ja || operaatoreid:

.. code-block:: java

    int a, b, c, d;
    String answer;
    ...
    if ((a > (b+c)) || (a == d) && !answer.equalsIgnoreCase("YES")) {
        ...
        
**Keerukamas tingimuses konjunktsiooni (&&) eemaldamine**

.. code-block:: java

  if ((x < y) && (y < z)) {
      System.out.println("y is between x and z");
  } else {
      System.out.println("y is not between x and z");
  }
  
Konjunktsiooni saab asendada kahe *if*-lausega:

.. code-block:: java

  if (x < y) {
      if (y < z) {
          System.out.println("y is between x and z");
      } else {
           System.out.println("y is not between x and z");
      } 
  } else {
      System.out.println("y is not between x and z");
  }
    
Sellisel juhul tuleb *else* haru kahekordistada.
  
**Keerukamas tingimuses disjunktsiooni (||) eemaldamine**

.. code-block:: java

  if ((x == 1) || (x == 2)) {
      System.out.println("x is equal to 1 or to 2");
  } else {
      System.out.println("x is different from 1 and from 2");
  }

Disjunktsiooni saab asendada *else if*-lausega:

.. code-block:: java

  if (x == 1) {
      System.out.println("x is equal to 1 or to 2");
  } else if (x == 2) {
      System.out.println("x is equal to 1 or to 2");
  } else {
      System.out.println("x is different from 1 and from 2");
  }
  
  Sellisel juhul tuleb dubleerida else-haru.
  
Tingavaldis
-----------

Süntaks:

.. code-block:: java

  condition ? expression-1 : expression-2;
  
Tingimus (*condition*) on boolean-tüüpi väärtus. *expression-1* ja *expression-2* peavad olema sama tüüpi.

Kui tingimus on tõene, käivita *expression-1*, vastasel juhul käivita *expression-2*.

Näide:

.. code-block:: java

   int a = 5;
   int b = 3;
   
   System.out.println("Bigger value is: " + (a > b) ? a : b); //Prints "Bigger value is: 5" to the console

Mis on samaväärne sellega:

.. code-block:: java

  int a = 5;
  int b = 3;
   
  if (a > b) {
      System.out.println("Bigger value is: " + a);
  } else {
      System.out.println("Bigger value is: " + b);
  }

*Switch*-lause
-----------

Erinevalt *it-them* ja *if-then-else* lausetest, *switch*-lausel saab olla palju võimalikke valikuid.

Järgnevas näide *Example* deklareeritakse täisarv nimega "month", mille väärtus kirjeldab kuud. Kood annab väljundiks kuu nime vastavalt selle väärtusele, kasutades *switch*-lauset.

.. code-block:: java

  public class Example {
      public static void main(String[] args) {

          int month = 8;
          String monthAsString;
          
          switch (month) {
              case 1:  monthAsString = "January";
                       break;
              case 2:  monthAsString = "February";
                       break;
              case 3:  monthAsString = "March";
                       break;
              case 4:  monthAsString = "April";
                       break;
              case 5:  monthAsString = "May";
                       break;
              case 6:  monthAsString = "June";
                       break;
              case 7:  monthAsString = "July";
                       break;
              case 8:  monthAsString = "August";
                       break;
              case 9:  monthAsString = "September";
                       break;
              case 10: monthAsString = "October";
                       break;
              case 11: monthAsString = "November";
                       break;
              case 12: monthAsString = "December";
                       break;
              default: monthAsString = "Invalid month";
                       break;
          }
          System.out.println(monthAsString);
      }
  }

------

https://docs.oracle.com/javase/tutorial/java/nutsandbolts/if.html
