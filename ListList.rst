=======================
Kahemõõtmelised kogumid
=======================

Peale primitiivsete andmetüüpide ja objektide võib Javas järjend või massiiv koosneda ka teistest järjenditest või massiividest.
Neid saab kogumisse lisada, sealt lugeda ja muidu neid kasutada täpselt samamoodi kui teisi andmeid.

**NB!** Järjendisse saab lisada massiive (nt *ArrayList<int[]>*), aga massivi ei saa lisada järjendeid.

Kahemõõtmeline massiiv
----------------------

Mitmemõõtmelist massiivi initsialiseerides peab määrama kõikide massiivide suurused.

.. code-block:: java

    int[][] matrix = new int[2][4];

    int[] row1 = {1, 2, 6, 10};
    int[] row2 = new int[4];
    
    row2[0] = 2;
    row2[1] = 11;
    row2[2] = 5;
    row2[3] = 100;

    // add rows to matrix
    matrix[0] = row1;
    matrix[1] = row2;

    for (int i = 0; i < matrix.length; i++) {
        System.out.println("Row " + i);
        
        for (int j = 0; j < matrix[0].length; j++) {
            System.out.println(matrix[i][j]);
        }
        System.out.println();
    }
    
    // change element value in array
    matrix[1][2] = 42;
    System.out.println("\n" + matrix[1][2]);

Antud kood trükib konsooli:

.. code-block:: console

    Row 0
    1
    2
    6
    10

    Row 1
    2
    11
    5
    100
    
    42


Kahemõõtmeline järjend
----------------------

.. code-block:: java

    ArrayList<ArrayList<String>> listOfLists = new ArrayList<ArrayList<String>>();

    ArrayList<String> firstList = new ArrayList<String>();
    firstList.add("this");
    firstList.add("is");
    firstList.add("a");
    firstList.add("list");

    ArrayList<String> secondList = new ArrayList<String>();
    secondList.add("this");
    secondList.add("is");
    secondList.add("another");
    secondList.add("list");

    // add two lists to ListOfLists
    listOfLists.add(firstList);
    listOfLists.add(secondList);

    for (ArrayList<String> list : listOfLists) {
        for (String word : list) {
            System.out.println(word);
        }
        System.out.println();
    }
    
    // change element with index 1 in secondList
    secondList.set(1, "was");
    
    // replace listOfLists element with index 1 with secondList 
    listOfLists.set(1, secondList);
    
    System.out.println();
    for (String word : listOfLists.get(1)) {
        System.out.println(word);
    }

See kood prindib konsooli:

.. code-block:: console

    this
    is
    a
    list

    this
    is
    another
    list
    
    this
    was
    another
    list
