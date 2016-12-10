==============
Võtmesõna this
==============
Object orienteeritud programeerimises võib olla sama nimega muutujaid rohkem kui üks, ja tavaliselt ongi. Selleks on selline asi nagu *this.variableName* mis määrab kindlaks, et tegemist on just selle classi muutujaga.

Koodi näites on konstructor milles on argumendiks **nimi** ja **id** ning see määrab klass muutujad mille nimed on samuti **name** ja **id** nendeks, mis oli ette antud.

.. code-block:: java

  public class Student {
  	private String name;
  	private int id;

  	Student(String name, int id) {
  		this.name = name;	//this.name on classi muutuja nimi ning lihtsalt name on argumendi muutuja
  		this.id = id;
  	}
  }

Seda ei pea kasutama ainult muutujate puhul. Seda on võimalik kasutada ka meetodite välja kutsumiseks, kui sellel pole eriti mõtet, kuna igal classis peaks niikuinii olema minimaalselt vähe informatsiooni teisete classide kohta.