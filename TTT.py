# glendon
# tic tac toe game
# with 3 levels
# level 1 is the normal game.
# level 3 is a bit ridiculous.
# have fun....


def print_board(board):
    """Prints the game board."""
    for row in board:
        print(" | ".join(row))
        print("-" * (len(row) * 4 - 1))

def check_winner(board, player, win_condition):
    """
    Checks if the player has won based on the win condition.
    """
    rows = len(board)
    cols = len(board[0])
    
    # Check rows
    for row in board:
        for i in range(cols - win_condition + 1):
            if all(cell == player for cell in row[i:i + win_condition]):
                return True
    
    # Check columns
    for col in range(cols):
        for i in range(rows - win_condition + 1):
            if all(board[i + j][col] == player for j in range(win_condition)):
                return True
    
    # Check diagonals (top-left to bottom-right)
    for i in range(rows - win_condition + 1):
        for j in range(cols - win_condition + 1):
            if all(board[i + k][j + k] == player for k in range(win_condition)):
                return True
    
    # Check diagonals (bottom-left to top-right)
    for i in range(win_condition - 1, rows):
        for j in range(cols - win_condition + 1):
            if all(board[i - k][j + k] == player for k in range(win_condition)):
                return True
    
    return False

def is_board_full(board):
    """Checks if the board is full."""
    return all(cell != " " for row in board for cell in row)

def play_game(rows, cols, win_condition):
    """
    Plays the Tic Tac Toe game with the specified grid size and win condition.
    """
    board = [[" " for _ in range(cols)] for _ in range(rows)]
    players = ["X", "O"]
    turn = 0
    
    print(f"\nWelcome to Level {1 if (rows, cols, win_condition) == (3, 3, 3) else 2 if (rows, cols, win_condition) == (5, 5, 4) else 3}!")
    print(f"Grid Size: {rows}x{cols}, Win Condition: {win_condition} in a row.")
    
    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn.")
        
        # Get player's move
        while True:
            try:
                row = int(input(f"Enter row (0-{rows - 1}): "))
                col = int(input(f"Enter column (0-{cols - 1}): "))
                if 0 <= row < rows and 0 <= col < cols and board[row][col] == " ":
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter numbers.")
        
        # Update the board
        board[row][col] = player
        
        # Check for a winner
        if check_winner(board, player, win_condition):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        # Check for a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        turn += 1

def main():
    """Main function to select the level and start the game."""
    print("Welcome to Enhanced Tic Tac Toe!")
    print("Select a level:")
    print("1. Level 1: 3x3 grid, 3 in a row to win")
    print("2. Level 2: 5x5 grid, 4 in a row to win")
    print("3. Level 3: 8x8 grid, 6 in a row to win")
    
    while True:
        choice = input("Enter the level number (1-3): ").strip()
        if choice in ["1", "2", "3"]:
            break
        else:
            print("Invalid choice. Please try again.")
    
    if choice == "1":
        play_game(3, 3, 3)
    elif choice == "2":
        play_game(5, 5, 4)
    elif choice == "3":
        play_game(8, 8, 6)

if __name__ == "__main__":
    main()