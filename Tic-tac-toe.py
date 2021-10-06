# Fist make a plan

# board
# display board
# play game
# check win
# check row
# check columns
# check diagonals
# check tie
# flip player

# ---- Global Variables ----


# script the board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

# display the board
game_still_going = True

# Who won? Or Tie?
winner = None

# w Whose turn is it?
current_player = "X"

# Game board


def display_board():
    print(board[0] + " | " + board[1] + " |" + board[2])
    print(board[3] + " | " + board[4] + " |" + board[5])
    print(board[6] + " | " + board[7] + " |" + board[8])


# rule of the game disp[lay the board
def play_game():

    display_board()

    while game_still_going:

        # handle the turn of a player
        handle_turn(current_player)

        # check if the game is over
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Ti.e")

# A function to handle the turn

# handle the turn of a player


def handle_turn(player):
    position = input("Choose a position for 1-9: ")
    position = int(position) - 1

    board[position] = "X"

    display_board()


def check_if_game_over():
    check_for_win()
    check_for_tie()


def check_for_win():

    # set up the globals
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_colums()
    # check diagonals
    diag_winner = check_diag()
    if row_winner:
        # There was a win
        winner = row_winner()
    elif column_winner:
        # There was a win
        winner = column_winner()
    elif diag_winner:
        # There was a win
        winner = diag_winner()
    else:
        # There was no win
        winner = None
    return


def check_rows():
    # set up globals again
    global game_still_going
    # check if any of the rows have won
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[4] == board[5] == board[6] != "-"
    row_3 = board[7] == board[8] == board[9] != "-"
    return


def check_colums():

    return


def check_diag():
    return


def check_for_tie():

    return


def flip_player():

    return


play_game()
