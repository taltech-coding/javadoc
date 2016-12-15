==============
Võtmesõna this
==============
Object orienteeritud programeerimises võib olla sama nimega muutujaid rohkem kui üks, ja tavaliselt ongi. Selleks on selline asi nagu *this.variableName* mis määrab kindlaks, et tegemist on just selle classi muutujaga.

Koodi näites on konstructor milles on argumendiks **nimi**, **id** ja õpilase **tag** ning see määrab klass muutujad mille nimed on samuti **name** ja **id**, lisaks on klassi muutuja mille nimi ei kattu argumendi muutujaga, millele ei ole vaja ette panna *this.* kuid võib panna.

.. code-block:: java

  public class Student {
  	private String name;
  	private int id;
  	private String tagName;

  	Student(String name, int id, String tag) {
  		this.name = name;	//this.name is a private variable specific to the class, while name by it self is an argument.
  		this.id = id;	// this.id is a private variable specific to the class, while id by it self is an argument.
  		tagName = tag 	// the argument name tag, does not overlap with the variable name tagName, so there is no need to use this.tagName, however you can use it.
  	}
  }

Seda ei pea kasutama ainult muutujate puhul. Seda on võimalik kasutada ka meetodite välja kutsumiseks, kui sellel pole eriti mõtet, kuna igal classis peaks niikuinii olema minimaalselt vähe informatsiooni teisete classide kohta.