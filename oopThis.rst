==============
Võtmesõna this
==============
Objektorienteeritud programmeerimises võib olla sama nimega muutujaid rohkem kui üks, ja tavaliselt ongi. Selleks on selline asi nagu *this.variableName* mis määrab kindlaks, et tegemist on just selle klassi muutujaga.

Koodinäites on konstruktor, milles on argumentideks **name**, **id**, **tag** ja **grade**, ning see määrab klassisisesed muutujad, mille nimed osaliselt kattuvad (**name** ja **id**). Lisaks on muutuja tagName, mille nimi ei kattu argumendi muutujaga ning järelikult pole vaja selle ette panna *this.*, kuid seda võib teha. Peale selle kasutatakse argumenti *grade* veel omakorda argumendina objekti meetodis, kus väärtustatakse hinne ära.

.. code-block:: java

  public class Student {
  	private String name;
  	private int id;
  	private String tagName;
  	private int grade;
  	private boolean enRolled = false;

  	Student(String name, int id, String tag, int grade) {
  		// this.name is a private variable specific to the object, while name by it self is an argument.
		this.name = name;	
  		// this.id is a private variable specific to the object, while id by it self is an argument.
		this.id = id;
		// The argument name tag does not overlap with the variable name tagName, 
		// 	so there is no need to use this.tagName, however you can use it.
  		tagName = tag 	
		// We can also use this. on methods to specify that we are using this objects methods.
  		this.initializegrades(grade); 
  		// but there is no need use this in order to use the objects methods.
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
