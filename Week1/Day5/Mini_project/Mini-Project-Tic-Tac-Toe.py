# TicTacToe — Two players (row/column input)

def init_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def display_board(board):
    print("\nTIC TAC TOE")
    print("*" * 17)
    for row in board:
        print(f"*  {row[0]} | {row[1]} | {row[2]}  *")
        print("*  ---|---|---  *")
    print("*" * 17 + "\n")

def player_input(board, player):
    while True:
        try:
            row = int(input("Enter row (1-3):    ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if row not in range(3) or col not in range(3):
                print("Please enter values between 1 and 3.")
            elif board[row][col] != " ":
                print("That position is already taken.")
            else:
                return row, col
        except ValueError:
            print("Invalid input. Enter a number.")

def check_win(board, player):
    # Lignes et colonnes
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    # Diagonales
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(board[r][c] != " " for r in range(3) for c in range(3))

def switch_player(player):
    return "O" if player == "X" else "X"

def play():
    print("Welcome to TIC TAC TOE!\n")

    while True:
        board  = init_board()
        player = "X"

        while True:
            display_board(board)
            print(f"Player {player}'s turn...\n")

            row, col      = player_input(board, player)
            board[row][col] = player

            if check_win(board, player):
                display_board(board)
                print(f"Player {player} wins!\n")
                break

            if check_draw(board):
                display_board(board)
                print("It's a draw!\n")
                break

            player = switch_player(player)

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing! \n")
            break

play()