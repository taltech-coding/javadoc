===================
Koodi moduleerimine
===================

Koodi moduleerimine tähendab selle jaotamist väikesteks ja teineteisest võimalikult vähe sõltuvateks osadeks. Javas loetakse üheks mooduliks tavaliselt paketti (*package*), kuid see võib olla ka üks klass või terve alamprojekt ehk hulk pakette. Sisemine funktsionaalsus on teiste moodulite eest peidetud ning andmevahetus käib liideste kaudu.

Ühe mooduli ülesannet peaks ideaalis olema võimalik kirjeldada ühe lausega. Kui see pole võimalik, on tõenäoliselt mõistlik erineva funktsionaalsusega osad eraldi moodulitesse jagada.

Miks koodi moduleerida?
=======================

- Modulaarset koodi saab tükkidena arendada: mitu inimest võivad korraga sama projekti kallal töötada, ilma et peaksid teineteise koodis muudatusi tegema.
- Modulaarset koodi on lihtne testida: iga moodulit saab testida teistest sõltumatult.
- Modulaarse koodi haldamine on kergem: väheneb süsteemi keerukus ning muudatuste tegemine ühes moodulis ei mõjuta alati teisi.
- Modulaarne kood on taaskasutatav: mooduleid on võimalik luua nii, et üht ja sama moodulit saaks kasutada erinevates olukordades.
- Modulaarset koodi on lihtsam edasi arendada: uute funktsionaalsuste lisamiseks saab lisada uusi mooduleid.
- Modulaarne kood on loetavam: keeruliste süsteemide puhul on kergem neist aru saada, kui vaadata korraga ainult ühte tükki suurest süsteemist.
