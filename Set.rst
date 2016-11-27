Set ehk hulk
================================================
Set ehk hulk on kollektsioon või kogum elementidest, milles ükski liige ei kordu. Javas on set tegelikult interface ehk liides. Interface'i kohta leiab rohkem informatsiooni objektorienteeritud koodi kirjutamist käsitlevate teemade juures. Javas on mitmeid erinevaid hulga tüüpe nt HashSet, AbstractSet, LinkedHashSet, TreeSet, ConcurrentSkipListSet, EnumSet jt. Objektorienteeritud mõttes implementeerivad nad kõik Set liidest. Sisuliselt on aga kõigil neil hulkadel sarnased algsed omadused (see, et üksiki liige ei kordu) ning erinevat tüüpi set'ide kohta saab kutsuda välja sarnsaeid meetodeid.

*HashSet*
---------
Üks võimalik hulga tüüpidest on HashSet<E>. Seda on võimalik luua nõnda:

.. code-block:: java

  public class SetExamples {
  
    public static void main(String[] args) {
    
      Set<Integer> exampleSet1 = new HashSet<>();
      
      //or
      
      HashSet<String> exampleSet2 = new HashSet<>();
        
    }
  }
