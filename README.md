 ## Tic Tac Toe

This is a simple command-line Tic Tac Toe game written in Python. The game is played on a 3x3 grid, with each player taking turns to place their mark (either 'X' or 'O') in one of the empty squares. The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins the game.

### How to play

To play the game, simply run the `tic_tac_toe.py` file. You will be prompted to enter the row and column of the square you want to place your mark in. The game will then check if you have won, and if not, it will switch to the next player's turn.

### Code explanation

The code for the game is relatively simple. The main function is `tic_tac_toe()`, which initializes the game board and then loops until a player wins or the game is drawn. The `print_board()` function prints the current state of the board to the console, and the `check_win()` function checks if the current player has won.

The game board is represented as a list of lists, where each inner list represents a row on the board. The squares on the board are numbered from 1 to 9, starting from the top left corner and going from left to right.

The `check_win()` function checks if the current player has won by checking if they have three of their marks in a row, either horizontally, vertically, or diagonally. The function returns `True` if the player has won, and `False` otherwise.

The game loop continues until a player wins or the game is drawn. If a player wins, the `print_board()` function is called to print the final state of the board, and then the `print()` function is called to print a message announcing the winner. If the game is drawn, the `print_board()` function is called to print the final state of the board, and then the `print()` function is called to print a message announcing the draw.

### Conclusion

This is a simple but fun Tic Tac Toe game written in Python. The game is easy to play and understand, and it can be a great way to learn the basics of programming.
