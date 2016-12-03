Overload ja Override
================================================

Tavaliselt tekitavad antud terminid segadust, kuid nendesse natuke süvenedes on arusaadav, et terminite taga olevad kontseptsioonid on piisavalt lihtsad.

*Overload* 
----------------------

Tegemist on meetodi overloadiga Javas, kui kahel või rohkemal meetodil **samas klassis** on sama meetodi nimi, kuid erinevad sisestatud argumendid. Overloading toimub kompileerimise ajal. 

Meetodi overload on korrektne siis, kui täidetud on üks või mõlemad tingimused:

    1. Sisestatud argumentide **arv** meetoditesse on erinev.

    2. Argumentide **tüübid** on erinevad. (nt. enne oli int, nüüd on float)


Tegemist **ei ole** overloadiga, ning kood tekitab komppilatsioonivea, kui:

    1. Meetodite nimed on samad, argumentide nimed ja tüübid on samad, nende arv on sama, kuid tagastustüüp (return type) on erinev.
    
    2. Erinevad on ainult meetodisse sistatud argumentide nimed.


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

Meetodite override on täiesti erinev overload'ist. Kui tegemist on alam ja ülemklasiga, ning mõlemas klassis esineb **täiesti sama** meetodi nimega, tagastustüübiga, parameetrite arvuga ning tüüpidega meetod, kuid ainaks erinevuseks on meetodi sisu, siis on tegemist override-ga. Override tekib koodi töö ajal, mitte kompilatsiooni ajal nagu Overload'i puhul.

Nüüd on sobilik tuua väike näide, mis illustreerib override't.


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

Kui ülemklassis tagastab meetod *someMethod()* numbri 3, siis alamklassis tagastab täpselt samasugune meetod numbri 4. 





