Gitlabi kasutamine suuremas projektis
=====================================

Suuremate projektide puhul on lisaks tavalisele Git'ile võimalik Gitlabis kasutada ka muud toetavat funktsionaalsust, mis näiteks meeskonnana projekti arendades muudab töökorralduse palju lihtsamaks. Gitlabile sarnased võimalused on olemas ka teistes keskondades nagu Github ja Bitbucket. 


Ülesanded (*issue*)
-------------------

Tööülesandeid on hea jaotada kasutades Gitlabi *issue*'sid. Iga uue funktsionaalsuse loomise, veaparanduse või muu tegevuse jaoks saab luua Gitlabis ülesande, kuhu on lühidalt kirjutatud, mida teha vaja on. Ülesannetele saab määrata ka sildid (*labels*), mis võimaldavad nende olemust kiiremini haarata. Näiteks veaparanduse ülesandele võiks panna külge sildi *bug*. Igale ülesandele saab määrata ka isiku, kes selle töö ära tegema peab ja vahest on hea panna ka kuupäev, millal töö valmis olema peab.

.. image:: /_images/gitlab_issues.png


Ülesannete lahendamine ja harud
-------------------------------

Tavaliselt on projekti põhikood alati *master* harus. 

Ülesannete lahendamiseks on kasulik teha eraldi Git'i haru. Seda saab teha nii lokaalselt enda Git'i salvest kui ka läbi Gitlabi veebiliidese. Lokaalselt saab läbi Git'i käsurea teha uue haru järnevalt: 

`git checkout -b "UUS-HARU"`

Siin pannakse uue haru nimeks "UUS-HARU". Arusadavuse parandamiseks hea on panna harule nimi, mis on lahendatava ülesande sisuga sarnane. Näiteks "#1-create-readme", siin #1 viitab Gitlab'i ülesande id-le.

Samamoodi saab lokaalselt uue haru luua kasutades ka IntelliJ'd. Menüüst valida `VCS -> Git -> Branches... -> New Branch`.

Teine võimalus haru tegemiseks on Gitlab'i veebileht. Avades lahendatava ülesande lehekülje Gitlabis on võimalik valida "**Create merge request**" mille puhul tehakse uus haru, kuhu kood lisada ja kohe ka *merge request*. Valides kõrvalt väiksema nupuga valiku, saab teha ka ainult uue haru ja *merge requesti* tegemise jätta hiljemaks.

.. image:: /_images/gitlab_issue_merge_request_submenu.png
   :scale: 50

Peale ülesandega seotud haru tegemist saab vastavas harus ülesande ära lahendada, töö *commit*'ida ning Gitlab'i *push*'ida ning seejärel liikuda *mergemise* sammu juurde. Käsurealt tehtud töö Gitlab'i samanimelisse harusse *push*'imiseks saab teha järnevalt:

`git push -u origin UUS-HARU`

Siin on "UUS-HARU" haru, mis tekib ka Gitlab'i.


Harude liitmine (*merge*)
-------------------------

Ülesande lahendamise lõpetamisel on vaja see mõne teise haruga ühendada. Üldjuhul on kõik asjad vaja lõpuks liita *master* haruga. Liitmiseks on samuti mitu erinevat võimalust, kas teha seda lokaalselt käsureal, IntelliJ'ga või läbi Gitlab'i.

Kui Gitlab'is minna lehele "**Merge Requests**" ja valida sealt "**New merge request**", siis saab teha uue "soovi" harude liitmiseks. *Source* ehk allika haruks valida haru, kus on ülesande lahendus ja üldjuhul *target* haru võib jääda *master*'iks.

.. image:: /_images/gitlab_merge_request.png

Harude ühendamise saab teha läbi Gitlab'i lihtsalt kui ei ole konflikte. 

.. image:: /_images/gitlab_merge.png
   :scale: 50

Kui harude liitmisel esineb konflikte, siis tuleb liitmine teostada käsitsi ja lokaalselt. Väiksemate konfliktide puhul pakub Gitlab ise ka nuppu "**Resolve Conflicts**", siis võib soovi korral seda ka brauseris teha.

.. image:: /_images/gitlab_merge_conflict.png
   :scale: 50

Vajutades nupule "**Merge locally**" on kõik sammud käsurealt harude liitmiseks ilusti välja toodud. Sama konfliktide lahendamise ja harude liitmise saab teha muidugi ka läbi IntelliJ'ga.

.. image:: /_images/gitlab_merge_locally.png
   :scale: 50

Käsurealt konflikte lahendma asudes on esimeseks sammuks muudatuste Gitlab'ist alla laadimine ja liidetavasse harusse liikumine.

.. code-block:: none

  git fetch origin
  git checkout -b HARU-MIDA-LIITA origin/HARU-MIDA-LIITA

Nüüd saab üle vaadata harus olevad muudatused ja liikuda edasi näiteks *master* haruga ühendamise juurde.

.. code-block:: none

  git fetch origin
  git checkout origin/master
  git merge --no-ff HARU-MIDA-LIITA

Kui liitmisel tekib konflikte, siis tuleb need käsitsi ära parandada, ehk valida millised muudatused jäävad alles.

Peale liitmise lõpetamist muudatused jälle üles *push*'ida.

.. code-block:: none

  git push origin master


Veel infot:

* https://docs.gitlab.com/ee/topics/gitlab_flow.html
* https://docs.gitlab.com/ee/university/training/topics/merge_conflicts.html