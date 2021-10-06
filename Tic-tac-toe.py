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

    print(player + "'s turn.")
    position = input("Choose a position for 1-9: ")

    valid = False
    while not valid:

        # while loop for invalid input
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position for 1-9: ")

        position = int(position) - 1

        # if loop to stop overriding position
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again!")

    board[position] = player

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

    # get the winner
    if row_winner:
        # There was a win
        winner = row_winner
    elif column_winner:
        # There was a win
        winner = column_winner
    elif diag_winner:
        # There was a win
        winner = diag_winner
    else:
        # There was no win
        winner = None
    return


def check_rows():
    # set up globals again
    global game_still_going
    # check if any of the rows have won
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if a win, flag a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner (X or o)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_colums():
    global game_still_going
    # check if any of the col have won
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # if a win, flag a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner (X or o)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diag():
    global game_still_going
    # check if any of the diag have won
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[6] == board[4] == board[2] != "-"
    # if a win, flag a win
    if diag_1 or diag_2:
        game_still_going = False
    # Return the winner (X or o)
    if diag_1:
        return board[0]
    elif diag_2:
        return board[6]
    return


def check_for_tie():
    # insert global
    global game_still_going
    if "-" not in board:
        game_still_going = False

    return


def flip_player():
    # need global var
    global current_player
    # if current player was X, then change it to O
    if current_player == "X":
        current_player = "O"
    # If current player is O, then change it to X
    elif current_player == "O":
        current_player = "X"
    return


play_game()
