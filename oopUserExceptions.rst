===========================
Kasutaja defineeritud erind
===========================

Peale juba olemasolevate erindite on võimalik kasutada ka enda defineerituid erindeid.

Kasutaja defineeritud erindi näide:

.. code-block:: java

    class CustomException extends Exception {
        String customMessage;

        CustomException(String customMessage) {
            this.customMessage = customMessage;
        }
        
        @Override
        public String toString() {
            return "CustomException message: " + customMessage;
        }
    }

CustomExceptioni kasutamine:

.. code-block:: java

    public static void main(String[] args) {
        try {
            throw new CustomException("This is a user defined exception.");
        } catch (CustomException ex) {
            System.out.println(ex);
        }
    }

.. code::

    CustomException message: This is a user defined exception.

Kui erind laiendab Exception klassi, on see *checked* erind. *Unchecked* erindi tegemiseks tuleb laiendada RuntimeException klassi.

Siinkohal oleks mõistlik tähele panna, et erindi töö ei ole programmiloogikat kontrollida, erind peab arendajat veast teavitama. See, kuna erindit visata, peab olema kirjas programmis, mitte erindis endas. Kasutaja defineeritud erindid ongi sellepärast kasulikud, et arendaja saab erindi väljastatud sõnumit enda jaoks kohandada, et tal oleks parem ülevaade sellest, mis programmi töös valesti läks.
