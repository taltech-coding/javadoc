====================
Meetodi ülelaadimine
====================

Üldjuhul on meetodite nimed klassi piires unikaalsed. Sellegipoolest on võimalik luua ühes klassis mitu samanimelist meetodit. Sel juhul on tegu meetodi ülelaadimisega (*overloading*).

Ülelaadimise korral erinevad samanimelised meetodid argumentide arvu ja/või tüüpide poolest. Meetodi väljakutsumisel eristatakse neid automaatselt selle põhjal, millised argumendid on antud.

(näide)

public class DataArtist {
    ...
    public void draw(String s) {
        ...
    }
    public void draw(int i) {
        ...
    }
    public void draw(double f) {
        ...
    }
    public void draw(int i, double f) {
        ...
    }
}


Kui muutujaid on sama palju ning nende tüübid on samad, siis ülelaadimine ei õnnestu, kuna kompilaator ei suuda neid eristada. Seetõttu ei piisa ka sellest, kui tagastatav andmetüüp on erinev.