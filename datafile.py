#!usr/bin/python3
#Austin Andrews
#01/28/2020

import pickle

games = { 1 :['FPS', 'Halo3', 'Bunjee', 'Microsoft', 'Xbox360', '2007', '10', 'either',
              'yes', '1/5/2008', '30.00', 'This game blows chunks']}
datafile = open("game_lib.pickle", "wb")
pickle.dump(games, datafile)
datafile.close()

