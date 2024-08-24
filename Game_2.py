# Tic Tac Toe Game

def print_board(board):
    """Prints the Tic Tac Toe board."""
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_win(board, player):
    """Checks if the current player has won."""
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    """Checks if the game is a draw."""
    return all(spot != ' ' for spot in board)

def tic_tac_toe():
    """Main function to run the Tic Tac Toe game."""
    board = [' '] * 9
    current_player = 'X'
    
    while True:
        print_board(board)
        
        # Get the player's move
        move = input(f"Player {current_player}, enter your move (1-9): ")
        
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        
        move = int(move) - 1
        
        if board[move] != ' ':
            print("This spot is already taken. Choose another one.")
            continue
        
        board[move] = current_player
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
