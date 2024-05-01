import numpy
import pandas
import matplotlib.pyplot as plt

#calculate number of matches played per player
playerDataMatch = "rl_data/matches_by_players.csv"
playersData = pandas.read_csv(playerDataMatch)
playersData.head()

rowsPerPlayer = playersData.groupby('player_id').size().reset_index(name='matches_played')
rowsPerPlayer.head()

fig, ax = plt.subplots()
plt.hist(rowsPerPlayer['matches_played'], density=True, bins=30)
ax = plt.gca()
plt.show()