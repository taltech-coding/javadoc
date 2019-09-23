Tingimuslause
--------------

Tingimuslaused on laused, mis käivitavad koodi vastavalt tingimusele. Vabas vormis võib tingimuslauset esitada "kui <tingimus>, siis <väide>". See tähendab, et kui <tingimus> on täidetud, siis <väide> kehtib.

Tingimus (*condition*) on boolean-tüüpi väärtus (*true*/*false*). Javas on kahte liiki tingimuslauseid:

- *if*-lause, et valida kahe valiku vahel;
- *switch*-lause, et valida mitme alternatiivi vahel.

*if*-lause
--------------

*if*-lause (tingimusdirektiiv) on kõige lihtsam tingimuslause. See ütleb programmile, et täida mingit käsku ainult siis, kui tingimus vastab tõele. *if*-lause algab sõnaga :code:`if`, millele järgneb ümarsulgudes loogiline avaldis (avaldis mille väärtus saab olla tõene või väär) ja sellele omakorda järgneb direktiiv, mis täidetakse siis, kui avaldis on tõene. Sellele võib järgneda :code:`else if`, millele järgneb loogiline avaldis, mida kontrollitakse siis, kui esimese if-lause avaldis oli väär. *else if* osa võib puududa. Sõnale :code:`else` aga järgneb direktiiv, mis täidetakse siis, kui eelnevad loogilised avaldised olid väärad. *else*-osa võib ka puududa.

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

Programmis on näha, et testScore võib korraga täita mitut tingimust: 78 >= 70 ja 78 >= 60. Kui üks tingimus on täidetud, siis programm ei vaata enam järgmisi tingimusi ja läheb if-lause lõppu.

Stiil
------

Kehv stiil:

.. code-block:: java

    if (booleanExpression) {
        return true;
    } else {
        return false;
    }

Parem stiil:

.. code-block:: java

    return booleanExpression;
    
.. image:: /_images/condition.png

Allikas: http://thecodinglove.com/post/143122431685/that-moment-when

Tingimus *if*-lauses
-----------------------

Tingimus (*condition*) võib olla näiteks:

- muutuja, mis on *boolean*-tüüpi:

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
  
Sellisel juhul tuleb dubleerida *else*-haru.
  
Tingavaldis
-----------

Tingavaldist (*ternary operator*) saab kasutada, et *if*-lauset lühemalt kirja panna.

Süntaks:

.. code-block:: java

  condition ? expression-1 : expression-2;
  
Tingimus (*condition*) on boolean-tüüpi väärtus. *expression-1* ja *expression-2* peavad olema sama tüüpi.

Kui tingimus on tõene, käivita *expression-1*, vastasel juhul käivita *expression-2*.

Näide:

.. code-block:: java

   int a = 5;
   int b = 3;
   
   System.out.println("Bigger value is: " + (a > b) ? a : b); // Prints "Bigger value is: 5" to the console

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
---------------

Erinevalt *if-then* ja *if-then-else* lausetest, saab *switch*-lausel (lülitidirektiivil) olla palju võimalikke valikuid. 

Süntaks:

.. code-block:: java

    switch (expression) {
        case possibleValue-1: statements-1;
             break;
        ...
        case possibleValue-n: statements-n;
             break;
        default: default-statements;
    }
    
*default* väärtus on valikuline, ning selle direktiivid on juhuks kui ühtegi muud varianti ei kasutata.

Järgnevas näites *Example* deklareeritakse täisarv nimega "month", mille väärtus kirjeldab kuud. Kood annab väljundiks kuu nime vastavalt selle väärtusele, kasutades *switch*-lauset.

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
  
Järgnevas näites *AnotherExample* deklareeritakse täisarvud nimega "month" ja "daysOfMonth", mille väärtused kirjeldavad kuud ja selles sisalduvate päevade arvu. Kood annab väljundiks lause vastavalt väärtusele.

.. code-block:: java

  public class AnotherExample {
      public static void main(String[] args) {
          int month, daysOfMonth;
          
          switch (month) {
          case 4: case 6: case 9: case 11:
              daysOfMonth = 30;
              break;
          case 1: case 3: case 5: case 7: case 8: case 10: case 12:
              daysOfMonth = 31;
              break;
          case 2:
              daysOfMonth = 28;
              break;
          default:
              daysOfMonth = 0;
              System.out.println("Month is not valid");
          }
          System.out.println("Days: " + daysOfMonth);      
      }
  }

------

https://docs.oracle.com/javase/tutorial/java/nutsandbolts/if.html

https://docs.oracle.com/javase/tutorial/java/nutsandbolts/switch.html
