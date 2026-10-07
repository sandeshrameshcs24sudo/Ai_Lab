# Tic-Tac-Toe using Functions

def display_board(board):
    print("\n")
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])


def check_winner(board, player):
    # Check rows
    if (board[0] == board[1] == board[2] == player or
        board[3] == board[4] == board[5] == player or
        board[6] == board[7] == board[8] == player):
        return True

    # Check columns
    if (board[0] == board[3] == board[6] == player or
        board[1] == board[4] == board[7] == player or
        board[2] == board[5] == board[8] == player):
        return True

    # Check diagonals
    if (board[0] == board[4] == board[8] == player or
        board[2] == board[4] == board[6] == player):
        return True

    return False


def check_draw(board):
    return " " not in board


def play_game():
    board = [" "] * 9
    player = "X"

    while True:
        display_board(board)

        position = int(input("Player " + player + ", enter position (1-9): "))

        if position < 1 or position > 9:
            print("Enter a number between 1 and 9.")
            continue

        if board[position - 1] != " ":
            print("Position already occupied!")
            continue

        board[position - 1] = player

        if check_winner(board, player):
            display_board(board)
            print("Player", player, "wins!")
            break

        if check_draw(board):
            display_board(board)
            print("Game is a draw!")
            break

        if player == "X":
            player = "O"
        else:
            player = "X"


# Start the game
play_game()
