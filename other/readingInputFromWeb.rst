Sisendi lugemine veebist
========================

URL'i parsimine
---------------

URL klass pakub kasutajatele mitmeid erinevaid meetodeid, mis lubavad teha päringuid URL objektide kohta. Sellistelt objektidelt võib küsida nende protokolli, *host*'i nime, pordi numbrit, *authority*'t, päringut, faili nime, *path*'i ning viidet.

Selleks on meetodid:

- *getProtocol()* - tagastab URL'i protokolli nime
- *getAuthority()* - tagastab URL'i *authority* komponendi
- *getHost()* - tagastab URL'i võõrustaja nime
- *getPort()* - tagastab *Integer*'i kujul pordi numbri, juhul kui see puudub tagastab -1
- *getPath()* - tagastab URL'i *path* komponendi
- *getQuery()* - tagastab URL'i päringu komponendi
- *getFile()* - tagastab *path* komponendi ning *getQuery()* väärtuse, kui see on olemas
- *getRef()* - tagastab URL'i *reference* komponendi

Oluline on meeles pidada, et iga URL ei sisalda kõiki eelloetletud komponente, need meetodid on olemas, sest tihti kasutatakse URL'e, milles sisalduvad mõned või kõik nendest komponentidest. URL klass on üpris HTTP keskne.

Koodinäide:

.. code-block:: java

    import java.net.*;
    import java.io.*;

    public class ParseURL {
        public static void main(String[] args) throws Exception {

            URL aURL = new URL("http://example.com:80/docs/books/tutorial"
                            + "/index.html?name=networking#DOWNLOADING");

            System.out.println("protocol = " + aURL.getProtocol());
            System.out.println("authority = " + aURL.getAuthority());
            System.out.println("host = " + aURL.getHost());
            System.out.println("port = " + aURL.getPort());
            System.out.println("path = " + aURL.getPath());
            System.out.println("query = " + aURL.getQuery());
            System.out.println("filename = " + aURL.getFile());
            System.out.println("ref = " + aURL.getRef());
        }
    }
    
Koodinäide tagastab:

.. code-block:: java

    protocol = http
    authority = example.com:80
    host = example.com
    port = 80
    path = /docs/books/tutorial/index.html
    query = name=networking
    filename = /docs/books/tutorial/index.html?name=networking
    ref = DOWNLOADING


URL'ilt lugemine
----------------

URL'i kohta saab välja kutsuda meetodi *openStream()*, mis loob voo, millest saab URL'i sisu välja lugeda. *openStream()* meetod tagastab *java.io.InputStream* objekti, seega on URL'ilt lugemine sarnane näiteks failist andmete lugemisega.

Järgnev koodinäide kasutab *openStream()* meetodit, et saada sisendvoog URL'ist http://www.oracle.com/. Seejärel kasutatakse *BufferedReader*'it, et lugeda vajalikku infot. Kõik, mis loetakse sisse, kopeeritakse *output* voogu.

.. code-block:: java

    import java.net.*;
    import java.io.*;

    public class URLReader {
        public static void main(String[] args) throws Exception {

            URL url = new URL("http://www.oracle.com/");
            
            BufferedReader in = new BufferedReader(
            new InputStreamReader(url.openStream()));

            String inputLine;
            while ((inputLine = in.readLine()) != null)
                System.out.println(inputLine);
            in.close();
        }
    }
  
Kui panna antud kood tööle, peaks nägema konsoolis veebilehe  http://www.oracle.com/ HTML koodi ning tekstilist sisu; juhul kui ei suudeta leida Oracle'i serverit või URL'i lugemisel tekib mõni muu viga, kuvatakse terminalis hoopis veateadet.
