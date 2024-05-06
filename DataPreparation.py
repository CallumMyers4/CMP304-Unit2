import numpy
import pandas
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans 

#calculate number of matches played per player
def readData():
    #read in file
    playerDataMatch = "rl_data/matches_by_players.csv"
    global playersData 
    playersData = pandas.read_csv(playerDataMatch)

def plotElbow():
    elbowCheck = 150 #max number of clusters to check
    wss = []

    for e in range(1, elbowCheck + 1):
        #creates a new dataset suitable for the elbow check using only numerical required data and filling in empty gaps with 0
        filled_data = playersData[['core_goals', 'core_assists', 'core_saves', 'demo_inflicted', 'movement_percent_supersonic_speed']].fillna(0)
        # Run KMeans for the current number of clusters
        kmeans = KMeans(n_clusters=e, random_state=0, n_init="auto").fit(filled_data) 
        # Append the inertia_ value to wss
        wss.append(kmeans.inertia_)

    print("Plotting graph...")
    plt.plot(wss) 
    plt.show()
    print("Graph plotted.")

def selectRegion(region):
    player_data = playersData[playersData['team_region'] == region]

    return player_data