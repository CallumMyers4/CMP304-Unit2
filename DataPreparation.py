import pandas
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans 

#calculate number of matches played per player
def readData():
    #read in file
    playerDataMatch = "rl_data/matches_by_players.csv"
    global playersData 
    playersData = pandas.read_csv(playerDataMatch)

    #fills in any missing data from specific columns
    global filled_data
    filled_data = playersData[['core_goals', 'core_assists', 'core_saves', 'demo_inflicted', 'movement_percent_supersonic_speed']].fillna(0)

def selectRegion(region):
    player_data = playersData[playersData['team_region'] == region]

    return player_data

def plotElbow():
    elbowCheck = 150 #max number of clusters to check
    global wss 
    wss = []

    print("Calculating line...")
    # Run KMeans for the current number of clusters
    for e in range(1, elbowCheck + 1):
        #creates a new dataset suitable for the elbow check using only numerical required data and filling in empty gaps with 0
        kmeans = KMeans(n_clusters=e, random_state=0, n_init="auto").fit(filled_data) 
        # Append the inertia_ value to wss
        wss.append(kmeans.inertia_)
    
    print("Plotting graph...")
    plt.plot(wss) 
    plt.show()

def getClusters(optimal, region_data):
    filled_data = region_data[['core_goals', 'core_assists', 'core_saves', 'demo_inflicted', 'movement_percent_supersonic_speed']].fillna(0)
    kmeans = KMeans(n_clusters = optimal, random_state = 0, n_init = "auto").fit(filled_data)
    clusterCentres  =  pandas.DataFrame(kmeans.cluster_centers_)   

    clusterCentres.columns = ['core_goals', 'core_assists', 'core_saves', 'core_demos', 'movement_percent_supersonic_speed']

    plt.scatter(clusterCentres['core_demos'], clusterCentres['core_saves'])
    ax = plt.gca()
    ax.set_xlabel('Demos')
    ax.set_ylabel('Saves')
    plt.show()