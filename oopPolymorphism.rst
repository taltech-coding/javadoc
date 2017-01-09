===========
Polümorfism
===========
Polümorfismi idee on see, et see kirjeldab endale unikaalset käitumist ning samal ajal jagab ülemklassi mingit funktsionaalsust. Selleks, et polümorfismi saavutada, tuleb kasutada vähemalt ühte ülemklassi meetodit. See lubab kasutada sama koodi ja funktsioone erinevate andmetüüpidega, mille tulemuseks on rohkem üldised ning abstraktsed implementatsioonid. 

Vaatame näidet kujundite puhul, kus programm oskab joonistada kujundeid ekraanile. Programm oskab teha ristkülikuid (*rectangle*) ja tavalisi kujundeid. Kujundite joonistamiseks võib kasutada *Rectangle* klasse. Nendel kõigil on superclass *Shape*, mis on nende kõigi ühisosa. Shape võiks sisaldada kujundi värvi, positsiooni, suurust ja nii edasi koos meetoditega, mis neid väärtusi muudab. 

Koodinäites on näha kus *Rectangle* kasutab enda ülemklassi redraw meetodit kus ta joonistab just *Rectangeli*. Kui alamklass kasutab mingit ülemklassi meetodit siis kasutatakse :code:`@override` viidet.

.. code-block:: java

	public class Shape {
		private String color;

		public void setColor(String color) {
		    this.color = color;
		    redraw();
		} 

		void redraw() {
			// Drawing default state of each shape
		}
		
		// more instance variables and methods
		
	} // end of class Shape

.. code-block:: java

	public class Rectangle extends Shape {
		@override
		public void redraw() {
			// Drawing a specified shape of Rectangle with special parameters.
		}
	}

Selles koodinäites on välja toodud polümorfismi algeline näide, kasutades eelmiseid klasse.

.. code-block:: java
	
	public class Example() {
		public static void main(String[] args) {
			String redColor = "Red";
			String blueColor = "Blue";
			// Creates a default shape.
			Shape defaultShape = new Shape();
			// uses shape method setColor to set it's color to red.
			defaultShape.setColor(redColor);
			// uses shape metod redraw to redraw the object.
			defaultshape.redraw();

			// Creates a specific shaped object, a rectangle.
			Rectangle rectangle = new Rectangle();
			// Uses shape method setColor to set it's color to blue.
			rectangle.setColor(blue);
			// Uses rectangle object method to redraw the rectangle.
			rectangle.redraw();
		}
	}

