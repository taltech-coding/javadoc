==========
Rekursioon
==========

Mõiste vms kirjeldamine kasutades mõistet ennast

Programmeerimises: probleemi lahendamiseks kutsub funktsioon ennast välja

Faktoriaali näide
-----------------

Faktoriaal mingist arvust on kõikide arvude korrutis alates 1-st kuni selle arvuni:

.. n! = 1            , kui n = 0
   n! = (n - 1)! x n , kui n > 0

.. math::

  n! =
  \begin{cases}
    1                 & \quad \text{if } n = 0\\
    (n - 1)! \times n & \quad \text{if } n > 0
  \end{cases}
   
Fibonacci jada
--------------

.. math::

  F_1 = 1
  F_2 = 1
  F_n = F_{n-1} + F_{n-2}
  
