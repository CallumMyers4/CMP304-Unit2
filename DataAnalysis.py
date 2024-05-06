from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from statistics import mean
import UserTesting as tests

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

#dictionary list to store classes against player IDs (the correct one then the predicted one)
playerClassifications = {}
playerClassificationsAI = {}

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

        #set rules for each class
        if  norm_demos > avg_demos_ovr and norm_time_supersonic > avg_supersonic_ovr:
            playerClassifications[player_id] = "Maniac"
        elif norm_goals > avg_goals_ovr and norm_saves < avg_saves_ovr and norm_assists < avg_assists_ovr:
            playerClassifications[player_id] = "Goalscorer"
        elif norm_goals > avg_goals_ovr and norm_assists > avg_assists_ovr and norm_saves < avg_saves_ovr:
            playerClassifications[player_id] = "Playmaker"
        elif norm_saves > avg_saves and norm_goals < avg_goals_ovr and norm_assists < avg_assists_ovr:
            playerClassifications[player_id] = "Goalkeeper"
        elif norm_demos > avg_demos_ovr and norm_saves > avg_saves_ovr and norm_goals < avg_goals_ovr:
            playerClassifications[player_id] = "Defender"
        elif (norm_goals > (avg_goals_ovr * 0.8) and norm_goals < (avg_goals_ovr * 1.2) 
              and norm_assists > (avg_assists_ovr * 0.8) and norm_assists < (avg_assists_ovr * 1.2)
              and norm_saves > (avg_saves_ovr * 0.8) and norm_saves < (avg_saves_ovr * 1.2)):
            playerClassifications[player_id] = "All Rounder"
        elif norm_goals > avg_goals_ovr and norm_assists > avg_assists_ovr and norm_saves > avg_saves_ovr:
            playerClassifications[player_id] = "MVP"
        elif norm_goals < avg_goals_ovr and norm_assists < avg_assists_ovr and norm_saves < avg_saves_ovr:
            playerClassifications[player_id] = "Weak link"
        else:
            playerClassifications[player_id] = "Unclassified"

    tests.drawPieCharts(playerClassifications, players)

def classifyPlayersAI(players, matches):
    X = []  # player stats
    y = []  # class names
    player_predictions = {}

    for player_id, player_data in players:
        #iterate over every row
        for index, row in player_data.iterrows():
            stats = [
                row['core_goals'] / matches[player_id],
                row['core_assists'] / matches[player_id],
                row['core_saves'] / matches[player_id],
                row['demo_inflicted'] / matches[player_id],
                row['movement_percent_supersonic_speed'] / matches[player_id]
            ]
            X.append(stats)

            # have AI decide on the correct class based on the rules
            classification = playerClassifications[player_id]

            if classification == "Maniac":
                y.append(1)
            elif classification == "Goalscorer":
                y.append(2)
            elif classification == "Playmaker":
                y.append(3)
            elif classification == "Goalkeeper":
                y.append(4)
            elif classification == "Defender":
                y.append(5)
            elif classification == "All Rounder":
                y.append(6)
            elif classification == "MVP":
                y.append(7)
            elif classification == "Weak link":
                y.append(8)
            else:
                y.append(9)

    #split the data into enough to train the AI, then enough to test this learning
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #begin to train the AI
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    #make predictions
    y_predict = clf.predict(X_test)
    print("Number of keys in players dictionary:", len(players))

    #iterate through the AI's predictions and store them in a second dictionary
    for i, (player_id, _) in enumerate(players):
       playerClassificationsAI[player_id ] = player_predictions[player_id] = y_predict[i]
    print(playerClassificationsAI)
    tests.drawPieChartsAI(playerClassificationsAI, players)