import matplotlib.pyplot as plt

#draws pie chart for manual classification
def drawPieCharts(classes, dataset):
    #default vars which will decide size of each section
    maniacs = 0 
    goalscorers = 0
    playmakers = 0
    goalkeepers = 0
    defenders = 0
    all_rounders = 0
    MVPs = 0
    weak_links = 0
    others = 0

    #iterate through the classes dictionary
    for player_id, player_data in dataset:

        #get the class string from each player ID
        classification = classes[player_id]

        #add one to the counter of the appropriate class as it is found in dictionary
        if classification == "Maniac":
            maniacs += 1
        elif classification == "Goalscorer":
            goalscorers += 1
        elif classification == "Playmaker":
            playmakers += 1
        elif classification == "Goalkeeper":
            goalkeepers += 1
        elif classification == "Defender":
            defenders += 1
        elif classification == "All Rounder":
            all_rounders += 1
        elif classification == "MVP":
            MVPs += 1
        elif classification == "Weak link":
            weak_links += 1
        else:
            others += 1

    #define labels for each section
    labels = 'Maniac', 'Goalscorer', 'Playmaker', 'Goalkeeper', 'Defender', 'All Rounder', 'MVP', "Weak Link", "Undefined"

    #use the counters to correctly size each section next to their labels
    sizes = [maniacs, goalscorers, playmakers, goalkeepers, defenders, all_rounders, MVPs, weak_links, others]

    #create the pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%')    #uses sizes and labels lists from above, autopct rounds each section to 1dp

    #display
    plt.show()

#draws pie chart for AI classification
def drawPieChartsAI(classes, dataset):
    #all is exactly the same as the function above, except the first iterator works slightly differently
    maniacs = 0 
    goalscorers = 0
    playmakers = 0
    goalkeepers = 0
    defenders = 0
    all_rounders = 0
    MVPs = 0
    weak_links = 0
    others = 0

    for player_id, player_data in dataset:
        classification = classes[player_id]
        #largely the same as above, however since the AI is using integers to store class with each ID, it must check which integer
        #is found in each iteration instead of which string, could have been done in same function but this way is more maintainable
        if classification == 1:
            maniacs += 1
        elif classification == 2:
            goalscorers += 1
        elif classification == 3:
            playmakers += 1
        elif classification == 4:
            goalkeepers += 1
        elif classification == 5:
            defenders += 1
        elif classification == 6:
            all_rounders += 1
        elif classification == 7:
            MVPs += 1
        elif classification == 8:
            weak_links += 1
        else:
            others += 1

    labels = 'Maniac', 'Goalscorer', 'Playmaker', 'Goalkeeper', 'Defender', 'All Rounder', 'MVP', "Weak Link", "Undefined"
    sizes = [maniacs, goalscorers, playmakers, goalkeepers, defenders, all_rounders, MVPs, weak_links, others]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%')

    plt.show()