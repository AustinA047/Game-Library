#!usr/bin/python3
#Austin Andrews
#01/27/2020

import pickle
games = {}
def add_game():
    print("\nAdd game is running")
    
def print_games():
    key_list = games.keys()
        
    for key in key_list:
        print()
        print("Genre: ", games[key][0])
        print("Title: ", games[key][1])
        print("Developer: ", games[key][2])
        print("Publisher: ", games[key][3])
        print("System: ", games[key][4])
        print("Release Date: ", games[key][5])
        print("Rating: ", games[key][6])
        print("Single/Multi/Both: ", games[key][7])
        print("Beat the game?: ", games[key][8])    
        print("Pruchase Date: ", games[key][9])
        print("Extra Notes: ", games[key][10])
        print("----------------------")  
    
def search_games():
    found_one = False
    name = input("  What is the title of the game? ")
    for key in games.keys():
        if name == games[key][1]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("System: ", games[key][4])
            print("Release Date: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Single/Multi/Both: ", games[key][7])
            print("Beat the game?: ", games[key][8])    
            print("Pruchase Date: ", games[key][9])
            print("Extra Notes: ", games[key][10])
            print("----------------------")              
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")    
    
def remove_game():
    print("\nRemove game is running")
    
def save_data():
    datafile = open("game_lib.pickle", "wb")
    pickle.dump(games, datafile)
    datafile.close()
    print("File Saved")
    
def quit():
    print("\nQuit is running")
    
keep_going = True

datafile = open("game_lib.pickle", "rb")
games = pickle.load(datafile)
datafile.close()

while keep_going:
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