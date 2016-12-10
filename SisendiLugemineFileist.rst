========================
Sisendi lugemine failist
========================
Javas võib sisend-väljud näha keeruline, kuid see pole halb. Sellega saavutatakse seda, et nii klaviatuurilt kui ka failist saab andmeid lugeda kõrgema kihi objektidega nagu BufferedReader või Scanner. Lisaks sellele on veel täiendav võimalus Files.readAllLines()

.. code-block:: java
	
	import java.io.BufferedReader;
	import java.io.IOException;
	import java.nio.file.Files;
	import java.nio.file.Path;
	import java.nio.file.Paths;
	import java.util.ArrayList;
	import java.util.List;
	import java.util.Scanner;
	 
	public class ReadFile {
	 
	/**
	 * Filename to be read. 
	 */
	public static final String FILENAME = "test.txt";
 
		public static void main(String[] args) {
			// Files.readAllLines
			try {
				for (String line : readSmallFile(FILENAME)) {
					System.out.println(line);
				}
			} catch (IOException e) {
				e.printStackTrace();
			}
			// BufferedReader
			try {
				System.out.println(readFileBuffered(FILENAME));
			} catch (IOException e) {
				e.printStackTrace();
			}
 	
			// Scanner
			try {
				System.out.println(readFileScanner(FILENAME));
			} catch (IOException e) {
				e.printStackTrace();
			}
 	
		/**
		 * Reads (a small) file and returns list of lines (strings).
		 * @param filename Filename to be read.
		 * @return List of lines.
		 * @throws IOException
		 */
		public static List<String> readSmallFile(String filename) throws IOException {
			Path path = Paths.get(filename);
			List<String> lines = Files.readAllLines(path);
			return lines;
		}
 	
		/**
		 * Reads file using Scanner.
		 * @param filename filename to be read.
		 * @return The contents of the file as one string.
		 * @throws IOException
		 */
		public static String readFileScanner(String filename) throws IOException {
			String finalString = "";
			Path path = Paths.get(filename);
			Scanner scanner = new Scanner(path);
			while (scanner.hasNextLine()) {
				// "\n" -> newline
				finalString += scanner.nextLine() + "\n";
			}
			scanner.close();
			return finalString;
		}
		/**
		 * Read file using BufferedReader.
		 * @param filename Filename to be read.
		 * @return The contents of the file as one string.
		 * @throws IOException
		 */
		public static String readFileBuffered(String filename) throws IOException {
			String finalString = "";
			Path path = Paths.get(filename);
			BufferedReader reader = Files.newBufferedReader(path);
			String line;
			while ((line = reader.readLine()) != null) {
				finalString += line + "\n";
			}
			reader.close();
			return finalString;
		}	
	}