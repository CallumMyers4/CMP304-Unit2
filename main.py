import matplotlib.pyplot as plt
import DataPreparation as dataPrep
import DataAnalysis as dataAnalysis
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans 

region_check = input("Enter region to classify: ")
dataPrep.matchesPlayed()
region_data = dataPrep.selectRegion(region_check)

player_data = region_data.groupby('player_id')   #gets the average per game by finding the sum of all values and dividing by the number of 
                                            #times that player appeared in the dataset
matches_played = player_data.size()     #the size of the player_data variable will show how many matches each player participated in - 
                                        #therefore can be useful for averages
dataAnalysis.maxValues(player_data, matches_played)

#perform a elbow check to determine the best cluster value
elbowCheck = 12 #max number of clusters to check
wss = []

for e in range(1, elbowCheck + 1):
    # Run KMeans for the current number of clusters
    kmeans = KMeans(n_clusters=e, random_state=0, n_init="auto").fit(player_data[['core_goals']]) 
    # Append the inertia_ value to wss
    wss.append(kmeans.inertia_)