#!usr/bin/python3
#Austin Andrews
#01/27/2020

import pickle

def add_game():
    print("\nAdd game is running")
def print_games():
    print("\nPrint games is running")
def search_games():
    print("\nSearch games is running")
def remove_game():
    print("\nRemove game is running")
def save_data():
    print("\nSave data is running")
def quit():
    print("\nQuit is running")
keep_going = True

if keep_going:
    print("""
    
    MAIN MENU
    1) Add New Game
    2) Print All Games
    3) Search Game By Title
    4) Remove A Game
    5) Save Database
    
    Q) Quit
    
    """)
    
    choice = input("What would you like to select?")
    if choice == "1":
        add_game()
    elif choice == "2":
        print_games()
    elif choice == "3":
        search_games()
    elif choice == "4":
        remove_game()
    elif choice == "5":
        save_data()
    elif choice == "Q" or choice == "q":
        quit()
        keep_going = False
        
print("\nGoodbye.")    