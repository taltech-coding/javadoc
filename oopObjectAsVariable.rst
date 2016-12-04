===============
Objekt muutujas
===============

Lisaks primitiivsetele andmetüüpidele võime muutuja tüübiks määrata ka mõne klassi. Sel juhul saab muutuja väärtuseks anda selle klassi instantse ehk objekte.

(näide)

Täpsemalt öeldes hakkab muutuja sellele objektile viitama. Samale objektile võib viidata üheaegselt mitu muutujat – tegu on ikkagi üheainsa objektiga. Iga muudatus, mida selles objektis teeme, mõjutab kõiki muutujaid korraga.

(arraylisti näide)

Kui me tahame teha nii, et ühe muutuja kaudu objektis tehtud muudatus ei mõjutaks teisi, tuleb meil teha sellest objektist koopia. (viide clone meetodi kirjeldusele teises dokumendis)

Objekt argumendina
------------------

Nagu teisi muutujaid, saab ka objekte kasutada funktsioonide argumentidena. Taaskord tuleb meeles pidada, et kaasa ei anta mitte koopiat objektist, vaid viide. See tähendab, et kui funktsiooni sees meie objekti kuidagi muudetakse, siis need muudatused on püsivad.

(Näide)

Kui me ei tea täpselt, kuidas funktsioon töötab, ning eesmärgiks pole objekti sisu muuta, oleks mõistlik eelnevalt objekt kloonida. Siis saame klooni argumendina kaasa anda ning objekti algne sisu säilib olenemata funktsiooni sisust.

(Näide)