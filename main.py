import matplotlib.pyplot as plt
import DataPreparation as dataPrep
import DataAnalysis as dataAnalysis

region_check = input("Enter region to classify: ")
dataPrep.matchesPlayed()
region_data = dataPrep.selectRegion(region_check)

player_data = region_data.groupby('player_id')   #gets the average per game by finding the sum of all values and dividing by the number of 
                                            #times that player appeared in the dataset
matches_played = player_data.size()     #the size of the player_data variable will show how many matches each player participated in - 
                                        #therefore can be useful for averages
dataAnalysis.maxValues(player_data, matches_played)