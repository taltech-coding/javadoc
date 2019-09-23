Faili kirjutamine
==================

BufferedWriter
---------------

Java 8 puhul mõistlik kasutada järgmist:

.. code-block:: java

    import java.io.BufferedWriter;
    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Path;
    import java.nio.file.Paths;

    /**
     * Example usage of BufferedWriter in Java 8.
     */
    public class BufferedWriterExampleJava8 {

        public static void main(String[] args) {
        
            Path path = Paths.get("path", "to", "example.txt");
            try (BufferedWriter writer = Files.newBufferedWriter(path)) {
                writer.write("Hello World!\n");
            } catch (IOException e) {
                System.out.println("IOException:" + e.getMessage());
                e.printStackTrace();
            }
        }
    }

BufferedWriter kasutab puhverdamist ning on efektiivne. Puhverdamine tähendab seda, et iga write operatsioon ei kirjuta andmeid kettale. Pigem puhverdatakse andmeid mingi hetk mälus. Kui teatud hulk andmeid on mälus juba puhverdatud (puhver saab täis), kirjutatakse need faili.

Fail pannake peale **try**-plokki kinni.

Olemasolevasse faili kirjutamine.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Olemasolevasse faili kirjutamiseks tuleb esmalt kontrollida, kas see eksisteerib. Faili saab teksti lisada, luues ``BufferedWriter`` objekti koos lisaparameetriga ``StandardOpenOption.APPEND``.

.. code-block:: java

    Path path = Paths.get("somefile.txt");
    boolean fileExists = Files.exists(path);
    
    if (fileExists) {
        try (BufferedWriter writer = Files.newBufferedWriter(path, StandardOpenOption.APPEND)) {
            writer.write("Append to text!\n");
        } catch (IOException e) {
            System.out.println("IOException:" + e.getMessage());
            e.printStackTrace();
        }
    }
    
    
    
PrintWriter
-----------

.. code-block:: java

    try (PrintWriter printWriter = new PrintWriter("my_numbers.txt")) {
        printWriter.println(1);
        printWriter.println(2);
        printWriter.println(3);

    } catch (FileNotFoundException e) {
        System.out.println("file not found");
    }

BufferedWriter
---------------

Enne Java 7-t:

.. code-block:: java

    import java.io.BufferedWriter;
    import java.io.FileWriter;
    import java.io.IOException;

    /**
     * BufferedWriter usage example.
     */
    public class BufferedWriterExample {
        public static void main(String[] args) {
            try (BufferedWriter writer = new BufferedWriter(new FileWriter("file.txt"))) {
                writer.write("Hello!\n");
            } catch (IOException e) {
                System.out.println("Error writing file:" + e.getMessage());
                e.printStackTrace();
            }
        }
    }
    
    
