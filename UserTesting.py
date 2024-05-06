import matplotlib.pyplot as plt

def drawPieCharts(classes, dataset):
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

    print("Maniacs:", maniacs)
    print("Goalscorers:", goalscorers)
    print("Playmakers:", playmakers)
    print("Goalkeepers:", goalkeepers)
    print("Defenders:", defenders)
    print("All Rounders:", all_rounders)
    print("MVPs:", MVPs)
    print("Weak Links:", weak_links)
    print("Undefined:", others)

    labels = 'Maniac', 'Goalscorer', 'Playmaker', 'Goalkeeper', 'Defender', 'All Rounder', 'MVP', "Weak Link", "Undefined"
    sizes = [maniacs, goalscorers, playmakers, goalkeepers, defenders, all_rounders, MVPs, weak_links, others]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%')

    plt.show()



def drawPieChartsAI(classes, dataset):
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

    print("Maniacs:", maniacs)
    print("Goalscorers:", goalscorers)
    print("Playmakers:", playmakers)
    print("Goalkeepers:", goalkeepers)
    print("Defenders:", defenders)
    print("All Rounders:", all_rounders)
    print("MVPs:", MVPs)
    print("Weak Links:", weak_links)
    print("Undefined:", others)

    labels = 'Maniac', 'Goalscorer', 'Playmaker', 'Goalkeeper', 'Defender', 'All Rounder', 'MVP', "Weak Link", "Undefined"
    sizes = [maniacs, goalscorers, playmakers, goalkeepers, defenders, all_rounders, MVPs, weak_links, others]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%')

    plt.show()