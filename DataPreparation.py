import numpy
import pandas
import matplotlib.pyplot as plt

#calculate number of matches played per player
def matchesPlayed():
    #read in file
    playerDataMatch = "rl_data/matches_by_players.csv"
    global playersData 
    playersData = pandas.read_csv(playerDataMatch)
    playersData.head()

    #group each row containing the same value in the player_id column
    rowsPerPlayer = playersData.groupby('player_id').size().reset_index(name='matches_played')
    rowsPerPlayer.head()

    fig, ax = plt.subplots()
    plt.hist(rowsPerPlayer['matches_played'], density=True, bins=30)
    ax = plt.gca()
    plt.show()

def selectPlayer(playerName):
    player_data = playersData[playersData['player_tag'] == playerName]
    #player_data = player_data[playersData['match_id'] == '6159ad3d143c37878b2384a9'] #(used to make testing easier)
    goals_per_player = player_data.groupby('player_id')['core_goals'].sum()     #calculate total value in core_goals category with valid match

    #plot as bar graph
    plt.bar(goals_per_player.index, goals_per_player.values)
    plt.xlabel('Player ID')
    plt.ylabel('Total Goals Scored')
    plt.title('Total Goals Scored by Each Player Across All Matches')
    plt.show()


#main
player_name = 'Amphis'
matchesPlayed()
selectPlayer(player_name)