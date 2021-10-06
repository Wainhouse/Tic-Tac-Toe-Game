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

# Game board

# script the board
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_", ]

# display the board


def display_board():
    print(board[0] + " | " + board[1] + " |" + board[2])
    print(board[3] + " | " + board[4] + " |" + board[5])
    print(board[6] + " | " + board[7] + " |" + board[8])


# rule of the game disp[lay the board
def play_game():

    display_board()

    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

# A function to handle the turn


def handle_turn():
    position = input("Choose a position for 1-9: ")
    position = int(position) - 1

    board[position] = "X"
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win()


# check rows
# check columns
# check diagonals
return


def check_if_tie()


return


def flip_player()


return


play_game()
