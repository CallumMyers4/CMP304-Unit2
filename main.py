import matplotlib.pyplot as plt
import DataPreparation as dataPrep
import DataAnalysis as dataAnalysis

dataPrep.readData()     #read in data files

optimal_clusters = 160      #decided from elbow graph
elbow = input("Enter 1 to see graph, any other input to skip ")      #gives user option whether or not to see graph of optimal clusters

if elbow == '1':
    dataPrep.plotElbow()


region_check = input("Enter region to classify: ")  #user selects which region to extract data from   
region_data = dataPrep.selectRegion(region_check)   #select players from a single region
player_data = region_data.groupby('player_id')      #groups all rows relating to the same player
matches_played = player_data.size()   #the size of the player_data variable will show how many matches each player participated in - 
                                        #therefore can be useful for averages
dataPrep.getClusters(optimal_clusters, player_data)  #get the appropriate clusters using the optimal amount decided from the elbow check

dataAnalysis.classifyPlayers(player_data, matches_played)  #gets max, avg and normalized values for all essential player data
dataAnalysis.classifyPlayersAI(player_data, matches_played)  #gets max, avg and normalized values for all essential player data