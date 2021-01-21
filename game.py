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
