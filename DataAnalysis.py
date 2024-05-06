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

#function to manually classify players - used to train AI and also compare the AI predictions against "true" classes
def classifyPlayers(players, matches):
    #finds the highest scoring value in each section of the dataset
    print(f"Manually classifying players...")
    print(f"Getting the highest scoring stats...")
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

    #finds each players average goals per game and then normalizes this by dividing it by the highest scoring
    print(f"Normalizing player data stats...")
    for player_id, player_data in players:
        #fill any blank spots in the dataset
        filled_data = player_data[['core_goals', 'core_assists', 'core_saves', 'demo_inflicted', 'movement_percent_supersonic_speed']].fillna(0)
        
        #calculate player's goals across all games, divide this by number of games they played to get average per game and
        #divide this by the most goals scored to normalize
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

    #calculate overall averages by taking the average of all normalized goals in the lists
    print(f"Calculating the average per stat...")
    avg_goals_ovr = mean(norm_goals_list)
    avg_assists_ovr = mean(norm_assists_list)
    avg_saves_ovr = mean(norm_saves_list)
    avg_demos_ovr = mean(norm_demos_list)
    avg_supersonic_ovr = mean(norm_supersonic_list)

    #gets the normal for each player's statistics again before comparing these to the classification rules and giving each player a class
    print(f"Checking players against class rulesets...")
    for player_id, player_data in players:
        #fill any blank spots in the dataset
        filled_data = player_data[['core_goals', 'core_assists', 'core_saves', 'demo_inflicted', 'movement_percent_supersonic_speed']].fillna(0)
        
        #calculate normalized stats
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

        #compare normalized values to rules for each class and store the correct class in the dictionary next to player ID
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

    #draw a pie chart showing the number of players per class
    print(f"Drawing chart of classes...")
    tests.drawPieCharts(playerClassifications, players)

#very similar to above function but done vi AI
def classifyPlayersAI(players, matches):
    print(f"Classifying players via AI...")
    X = []  # player stats
    y = []  # class names

    #scan over all of the dataset
    print(f"Populating AI training dataset...")
    for player_id, player_data in players:
        #iterate over every row
        for index, row in player_data.iterrows():
            #gets the stats per game for each player
            stats = [
                row['core_goals'] / matches[player_id],
                row['core_assists'] / matches[player_id],
                row['core_saves'] / matches[player_id],
                row['demo_inflicted'] / matches[player_id],
                row['movement_percent_supersonic_speed'] / matches[player_id]
            ]

            #add these stats to the AI's knowledge listW of player stats
            X.append(stats)

            #gets the classification of each player from the dictionary created above
            classification = playerClassifications[player_id]

            #turns each class into a value to make it easier for outputting from the AI (essentially works like having an int array instead
            #of a string array)
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
    print(f"Splitting AI datasets...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #begin to train the AI
    print(f"Training AI...")
    clf = DecisionTreeClassifier()      #creates a new decision tree classifier for supervised learning
    clf.fit(X_train, y_train)   #uses the player stats stored in X and labels attached to these stats in Y to learn the class rules

    #make predictions
    print(f"Making predictions...")
    y_predict = clf.predict(X_test)     #uses the portion of data stored in x_test to make predictions and stores these labels in y_predict

    #iterate through the AI's predictions and store them in a second dictionary
    print(f"Storing prediction results...")
    for i, (player_id, _) in enumerate(players):       #for loop which cycles through all of the players dataset
        playerClassificationsAI[player_id] = y_predict[i]   #stores all predicted classes into dictionary next to correct player ID

    print(f"Displaying predicted classes...")
    tests.drawPieChartsAI(playerClassificationsAI, players)     #draws a pie chart displaying how the AI predicted the split of classes