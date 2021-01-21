import os
import time
import random

def welcome():
    for i in range(0, 11):
        print("*", end="")
    print()
    print("* WELCOME *", end="")
    print()
    for i in range(0, 11):
        print("*", end="")
    print()
    input("Press ENTER key to start")
    option()

def option():
    for i in range(0, 21):
        print("*", end="")
    print()
    print("1.Tic Tac Toe")
    for i in range(0, 21):
        print("*", end="")
    print()
    chc = int(input("Enter your choice number: "))
    if chc == 1:
        tictactoemenu()
    else:
        welcome()

def tictactoemenu():
    print("Welcome To Tic Tac Toe")
    for i in range(0, 21):
        print("*", end="")
    print()
    print("1. Two Player\n2. One Player")
    for i in range(0, 21):
        print("*", end="")
    print()
    chc = int(input("Enter the number of your choice: "))
    if chc == 1:
        two_player()
    elif chc == 2:
        single_player()
    else:
        option()

def two_player():
    board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def rules():
        print("Welcome to TIC TAC TOE")
        print("This is a two player game where USER 1 is X and USER 2 is O")
        print("Enter your choice from 1 to 9")
        print("""
                1 | 2 | 3
                ---|---|---
                4 | 5 | 6
                ---|---|---
                7 | 8 | 9
                """)
    def print_board():
        print("   |   |   ")
        print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
        print("   |   |   ")

    def is_winner(board, player):
        if (board[1] == player and board[2] == player and board[3] == player) or \
            (board[4] == player and board[5] == player and board[6] == player) or \
            (board[7] == player and board[8] == player and board[9] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[3] == player and board[6] == player and board[9] == player) or \
            (board[1] == player and board[5] == player and board[9] == player) or \
                (board[3] == player and board[5] == player and board[7] == player):
            return True
        else:
            return False

    def is_board_full(board):
        if " " in board:
            return False
        else:
            return True

    while True:
        os.system("clear")
        rules()
        print_board()

        # user 1
        choice = input("Please choose an empty space for X: ")
        choice = int(choice)
        if board[choice] == " ":
            board[choice] = "X"
        else:
            print("Spot already taken")
            time.sleep(1)
        # for user 1 to win
        if is_winner(board, "X"):
            os.system("clear")
            rules()
            print_board()
            print("USER1 Win")
            break

        os.system("clear")
        rules()
        print_board()

        # check if board is full i.e. a tie
        if is_board_full(board):
            print("Tie")
            break

        choice = input("Please choose an empty space for O: ")
        choice = int(choice)
        if board[choice] == " ":
            board[choice] = "O"
        else:
            print("Spot already taken")
            time.sleep(1)
        # for user 2 to win
        if is_winner(board, "O"):
            os.system("clear")
            rules()
            print_board()
            print("USER2 Win")
            break

        # check if board is full i.e. a tie
        if is_board_full(board):
            print("Tie")
            break

def single_player():
    board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def rules():
        print("Welcome to TIC TAC TOE")
        print("This is a single player game where You are X and Computer is O")
        print("Enter your choice from 1 to 9")
        print("""
                1 | 2 | 3
                ---|---|---
                4 | 5 | 6
                ---|---|---
                7 | 8 | 9
                """)

    def print_board():
        print("   |   |   ")
        print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
        print("   |   |   ")

    def is_winner(board, player):
        if (board[1] == player and board[2] == player and board[3] == player) or \
            (board[4] == player and board[5] == player and board[6] == player) or \
            (board[7] == player and board[8] == player and board[9] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[3] == player and board[6] == player and board[9] == player) or \
            (board[1] == player and board[5] == player and board[9] == player) or \
                (board[3] == player and board[5] == player and board[7] == player):
            return True
        else:
            return False

    def is_board_full(board):
        if " " in board:
            return False
        else:
            return True

    def get_computer_move(board, player):

        # check for a win
        for i in range(1, 10):
            if board[i] == " ":
                board[i] = player
                if is_winner(board, player):
                    return i
                else:
                    board[i] = " "

        # check for column block
        for i in [1, 2, 3]:
            if board[i] == "X" and board[i+3] == "X" and board[i+6] == " ":
                return i+6
            if board[i+3] == "X" and board[i+6] == "X" and board[i] == " ":
                return i
            if board[i] == "X" and board[i+6] == "X" and board[i+3] == " ":
                return i+3

        # check for rows blocks
        for i in [1, 4, 7]:
            if board[i] == "X" and board[i+1] == "X" and board[i+2] == " ":
                return i+2
            if board[i+1] == "X" and board[i+2] == "X" and board[i] == " ":
                return i
            if board[i] == "X" and board[i+2] == "X" and board[i+1] == " ":
                return i+1

        # check diagonal block
        if board[1] == "X" and board[5] == "X" and board[9] == " ":
            return 9
        if board[9] == "X" and board[5] == "X" and board[1] == " ":
            return 1
        if board[1] == "X" and board[9] == "X" and board[5] == " ":
            return 5
        if board[3] == "X" and board[5] == "X" and board[7] == " ":
            return 7
        if board[7] == "X" and board[5] == "X" and board[3] == " ":
            return 3
        if board[3] == "X" and board[7] == "X" and board[5] == " ":
            return 5

        if board[5] == " ":
            return 5
        while True:
            move = random.randint(1, 9)
            if board[move] == " ":
                return move
                break
            return 5

    while True:
        os.system("clear")
        rules()
        print_board()

        # user 1
        choice = input("Please choose an empty space for X: ")
        choice = int(choice)
        if board[choice] == " ":
            board[choice] = "X"
        else:
            print("Spot already taken")
            time.sleep(1)
        # for user 1 to win
        if is_winner(board, "X"):
            os.system("clear")
            rules()
            print_board()
            print("Congratulations!! You Win")
            break

        os.system("clear")
        rules()
        print_board()

        # check if board is full i.e. a tie
        if is_board_full(board):
            print("Tie")
            break

        # user 2
        choice = get_computer_move(board, "O")
        if board[choice] == " ":
            board[choice] = "O"
        else:
            print("Spot already taken")
            time.sleep(1)
        # for user 2 to win
        if is_winner(board, "O"):
            os.system("clear")
            rules()
            print_board()
            print("Sorry!! COMPUTER Wins")
            break

        # check if board is full i.e. a tie
        if is_board_full(board):
            print("Tie")
            break


def print_scoreboard(score_board):
    print("--------------------------------")
    print("            SCOREBOARD       ")
    print("--------------------------------")

    players = list(score_board.keys())
    print("   ", players[0], "    ", score_board[players[0]])
    print("   ", players[1], "    ", score_board[players[1]])

    print("--------------------------------\n")


welcome()
print("\n")
option()
