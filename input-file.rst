========================
Sisendi lugemine failist
========================
Javas võib sisend-väljud näha keeruline, kuid see pole halb. Sellega saavutatakse seda, et nii klaviatuurilt kui ka failist saab andmeid lugeda kõrgema kihi objektidega nagu BufferedReader või Scanner. Lisaks sellele on veel täiendav võimalus Files.readAllLines().

Kasutades Try with meetodit ei ole vaja manuaalselt lugemis meetodit kinni pannal. Juhul kui ei kasuta try with resources siis tuleb teha **finally** block kus pannakse lugemis meetod kinni. All pool on ka sellest näide.

BufferedReader
--------------

.. code-block:: java

    import java.io.BufferedReader;
    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Path;
    import java.nio.file.Paths;

    /**
     * BufferedReader usage example.
     */
    public class BufferedReaderExampleJava8 {
        public static void main(String[] args) {
            Path path = Paths.get("path", "to", "file.txt");
            try (BufferedReader reader = Files.newBufferedReader(path)) {
                while (true) {
                    String line = reader.readLine();
                    if (line == null) break;
                }
            } catch (IOException e) {
                System.out.println("Error reading file:" + e.getMessage());
                e.printStackTrace();
            }
        }
    }

Files.readAllLines(Path)
------------------------

:code:`Files.readAllLines(Path)` annab võimaluse ühe reaga saada kätte järjend failis olevatest ridadest.

.. code-block:: java

    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Path;
    import java.nio.file.Paths;
    import java.util.List;

    /**
     * Files.readAllLines(Path) usage example.
     */
    public class FilesExample {
        public static void main(String[] args) {
            Path path = Paths.get("path", "to", "file.txt");
            try {
                List<String> lines = Files.readAllLines(path);

            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

Scanner
-------

Scanner võib olla tuttav standardsisendi lugemisest. Scanner (nagu ka teised voogudega tegelevad objektid) on võimalikult abstraktne ning lubab infot lugeda nii standardsisendist (klaviatuurilt) kui ka failist.

Järgev koodinäide loeb sisenfailist arve. Kuna :code:`Scanner` objektil on olemas meetod arvude tuvastamiseks (:code:`hasNextInt()`) ja lugemiseks (:code:`nextInt()`), saab sellega väikse vaevaga arvud failist kätte.

.. code-block:: java

    import java.io.IOException;
    import java.nio.file.Path;
    import java.nio.file.Paths;
    import java.util.Scanner;

    /**
     * Scanner usage example.
     */
    public class ScannerExample {
        public static void main(String[] args) {

            Path path = Paths.get("path", "to", "numbers.txt");
            try (Scanner scanner = new Scanner(path)) {
                while (scanner.hasNext()) {
                    if (scanner.hasNextInt()) {
                        System.out.println("Got a number:" + scanner.nextInt());
                    } else {
                        System.out.println("Not a number:" + scanner.next());
                    }
                }
            } catch (IOException e) {
                System.out.println("Error reading file:" + e.getMessage());
                e.printStackTrace();
            }
        }
    }

    
Erinevaid näiteid
------------------


Erinevad näited kombineeritud ühte faili:

.. code-block:: java

	import java.io.*;
	import java.nio.file.Files;
	import java.nio.file.Path;
	import java.nio.file.Paths;
	import java.util.List;
	import java.util.Scanner;
	import java.util.stream.Stream;

	public class ReadFile {
		// Filename to be read.
	    public static final String FILENAME = "test.txt";
	    public static final File FILE = new File(FILENAME);
	    public static final Path path = Paths.get(FILENAME);

	    public static void main(String[] args) {
	        // Buffered reader with StrngBuilder.
	        try (BufferedReader br = new BufferedReader(new FileReader(FILENAME))) {
	            StringBuilder sb = new StringBuilder();
	            String line = br.readLine();

        	    while (line != null) {
        	        sb.append(line);
        	        sb.append(System.lineSeparator());
        	        line = br.readLine();
        	    }
        	    String everything = sb.toString();
        	    System.out.println(everything);
        	} catch (IOException e) {
            	e.printStackTrace();
        	}

  	      //  Try with reources
        	try (InputStream inputStream = new FileInputStream(FILE)) {
        	    String fileContents = "";
        	    int intValueOfLetter;
        	    char letter;
        	    while ((intValueOfLetter = inputStream.read()) != -1) {
        	        letter = (char) intValueOfLetter;
        	        fileContents += letter;
        	    }
        	    System.out.println(fileContents);
        	} catch (IOException e) {
        	    e.printStackTrace();
        	}

        	// Files.readAllLines
        	try {
        	    Path path = Paths.get(FILENAME);
        	    List<String> lines = Files.readAllLines(path);
        	    for (String line : lines) {
        	        System.out.println(line);
        	    }
        	} catch (IOException e) {
        	    e.printStackTrace();
        	}

        	// BufferedReader with normal string.
        	try (BufferedReader reader = Files.newBufferedReader(path)) {
        	    String finalString = "";
        	    String line;
        	    while ((line = reader.readLine()) != null) {
        	        finalString += line + "\n";
        	    }
        	    System.out.println(finalString);
        	} catch (IOException e) {
        	    e.printStackTrace();
        	}

        	// Scanner
        	try (Scanner scanner = new Scanner(path)) {
        	    String finalString = "";
        	    while (scanner.hasNextLine()) {
        	        finalString += scanner.nextLine() + "\n";
        	        System.out.println(finalString);
        	    }
        	} catch (IOException e) {
        	    e.printStackTrace();
        	}

        	// Lambda
        	try (Stream<String> stream = Files.lines(path)) {
        	    stream.forEach(System.out::println);
        	} catch (IOException e) {
        	    e.printStackTrace();
        	}
    	}
	}


Siin on koodi näide kuidas readerit manuaalselt kinni panna.



.. code-block:: java
	
	try {
	    BufferedReader reader = Files.newBufferedReader(path);
	    try {
	        String finalStringForBufferedReader = "";
	        String line;
	        while ((line = reader.readLine()) != null) {
	            finalStringForBufferedReader += line + "\n";
	        }
	        System.out.println(finalStringForBufferedReader);
	    } finally {
	        reader.close();
	    }
	} catch (IOException e) {
	    e.printStackTrace();
	}
