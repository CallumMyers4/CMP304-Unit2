import pandas
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans 

#calculate number of matches played per player
def readData():
    #read in file
    print(f"Reading in files...")
    playerDataMatch = "rl_data/matches_by_players.csv"
    global players_data 
    players_data = pandas.read_csv(playerDataMatch)

    #fills in any missing data from specific columns to avoid NaN (not a number) errors later on
    print(f"Filling out missing areas...")
    global filled_data
    filled_data = players_data[['core_goals', 'core_assists', 'core_saves', 'demo_inflicted', 'movement_percent_supersonic_speed']].fillna(0)

#filters data into a specific region chosen by the user
def selectRegion(region):
    print(f"Filtering by region...")
    player_data = players_data[players_data['team_region'] == region]

    return player_data

#creates a graph which will show the elbow where the results of adding more clusters into the program is unlikely to improve performace
#this point of optimal clusters will be where the graph flattens out
def plotElbow():
    elbow_check = 200 #max number of clusters to check
    global wss 
    wss = []

    print(f"Calculating line...")
    # Run KMeans for the current number of clusters
    for e in range(1, elbow_check + 1):
        kmeans = KMeans(n_clusters=e, random_state=0, n_init="auto").fit(filled_data) 
        # Append the inertia_ value to wss
        wss.append(kmeans.inertia_)
    
    print(f"Plotting graph...")
    plt.plot(wss) 
    plt.show()