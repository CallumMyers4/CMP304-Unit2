import numpy
import pandas
import matplotlib.pyplot as plt

#calculate number of matches played per player
def matchesPlayed():
    #read in file
    playerDataMatch = "rl_data/matches_by_players.csv"
    global playersData 
    playersData = pandas.read_csv(playerDataMatch)

def selectRegion(region):
    player_data = playersData[playersData['team_region'] == region]

    return player_data