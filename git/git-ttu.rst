Giti kasutamine TTÜs
----------------------

Sammud projekti Giti panemisel:

.. code-block:: console

  git clone https://gitlab.cs.ttu.ee/UNIID/PROJECT.git
  
Repositooriumi kloonimine enda arvutisse, kus ``UNIID`` tuleb **asendada** enda Uni-ID-ga. ``PROJECT`` tuleks asendada vastavas aines määratud projekti nimega (näiteks ``iti0202-2019``).

Te näete oma projekte veebilehel: https://gitlab.cs.ttu.ee . Kui avate projekti, siis seal on näha ka terviklik projekti (salve) aadress. Saate aadressi kopeerida ja kloonimisel kasutada.

Kui millegipärast ei õnnestu repositooriumi kloonimine, siis tuleks kontrollida, kas kasutate ikka **https://** protokolli, mitte http://. Tuleks ka kontrollida, kas olete projekti, uniid ja parooli õigesti sisestanud (suur- ja väiketähed on erinevad!).

.. code-block:: console

  cd PROJECT
  
  mkdir EX00
  
  cd EX00
  
Siia kausta tuleks nüüd luua fail, näiteks ``Main.java`` (siin lihtsustatud näide, tegelikult tuleks luua ka pakett).

.. code-block:: console

  git add Main.java
  
  git commit -m "Lühike kommentaar koodi lisamise kohta"
  
  git push origin master
  
Üles võib panna ka terve kausta:

.. code-block:: console

  git add EX00
  
  git commit -m "Lisan terve EX00 kausta"
  
  git push origin master
  
Tulemusena peaks tulema e-maili aadressile (mail.ttu.ee) kiri õnnestumise või ebaõnnestumise kohta, õnnestumise korral ka automaattestide tulemused. Peale tagasiside saamist võib koodi täiendada, et tulemus õige oleks. Sellisel juhul on vaja kood uuesti Giti üles laadida:

.. code-block:: console

  git add Main.java
  
  git commit -m "Lühike kommentaar tehtud muudatuste kohta"
  
  git push origin master

  
Probleemide vältimiseks tuleks alati enne koodimuudatusi teha repositooriumile ``git pull``. See tõmbab uusima versiooni serverist. Kui see samm jääb tegemata, võib juhtuda, et failide seis arvutis läheb konflikti serveris oleva seisuga.

Vaata rohkem Giti kohta: :doc:`git`
