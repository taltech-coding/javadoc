.. |br| raw:: html

   <br />

   

Funktsioon (Meetod)
===================

Javas peavad kõik funktsioonid (ehk meetodid) olema deklareeritud klassides. Igale meetodi sisendparameetrile tuleb määrata objektitüüp. Sama tuleb teha ka meetodi poolt tagastatava väärtuse jaoks.

+---------------------------------------------------+------------------------------------------------------------------+
| Python                                            | Java                                                             |
+===================================================+==================================================================+
| Meetodi süntaks                                                                                                      |
+---------------------------------------------------+------------------------------------------------------------------+
|                                                   |                                                                  |
| .. code-block:: python                            | .. code-block:: java                                             |
|                                                   |                                                                  |
|     def func_name(var1, ...):                     |     visibilityType returnType methodName(varType varName, ...) { |
|                                                   |                                                                  |
+---------------------------------------------------+------------------------------------------------------------------+
| Meetodi näide                                                                                                        |
+---------------------------------------------------+------------------------------------------------------------------+
|                                                   |                                                                  |
| .. code-block:: python                            | .. code-block:: java                                             |
|                                                   |                                                                  |
|     def add_strings(s1, s2):                      |     public class StringAdder {                                   |
|         return s1 + s2                            |         public String addStrings(String s1, String s2) {         |
|                                                   |             return s1 + s2;                                      |
|                                                   |         }                                                        |
|                                                   |     }                                                            |
+---------------------------------------------------+------------------------------------------------------------------+

Javas on võimalik klassile, klassi meetoditele ning instansi muutujatele lisada ka **nähtavuse tase**. Tüüpiliselt on selleks public, mis tähendab, et klassi / meetodi / muutuja poole saab pöörduda kõikjalt projektist, kuid on ka teisi valikuid (mitte midagi, private, protected, ...), millest räägime hiljem.

Tüüpiliselt loome javas klassi meetodite kasutamiseks klassist objekti. See on tähtis juhul, kui meetodi töö oleneb objekti iseäärasustest.

.. code-block:: java
	
    public class Hello {
        public String name;
    	
        public Hello(String name) {
            this.name = name;
        }
    	
        public String sayHello() {
            return "Hello, " + this.name;
        }
    }

.. code-block:: java
	
	Hello john = new Hello("John");
	System.out.println(john.sayHello()); // => Hello, John

Kuid juhtudel, kus meetodi töö ei olene objekti iseäärasustest (näiteks ei kasutata ühtegi objekti andmevälja), on mõttekas lisada meetodile võtmesõna **static**.Niimoodi ei ole vaja meetodi kasutamiseks luua klassist objekti ning üldiselt öeldakse, et meetod kuulub klassile, mitte instansile (eraldi objektile).

.. code-block:: java
    
    public class StringAdder {
        public static String addStrings(String s1, String s2) {
            return s1 + s2;
        }
    }

.. code-block:: java
    
    System.out.println(StringAdder.addStrings("Hello", " world")); // => Hello world

Static meetodite ning muutujate poole pöördutakse klassinime abil ning need on klassidest loodud objektide vahel jagatud. St, et näiteks muutes static andmevälja väärtust ühes objektis, muutub ta kõigis objektides.
