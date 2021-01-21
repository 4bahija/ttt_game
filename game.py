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
        
