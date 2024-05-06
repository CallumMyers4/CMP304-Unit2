import pandas
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans 

#calculate number of matches played per player
def readData():
    #read in file
    playerDataMatch = "rl_data/matches_by_players.csv"
    global playersData 
    playersData = pandas.read_csv(playerDataMatch)

    #fills in any missing data from specific columns to avoid NaN (not a number) errors later on
    global filled_data
    filled_data = playersData[['core_goals', 'core_assists', 'core_saves', 'demo_inflicted', 'movement_percent_supersonic_speed']].fillna(0)

#filters data into a specific region chosen by the user
def selectRegion(region):
    player_data = playersData[playersData['team_region'] == region]

    return player_data

#creates a graph which will show the elbow where the results of adding more clusters into the program is unlikely to improve performace
#this point of optimal clusters will be where the graph flattens out
def plotElbow():
    elbowCheck = 150 #max number of clusters to check
    global wss 
    wss = []

    print("Calculating line...")
    # Run KMeans for the current number of clusters
    for e in range(1, elbowCheck + 1):
        kmeans = KMeans(n_clusters=e, random_state=0, n_init="auto").fit(filled_data) 
        # Append the inertia_ value to wss
        wss.append(kmeans.inertia_)
    
    print("Plotting graph...")
    plt.plot(wss) 
    plt.show()