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

