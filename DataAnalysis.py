from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from statistics import mean

#create lists to store running totals for each average
total_goals_list = []
total_assists_list = []
total_saves_list = []
total_demos_list = []
total_supersonic_list = []

norm_goals_list = []
norm_assists_list = []
norm_saves_list = []
norm_demos_list = []
norm_supersonic_list = []

def classifyPlayers(players, matches):
    #get averages for each player in the dataset
    for player_id, player_data in players:
        filled_data = player_data[['core_goals', 'core_assists', 'core_saves', 'demo_inflicted', 'movement_percent_supersonic_speed']].fillna(0)
        total_goals = filled_data['core_goals'].sum()
        total_goals_list.append(total_goals)
        most_goals = max(total_goals_list)

        total_assists = filled_data['core_assists'].sum()
        total_assists_list.append(total_assists)
        most_assists = max(total_assists_list)

        total_saves = filled_data['core_saves'].sum()
        total_saves_list.append(total_saves)
        most_saves = max(total_saves_list)

        total_demos = filled_data['demo_inflicted'].sum()
        total_demos_list.append(total_demos)
        most_demos = max(total_demos_list)

        total_supersonic = filled_data['movement_percent_supersonic_speed'].sum()
        total_supersonic_list.append(total_supersonic)
        most_supersonic = max(total_supersonic_list)

    for player_id, player_data in players:
        filled_data = player_data[['core_goals', 'core_assists', 'core_saves', 'demo_inflicted', 'movement_percent_supersonic_speed']].fillna(0)
        total_goals = filled_data['core_goals'].sum()
        avg_goals = total_goals / matches[player_id]
        norm_goals = avg_goals / most_goals

        total_assists = filled_data['core_assists'].sum()
        avg_assists = total_assists / matches[player_id]
        norm_assists = avg_assists / most_assists

        total_saves = filled_data['core_saves'].sum()
        avg_saves = total_saves / matches[player_id] 
        norm_saves = avg_saves / most_saves

        total_demos = filled_data['demo_inflicted'].sum()
        avg_demos = total_demos / matches[player_id] 
        norm_demos = avg_demos / most_demos

        total_time_supersonic = filled_data['movement_percent_supersonic_speed'].sum()
        avg_time_supersonic = total_time_supersonic / matches[player_id]
        norm_time_supersonic = avg_time_supersonic / most_supersonic

        #add normalized values to the lists
        norm_goals_list.append(norm_goals)
        norm_assists_list.append(norm_assists)
        norm_saves_list.append(norm_saves)
        norm_demos_list.append(norm_demos)
        norm_supersonic_list.append(norm_time_supersonic)

    #calculate overal averages
    avg_goals_ovr = mean(norm_goals_list)
    avg_assists_ovr = mean(norm_assists_list)
    avg_saves_ovr = mean(norm_saves_list)
    avg_demos_ovr = mean(norm_demos_list)
    avg_supersonic_ovr = mean(norm_supersonic_list)

    for player_id, player_data in players:
        print(avg_goals_ovr)
        print(avg_assists_ovr)
        print(avg_saves_ovr)
        print(avg_demos_ovr)
        print(avg_supersonic_ovr)

        if norm_goals > avg_goals_ovr:
            print(f"Player {player_id} is a goal scorer.")
        elif norm_assists > avg_assists_ovr:
            print(f"Player {player_id} is an assist provider.")
        elif norm_saves > avg_saves_ovr:
            print(f"Player {player_id} is a goalie.")
        elif norm_demos > avg_demos_ovr:
            print(f"Player {player_id} is a demo expert.")
        elif norm_time_supersonic > avg_supersonic_ovr:
            print(f"Player {player_id} spends a lot of time supersonic.")
        else:
            print(f"Player {player_id} does not fit any classification.")