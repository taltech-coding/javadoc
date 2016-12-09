Set ehk hulk
============

Set ehk hulk on kollektsioon või kogum elementidest, milles ükski liige ei kordu. Javas on set tegelikult interface ehk liides. Interface'i kohta leiab rohkem informatsiooni objektorienteeritud koodi kirjutamist käsitlevate teemade juures. Javas on mitmeid erinevaid hulga tüüpe nt *HashSet*, *AbstractSet*, *LinkedHashSet*, *TreeSet*, *ConcurrentSkipListSet*, *EnumSet* jt. Objektorienteeritud mõttes implementeerivad nad kõik Set liidest. Sisuliselt on aga kõigil neil hulkadel sarnased algsed omadused (see, et üksiki liige ei kordu) ning erinevat tüüpi set'ide kohta saab kutsuda välja sarnsaeid meetodeid.

HashSet
-------

Üks võimalik hulga tüüpidest on HashSet<E>. HashSet ei hoia meeles sinna paigutatud elementide järjekorda, erinevalt mõnest teisest hulgast on võimalik HashSet'is hoida ka null elementi. Seda on saab luua nõnda:


.. code-block:: java

  public class SetExamples {
  
    public static void main(String[] args) {
    
      Set<Integer> exampleSet1 = new HashSet<>();
      
      //or
      
      HashSet<String> exampleSet2 = new HashSet<>();
        
    }
  }
  
  
Set'ide kasutamiseks on javas mitmeid erinevaid meetodeid, neist esimene on *add(E e)*, mis lisab hulka ühe elemendi juhul kui seda juba hulgas pole. Teine kasulik meetod on *clear()*, mis kustutab kõik hulgas olevad elemendid. *contains(Object o)* tagastab boolean väärtuse (*true*/*false*) selle kohta, kas konkreetne objekt esineb hulgas või mitte. Seda, kas set'is on elemente või on see tühi saab kontrollida meetodi *isEmpty()* abil, mis tagastab true juhul kui hulgas pole ühtegi elementi. *remove(Object o)* eemaldab soovitud elemendi hulgast, kui see set'is olemas on ning meetod *size()* tagastab hulgas olevate elementide arvu ehk set'i pikkuse.
  

.. code-block:: java

  public class SetExamples {
  
    public static void main(String[] args) {
      
      HashSet<Integer> exampleSet = new HashSet<>();
      
      //adds 6 to exampleSet
      exampleSet.add(6);
      
      //removes all elements from exampleSet
      exampleSet.clear();
      
      //returns false because exampleSet is empty
      boolean containsSix = exampleSet.contains(6);
      
      //returns true because exampleSet is empty
      boolean empty = exampleSet.isEmpty();
      
       exampleSet.add(1);
       exampleSet.add(6);
       exampleSet.add(666);
       
       //removes 1 from exampleSet
       exampleSet.remove(1);
       
       //length is equal to 2
       int length = exampleSet.size();
          
    }
  }
  
LinkedHashSet
-------------

LinkedHashSet on sarnane HashSet'iga, kuid erinevalt viimasest sälitab LinkedHashSet elementide järjekorra.
  
