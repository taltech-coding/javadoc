

Tsüklid
================

+------------------------------------------------------+-----------------------------------------------------------+
| Python                                               | Java                                                      |
+======================================================+===========================================================+
|                                                      |                                                           |
| .. code-block:: python                               | .. code-block:: java                                      |
|                                                      |                                                           |
|     for i in range(10):                              |     for (int i = 0; i < 10; i++) {                        |
|         print(i)                                     |         System.out.println(i);                            |
|                                                      |     }                                                     |
|                                                      |                                                           |
|                                                      | Või kasutades *stream*'i:                                 |
|                                                      |                                                           |
|                                                      | .. code-block:: java                                      |
|                                                      |                                                           |
|                                                      |     IntStream.range(0, 10).forEach(System.out::println);  |
|                                                      |                                                           |
|                                                      |                                                           |
+------------------------------------------------------+-----------------------------------------------------------+
|                                                      |                                                           |
| .. code-block:: python                               | .. code-block:: java                                      |
|                                                      |                                                           |
|     i = 0                                            |     int i = 0;                                            |
|     while i < 10:                                    |     while (i < 10) {                                      |
|         print(i)                                     |         System.out.println(i++);                          |
|         i += 1                                       |         // i++ -> prints out the current value            |
|                                                      |         // of i, then increments it by 1                  |
|                                                      |     }                                                     |
|                                                      |                                                           |
+------------------------------------------------------+-----------------------------------------------------------+
|                                                      |                                                           |
| .. code-block:: python                               | .. code-block:: java                                      |
|                                                      |                                                           |
|     lst = [1, 2, 3]                                  |     List<Integer> list = new ArrayList<>();               |
|     for x in lst:                                    |     list.add(1); list.add(2); list.add(3);                |
|         print(x)                                     |     //List<Integer> list = new ArrayList<>(               |
|                                                      |     //    Arrays.asList(1, 2, 3));                        |
|                                                      |     for (Integer x : list) {                              |
|                                                      |         System.out.println(x);                            |
|                                                      |     }                                                     |
|                                                      |                                                           |
|                                                      | Või kasutades *stream*'i:                                 |
|                                                      |                                                           |
|                                                      | .. code-block:: java                                      |
|                                                      |                                                           |
|                                                      |     List<Integer> list = new ArrayList<>(                 |
|                                                      |             Arrays.asList(1, 2, 3)                        |
|                                                      |     );                                                    |
|                                                      |     list.stream().forEach(System.out::println);           |
|                                                      |                                                           |
+------------------------------------------------------+-----------------------------------------------------------+
|                                                      |                                                           |
| .. code-block:: python                               | .. code-block:: java                                      |
|                                                      |                                                           |
|     for x in range(10, 0, -2):                       |     for (int i = 10; i > 0; i -= 2) {                     |
|         print(x)                                     |         System.out.println(i);                            |
|                                                      |     }                                                     |
|                                                      |                                                           |
|                                                      | Või kasutades *stream*'i:                                 |
|                                                      |                                                           |
|                                                      | .. code-block:: java                                      |
|                                                      |                                                           |
|                                                      |     IntStream.iterate(10, n-> n -= 2)                     |
|                                                      |             .takeWhile(n -> n > 0)                        |
|                                                      |             .forEach(System.out::println);                |
|                                                      |                                                           |
+------------------------------------------------------+-----------------------------------------------------------+
|                                                      |                                                           |
| .. code-block:: python                               | .. code-block:: java                                      |
|                                                      |                                                           |
|     j = 1                                            |     for (int i = 0, j = 1; i <= 10; j *= 2, i += 1) {     |
|     for i in range(11):                              |         System.out.println(j);                            |
|         print(j)                                     |     }                                                     |
|         j*=2                                         |                                                           |
|                                                      |                                                           |
+------------------------------------------------------+-----------------------------------------------------------+
|                                                      |                                                           |
| .. code-block:: python                               | .. code-block:: java                                      |
|                                                      |                                                           |
|     day = "Monday"                                   |     String day = "Monday";                                |
|     for letter in day:                               |     for (int i = 0; i < day.length(); i++) {              |
|         print(letter)                                |         System.out.println(day.charAt(i));                |
|                                                      |     }                                                     |
|                                                      |                                                           |
|                                                      | Või kasutades *stream*'i:                                 |
|                                                      |                                                           |
|                                                      | .. code-block:: java                                      |
|                                                      |                                                           |
|                                                      |     String day = "Monday";                                |
|                                                      |     day.chars()                                           |
|                                                      |             .mapToObj(c -> (char)c)                       |
|                                                      |             .forEach(System.out::println);                |
|                                                      |                                                           |
+------------------------------------------------------+-----------------------------------------------------------+
| Paarisarvude summa                                                                                               |
+------------------------------------------------------+-----------------------------------------------------------+
|                                                      |                                                           |
| .. code-block:: python                               | .. code-block:: java                                      |
|                                                      |                                                           |
|     even_sum = 0                                     |     int evenSum = 0;                                      |
|     for x in range(10):                              |     for (int i = 0; i < 10; i++) {                        |
|         if x % 2 == 0: even_sum += x                 |         if (i % 2 == 0) evenSum += i;                     |
|                                                      |     }                                                     |
|     print(even_sum)                                  |     System.out.println(evenSum);                          |
|                                                      |                                                           |
| Või kasutades list comprehensionit:                  | Või kasutades *stream*'i/lambdat:                         |
|                                                      |                                                           |
| .. code-block:: python                               | .. code-block:: java                                      |
|                                                      |                                                           |
|     print(sum([x for x in range(10) if x % 2 == 0])) |     System.out.println(                                   |
|                                                      |             IntStream.range(0, 10)                        |
|                                                      |             .filter(x -> x % 2 == 0)                      |
|                                                      |             .sum()                                        |
|                                                      |     );                                                    |
|                                                      |                                                           |
+------------------------------------------------------+-----------------------------------------------------------+
| Sorteerimine ilma duplikaatideta                                                                                 |
+------------------------------------------------------+-----------------------------------------------------------+
|                                                      |                                                           |
| .. code-block:: python                               | .. code-block:: java                                      |
|                                                      |                                                           |
|     numbers = [3, 3, 1, 4, 7, 7, 7]                  |     List<Integer> numbers =                               |
|     result = []                                      |             Arrays.asList(3, 3, 1, 4, 7, 7, 7);           |
|     for n in numbers:                                |     List<Integer> result = new ArrayList<>();             |
|         if n not in result:                          |     for (Integer n: numbers) {                            |
|             result.append(n)                         |         if (!result.contains(n)) {                        |
|                                                      |             result.add(n);                                |
|     for nr in sorted(result):                        |         }                                                 |
|         print(nr)                                    |     }                                                     |
|                                                      |     Collections.sort(result);                             |
| Või kasutades seti:                                  |     result.forEach(System.out::println);                  |
|                                                      |                                                           |
| .. code-block:: python                               | Või kasutades *stream*'i/lambdat:                         |
|                                                      |                                                           |
|     numbers = [3, 3, 1, 4, 7, 7, 7]                  | .. code-block:: java                                      |
|     print(*sorted(set(numbers)), sep='\n')           |                                                           |
|                                                      |     List<Integer> numbers = List.of(3, 3, 1, 4, 7, 7, 7); |
|                                                      |     numbers.stream()                                      |
|                                                      |         .distinct()                                       |
|                                                      |         .sorted()                                         |
|                                                      |         .forEach(System.out::println);                    |
|                                                      |                                                           |
+------------------------------------------------------+-----------------------------------------------------------+


Loe tsüklite kohta siit: :doc:`../control_flow/loop`.


.. generated using "python3 rst_table.py loop-helper.txt loop.rst"
