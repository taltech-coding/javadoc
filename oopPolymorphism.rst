===========
Polümorfism
===========
Polümorfismi idee on see, et see kirjeldab endale unikalset käitumist ning samal ajal jagab ülemklassi mingit funktsionaalsust. Selleks et polümorfismi saavutada, tuleb kasutada vähemalt ühte ülemklassi meetodit. See lubab kasutada sama koodi ja funktsioone erinevate andmetüüpidega, mille tulemuseks on rohkem üldised ning abstraktsed implementsioonid. 

Vaatame näidet kujundite puhul, kus programm oskab joonistada kujundeid ekraanile. Programm oskab teha ristkülikuid (Rectable) ja ovaale (Oval). Kujundite joonistamiseks võib kasutada klasse *Rectangle* ja *Oval* klasse. Nendel kõigil on superclass *Shape*, mis on neil kõigil ühis osa. Shape võiks sisaldada kujuundi värvi, positsiooni, suurust ja nii edasi koos meetoditega, mis neid väärtusi muudab. 

Koodi näites on näha kus *Rectangle* kasutab enda ülemklassi redraw meetodit kus ta joonistab just *Rectangeli*. Kui alamklass kasutab mingit ülemklassi meetodit siis on kasutules @override viidet.

.. code-block:: java

	public class Shape {
		// Must be importedfrom java.awt
		private Color color;

		public void setColor(Color color) {
		    this.color = new color;
		    redraw();
		} 

		void redraw() {
			// Drawing default state of each shape
		}

		// more instnce variables and methods

	} // end of class Shape

.. code-block:: java

	public class Rectangle extends Shape {
		@override
		public void redraw() {
			// Drawing a specified shape of Rectangle with special parameters.
		}
	}

Siin koodi näites on välja toodid polümorfismi algelist näidet kasutades eelmiseid classe.

.. code-block:: java
	
	// Requires Color import
	public class Example() {
		public static void main(String[] args) {
			// Requires imports
			Color red = new Color(1,0,0);
			Color blue = new Color(0,1,0);
			// Creates a default shape.
			Shape defaultShape = new Shape();
			// uses shape method setColor to set it's color to red.
			defaultShape.setColor(red);
			// uses shape metod redraw to redraw the object.
			defaultshape.redraw();

			// Creates a specific shaped object.
			Rectangle rectangle = new Rectangle();
			// Uses shape method setColor to set it's color to blue.
			rectangle.setColor(blue);
			// Uses rectangle object method to redraw the object.
			rectangle.redraw();
		}
	}

