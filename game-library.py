#!usr/bin/python3
#Austin Andrews
#01/27/2020

import pickle
games = {}
def add_game():
    new_key = len(games) + 1
    new_entry = []
    valid = False
    while not valid:
        #input stuff
        genre = input("What is the Genre?  ")
        new_entry.append(genre)
        
        title = input("What is the Title?  ")
        new_entry.append(title)
        
        developer = input("What is the Developer?  ")
        new_entry.append(developer)
        
        publisher = input("What is the Publisher?  ")
        new_entry.append(publisher)
        
        platform = input("What is the Platform?  ")
        new_entry.append(platform)
        
        release = input("What is the Release Date?  ")
        new_entry.append(release)
        
        rating = input("What is your Rating?  ")
        new_entry.append(rating)
        
        single_multi_both = input("Is your game single multiplayer or both?  ")
        new_entry.append(single_multi_both)
        
        beat = input("Have you beat the game?  ")
        new_entry.append(beat)
        
        purchase_date = input("What is the Purchase Date  ")
        new_entry.append(purchase_date)
        
        price = input("What is the price  ")
        new_entry.append(price)
        

        notes = input("Any extra Notes?  ")
        new_entry.append(notes)

        
        answer = input("Is this correct?  ")
        if answer.lower() in ("yes", "y"):
            valid = True   
            games[new_key] = new_entry
    
def edit_game():
    print("Here is the Library: ")
    for key in games.keys():
        print(key, "-", games[key][1])
    edit_key = int(input("Which game do you want to change?  "))
    edit_entry = games[edit_key]
    valid = False
    while not valid:
        #input stuff
        print("Current Genre: ", edit_entry[0])
        genre = input("What is the New Genre?  ")
        edit_entry[0] = genre
        
        print("Current Title: ", edit_entry[1])
        title = input("What is the New Title?  ")
        edit_entry[1] = title
        
        print("Current Developer: ", edit_entry[2])
        developer = input("What is the New Developer?  ")
        edit_entry[2] = developer
        
        print("Current Publisher: ", edit_entry[3])
        publisher = input("What is the New Publisher?  ")
        edit_entry[3] = publisher
        
        print("Current Platform: ", edit_entry[4])
        platform = input("What is the New Platform?  ")
        edit_entry[4] = platform
        
        print("Current Release Date: ", edit_entry[5])
        release = input("What is the New Release Date?  ")
        edit_entry[5] = release
        
        print("Current Rating: ", edit_entry[6])
        rating = input("What is your New Rating  ")
        edit_entry[6] = rating
        
        print("Current Mode: ", edit_entry[7])
        single_multi_both = input("Is your game single multiplayer or both?  ")
        edit_entry[7] = single_multi_both
        
        print("Current Completion: ", edit_entry[8])
        beat = input("Have you beat the game?  ")
        edit_entry[8] = beat
        
        print("Current Purchase Date: ", edit_entry[9])
        purchase_date = input("What is the New Purchase Date  ")
        edit_entry[9] = purchase_date
        
        print("Current price: ", edit_entry[10])
        price = input("What is the price?  ")
        edit_entry[10] = price       
        
        print("Current Notes: ", edit_entry[11])
        notes = input("Any New extra Notes?  ")
        edit_entry[11] = notes

        
        answer = input("Is this correct?  ")
        if answer.lower() in ("yes", "y"):
            valid = True   
            games[edit_key] = edit_entry    
    
    
def print_games():
    key_list = games.keys()
        
    for key in key_list:
        print()
        print("Genre: ", games[key][0])
        print("Title: ", games[key][1])
        print("Developer: ", games[key][2])
        print("Publisher: ", games[key][3])
        print("Platform: ", games[key][4])
        print("Release Date: ", games[key][5])
        print("Rating: ", games[key][6])
        print("Single/Multi/Both: ", games[key][7])
        print("Beat the game?: ", games[key][8])    
        print("Pruchase Date: ", games[key][9])
        print("Extra Notes: ", games[key][10])
        print("----------------------")
        
def search_by_genre():
    found_one = False
    name = input("What Genre would you like?  ")
    for key in games.keys():
        if name == games[key][0]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("Platform: ", games[key][4])
            print("Release Date: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Single/Multi/Both: ", games[key][7])
            print("Beat the game?: ", games[key][8])    
            print("Pruchase Date: ", games[key][9])
            print("Extra Notes: ", games[key][10])
            print("----------------------")              
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")    
        
def search_by_title():
    found_one = False
    name = input("What Title would you like?  ")
    for key in games.keys():
        if name == games[key][1]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("Platform: ", games[key][4])
            print("Release Date: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Single/Multi/Both: ", games[key][7])
            print("Beat the game?: ", games[key][8])    
            print("Pruchase Date: ", games[key][9])
            print("Extra Notes: ", games[key][10])
            print("----------------------")              
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")
        
def search_by_developer():
    found_one = False
    name = input("What Developer would you like?  ")
    for key in games.keys():
        if name == games[key][2]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("Platform: ", games[key][4])
            print("Release Date: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Single/Multi/Both: ", games[key][7])
            print("Beat the game?: ", games[key][8])    
            print("Pruchase Date: ", games[key][9])
            print("Price: ", games[key][10])
            print("Extra Notes: ", games[key][11])
            print("----------------------")              
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")
        
def search_by_publisher():
    found_one = False
    name = input("What Publisher would you like?  ")
    for key in games.keys():
        if name == games[key][3]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("Platform: ", games[key][4])
            print("Release Date: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Single/Multi/Both: ", games[key][7])
            print("Beat the game?: ", games[key][8])    
            print("Pruchase Date: ", games[key][9])
            print("Price: ", games[key][10])
            print("Extra Notes: ", games[key][11])
            print("----------------------")              
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")
        
        
def search_by_Platform():
    found_one = False
    name = input("What Platform would you like?  ")
    for key in games.keys():
        if name == games[key][4]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("Platform: ", games[key][4])
            print("Release Date: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Single/Multi/Both: ", games[key][7])
            print("Beat the game?: ", games[key][8])    
            print("Pruchase Date: ", games[key][9])
            print("Price: ", games[key][10])
            print("Extra Notes: ", games[key][11])
            print("----------------------")              
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")
        
def search_by_release_date():
    found_one = False
    name = input("What Date would you like?  ")
    for key in games.keys():
        if name == games[key][5]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("Platform: ", games[key][4])
            print("Release Date: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Single/Multi/Both: ", games[key][7])
            print("Beat the game?: ", games[key][8])    
            print("Pruchase Date: ", games[key][9])
            print("Price: ", games[key][10])
            print("Extra Notes: ", games[key][11])
            print("----------------------")              
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")
        
def search_by_rating():
    found_one = False
    name = input("What title would you like?  ")
    for key in games.keys():
        if name == games[key][6]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("Platform: ", games[key][4])
            print("Release Date: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Single/Multi/Both: ", games[key][7])
            print("Beat the game?: ", games[key][8])    
            print("Pruchase Date: ", games[key][9])
            print("Price: ", games[key][10])
            print("Extra Notes: ", games[key][11])
            print("----------------------")              
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")
        
def search_by_single_multi():
    found_one = False
    name = input("Is the game single or multiplayer  ")
    for key in games.keys():
        if name == games[key][7]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("Platform: ", games[key][4])
            print("Release Date: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Single/Multi/Both: ", games[key][7])
            print("Beat the game?: ", games[key][8])    
            print("Pruchase Date: ", games[key][9])
            print("Price: ", games[key][10])
            print("Extra Notes: ", games[key][11])
            print("----------------------")              
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")
        
def search_by_beat_it():
    found_one = False
    name = input("Have you beat it?  ")
    for key in games.keys():
        if name == games[key][8]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("Platform: ", games[key][4])
            print("Release Date: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Single/Multi/Both: ", games[key][7])
            print("Beat the game?: ", games[key][8])    
            print("Pruchase Date: ", games[key][9])
            print("Price: ", games[key][10])
            print("Extra Notes: ", games[key][11])
            print("----------------------")              
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")
        
def search_by_purchase_date():
    found_one = False
    name = input("What purchase date would you like?  ")
    for key in games.keys():
        if name == games[key][9]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("Platform: ", games[key][4])
            print("Release Date: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Single/Multi/Both: ", games[key][7])
            print("Beat the game?: ", games[key][8])    
            print("Pruchase Date: ", games[key][9])
            print("Price: ", games[key][10])
            print("Extra Notes: ", games[key][11])
            print("----------------------")              
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")
        
def search_by_price():
    found_one = False
    name = input("What price would you like?  ")
    for key in games.keys():
        if name == games[key][10]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("Platform: ", games[key][4])
            print("Release Date: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Single/Multi/Both: ", games[key][7])
            print("Beat the game?: ", games[key][8])    
            print("Pruchase Date: ", games[key][9])
            print("Price: ", games[key][10])
            print("Extra Notes: ", games[key][11])
            print("----------------------")              
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")
    
def remove_game():
    for key in games.keys():
        print(key, "-", games[key][1])    
    selected_key = input("What is the game you would like to remove")
    selected_key = int(selected_key)    
    if selected_key in games.keys():
        try:
            for keys in range(1, len(games)+1):
                if keys>= selected_key and keys != len(games):
                    games[keys] = games[keys+1]
                    if keys == len(games):
                        games.pop(keys)
        except:
            print("Error message")
    else:
        print("error message jeded")
    
    
def save_data():
    datafile = open("game_lib.pickle", "wb")
    pickle.dump(games, datafile)
    datafile.close()
    print("File Saved")
    
def quit():
    choice = input("Would you like to save?: ")
    if choice == "yes":
        save_data()
    elif choice == "no":
        pickle_file = open("datafile.pickle", "wb")
        pickle.dump(games, pickle_file)
        pickle_file.close()
    else:
        print("*** NOT A VALID CHOICE ***\n")    
    
def search():
    print('''
    1)Genre:
    2)Title:
    3)Developer:
    4)Publisher:
    5)Platform:
    6)Year Released:
    7)Rating:
    8)Single Or Multiplayer
    9)Beat Game:
    10)Purchase Date:
    11)Price:
    ''')
    choice = input("What would you like to search for?  ")
    if choice == "Genre":
        search_by_genre()
    elif choice == "Title":
        search_by_title()
    elif choice == "Developer":
        search_by_developer()
    elif choice == "Publisher":
        search_by_publisher()
    elif choice == "Platform":
        search_by_Platform()
    elif choice == "Year Release":
        search_by_release_date()
    elif choice == "Rating":
        search_by_rating()
    elif choice == "Single or Multiplayer":
        search_by_single_multi()
    elif choice == "Beat Game":
        search_by_beat_it()
    elif choice == "Purchase Date":
        search_by_purchase_date()        
    elif choice == "Price":
        search_by_price()
    
    else:
        print("*** NOT A VALID CHOICE ***\n")    
    
keep_going = True

datafile = open("game_lib.pickle", "rb")
games = pickle.load(datafile)
datafile.close()




while keep_going:
    print("""
    
    MAIN MENU
    1) Add New Game
    2) Edit Game
    3) Print All Games
    4) Search Game By Category
    5) Remove A Game
    6) Save Database
    
    Q) Quit
    
    """)
    choice = input("What would you like to select?")
    if choice == "1":
        add_game()
    elif choice == "2":
        edit_game()
    elif choice == "3":
        print_games()
    elif choice == "4":
        search()
    elif choice == "5":
        remove_game()
    elif choice == "6":
        save_data()
    elif choice == "Q" or choice == "q":
        quit()
        keep_going = False
        
print("\nGoodbye.")    