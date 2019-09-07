Overload ja Override
================================================

Tavaliselt tekitavad antud terminid segadust, kuid nendesse natuke süvenedes on arusaadav, et terminite taga olevad kontseptsioonid on üpris lihtsad.

*Overload* 
----------------------

Tegemist on meetodi ülelaadimisega Javas, kui kahel või rohkemal meetodil **samas klassis** on sama meetodi nimi, kuid erinevad sisestatavad argumendid. Ülelaadimine toimub kompileerimise ajal. 

Meetodi ülelaadimine on korrektne siis, kui täidetud on üks või mõlemad tingimused:

1. Sisestatud argumentide **arv** meetoditesse on erinev.

2. Argumentide **tüübid** on erinevad. (nt. enne oli int, nüüd on float)


Tegemist **ei ole** ülelaadimisega, ning kood tekitab kompilatsioonivea, kui:

1. Meetodite nimed on samad, argumentide nimed ja tüübid on samad, nende arv on sama, kuid tagastustüüp (*return type*) on erinev.
    
2. Erinevad on ainult meetodisse sisestatud argumentide nimed.


.. code-block:: java
    
                //compiler error - can't overload based on the type returned 
                //(one method returns int, the other returns a float):    
                
                int changeDate(int Year);  
                float changeDate (int Year);    
                
                //compiler error - can't overload by changing just 
                //the name of the parameter (from Year to Month):    
                
                int changeDate(int Year);   
                int changeDate(int Month);  
                 
                //valid case of overloading, since the methods
                //have different number of parameters:        
                
                int changeDate(int Year, int Month);  
                int changeDate(int Year);    
                
                //also a valid case of overloading, since the   
                //parameters are of different types:    
                
                int changeDate(float Year);  
                int changeDate(int Year); 

*Override* 
----------------------

Meetodite ülekirjutamine on täiesti erinev ülelaadimisest. Kui tegemist on alam- ja ülemklassiga, ning mõlemas klassis esineb **täiesti sama** nime, tagastustüübi (või tagastustüüp on originaaltüübi alamtüüp), parameetrite arvu ning tüüpidega meetod, kuid ainsaks erinevuseks on meetodi sisu, siis on tegemist ülekirjutamisega. Ülekirjutamine tekib koodi töö ajal, mitte kompilatsiooni ajal nagu ülelaadimise puhul.

Nüüd on sobilik tuua väike näide, mis illustreerib ülekirjutamist:


.. code-block:: java

  public class Parent {
    
    public int someMethod() {
       return 3;
       }
    }
    
    
  public class Child extends Parent{
    
    @Override
    public int someMethod() {
       return 4;
       }
    }

.. code-block:: java

    public class Main {

        public static void main(String[] args) {

            Parent parent = new Parent();
            Child child = new Child();

            System.out.println(parent.someMethod());
            System.out.println(child.someMethod());

        }
    }

Tekitame *main* meetodi, kus võib koodi testida. Kui ülemklassi objekt *parent* tagastab meetodis *someMethod()* numbri 3, siis alamklassis *child* tagastab täpselt samasugune meetod numbri 4. 





