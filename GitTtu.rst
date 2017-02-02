Git'i kasutamine TTÜs
----------------------

Sammud projekti Git'i panemisel:

.. code-block:: console

  git clone https://uniid@git.ttu.ee/ained/iti0011/uniid.git
  
Repositooriumi kloonimine enda arvutisse, kus *uniid* tuleb **asendada** enda Uni-ID-ga. Ainekood (iti0011) tuleks asendada vastava aine ainekoodiga.

Kui millegi pärast ei õnnestu repositooriumi kloonimine, siis tuleks kontrollida, kas kasutate ikka **https://** protokolli, mitte http://. Tuleks ka kontrollida, kas olete uniid ja parooli õigesti sisestanud (suur- ja väiketähed on erinevad!).

.. code-block:: console

  cd uniid
  
  mkdir EX00
  
  cd EX00
  
Siia kausta tuleks nüüd luua fail, näiteks *Main.java*.

.. code-block:: console

  git add Main.java
  
  git commit -m "Lühike kommentaar koodi lisamise kohta"
  
  git push origin master
  
Üles võib panna ka terve kausta:

.. code-block:: console

  git add EX00
  
  git commit -m "Lisan terve EX00 kausta"
  
  git push origin master
  
Tulemusena peaks tulema e-maili aadressile (mail.ttu.ee) kiri õnnestumise või ebaõnnestumise kohta, õnnestumise korral ka automaattestide tulemused. Peale tagasiside saamist võib funktsiooni täiendada, et vastus õige oleks. Sellisel juhul on vaja kood uuesti Git'i üles laadida:

.. code-block:: console

  git add Main.java
  
  git commit -m "Lühike kommentaar tehtud muudatuste kohta"
  
  git push origin master

  
Probleemide vältimiseks tuleks alati enne koodimuudatusi teha repositooriumile *git pull*. See tõmbab uusima versiooni serverist. Kui see samm jääb tegemata, võib juhtuda, et failide seis arvutis läheb konflikti serveris oleva seisuga.

Vaata rohkem git'i kohta: :doc:`Git`
