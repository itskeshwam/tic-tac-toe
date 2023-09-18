def print_board(board):
    """Print the Tic Tac Toe board with vertical dashes"""
    for i in range(5):
        if i % 2 == 0:
            print(' | '.join(board[i // 2]))
        else:
            print('-' * 9)

def check_win(board, player):
    """Check if the player has won"""
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Player {current_player}, enter row (1, 2, or 3):")
        row = int(input()) - 1  # Adjust for 0-based indexing
        print(f"Player {current_player}, enter column (1, 2, or 3):")
        col = int(input()) - 1  # Adjust for 0-based indexing

        if not (0 <= row < 3) or not (0 <= col < 3) or board[row][col] != ' ':
            print("Invalid input. Try again.")
            continue

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a draw
        if all(cell != ' ' for row in board for cell in row):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player for the next turn
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()