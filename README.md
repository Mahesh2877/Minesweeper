# Minesweeper
Here, we attempt to create a Minesweeper board where the locations of the Bombs are provided to us.

The objective here is:
    Provided the size of the Minesweeper Board and the locations of the Bombs -> Create the Minesweeper board with each cell storing the correct number(i.e., the number of bombs in its immediate neighbouring cells)
    
To solve this we can:
    Iterate through the bomb cells only(this is possible as their location is already given to us) -> For each cell, increment the value of all it's neighbouring cells by one if they are still inside the boundary of the board and are not bombs themselves.
