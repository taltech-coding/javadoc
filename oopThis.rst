==============
Võtmesõna this
==============
Objektorienteeritud programmeerimises võib olla sama nimega muutujaid rohkem kui üks, ja tavaliselt ongi. Selleks on selline asi nagu *this.variableName* mis määrab kindlaks, et tegemist on just selle klassi muutujaga.

Koodi näites on konstruktor milles on argumendiks **nimi**, **id** ja õpilase **tag** ning see määrab klassisisesed muutujad, mille nimed on samuti **name** ja **id**, lisaks on klassi muutuja, mille nimi ei kattu argumendi muutujaga, millele ei ole vaja ette panna *this.* kuid seda võib teha.

.. code-block:: java

  public class Student {
  	private String name;
  	private int id;
  	private String tagName;
  	private int grade;
  	private boolean enRolled = false;

  	Student(String name, int id, String tag, int grade) {
  		// this.name is a private variable specific to the class, while name by it self is an argument.
		this.name = name;	
  		// this.id is a private variable specific to the class, while id by it self is an argument.
		this.id = id;
		// The argument name tag, does not overlap with the variable name tagName, 
		// 	so there is no need to use this.tagName, however you can use it.
  		tagName = tag 	
		// We can also use this. on methods to specify that we are using this class methods.
  		this.initializegrades(grade); 
  		// but there are no need use this. in order to use the class method
		enroll(); 
  	}

  	private void initializeGrades(int grade) {
  		this.grade = grade;
  	}

  	private void enroll() {
  		this.enRolled = !enRolled;
  	}
  }

Konstruktoripõhine näide, kus ühe konstruktori sees kutsutakse teine konstruktor välja:

.. code-block:: java

	public class Rectangle {
		private int x, y;
		private int width, height;

		public Rectangle() {
			this(0, 0, 1, 1);
		}
		
		public Rectangle(int width, int height) {
			this(0, 0, width, height);
		}
		
		public Rectangle(int x, int y, int width, int height) {
        		this.x = x;
        		this.y = y;
        		this.width = width;
        		this.height = height;
    		}
	}

Seda ei pea kasutama ainult muutujate puhul. Seda on võimalik kasutada ka meetodite välja kutsumiseks, millel aga pole eriti mõtet, kuna igal klassis peaks niikuinii olema minimaalselt informatsiooni teiste klasside kohta.
