def maxValues(players, matches):
    total_goals_pp = players['core_goals'].sum()
    avg_goals = total_goals_pp / matches
    most_goals = total_goals_pp.max()
    print("Most goals: ", most_goals)
    print(avg_goals)

    total_assists_pp = players['core_assists'].sum()
    avg_assists = total_assists_pp / matches
    most_assists = total_assists_pp.max()
    print("Most assists: ", most_assists)
    print(avg_assists)

    total_saves_pp = players['core_saves'].sum()
    avg_saves = total_saves_pp / matches
    most_saves = total_saves_pp.max()
    print("Most saves: ", most_saves)
    print(avg_saves)

    total_demos = players['demo_inflicted'].sum()
    avg_demos = total_demos / matches
    most_demos = total_demos.max()
    print("Most demos: ", most_demos)
    print(avg_demos)

    total_time_supersonic_pp = players['movement_percent_supersonic_speed'].sum()
    avg_time_spent_supersonic = total_time_supersonic_pp / matches
    most_time_supersonic = total_time_supersonic_pp.max()
    print("Most percent of time supersonic: ", most_time_supersonic)
    print(avg_time_spent_supersonic)