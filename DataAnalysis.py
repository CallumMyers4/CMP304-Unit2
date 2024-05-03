def maxValues(players, matches):
    total_goals_pp = players['core_goals'].sum()
    avg_goals = total_goals_pp / matches
    most_goals = total_goals_pp.max()
    norm_goals = avg_goals / most_goals
    print(norm_goals)

    total_assists_pp = players['core_assists'].sum()
    avg_assists = total_assists_pp / matches
    most_assists = total_assists_pp.max()
    norm_assists = avg_assists / most_assists
    print(norm_assists)

    total_saves_pp = players['core_saves'].sum()
    avg_saves = total_saves_pp / matches
    most_saves = total_saves_pp.max()
    norm_saves = avg_saves / most_saves
    print (norm_saves)

    total_demos = players['demo_inflicted'].sum()
    avg_demos = total_demos / matches
    most_demos = total_demos.max()
    norm_demos = avg_demos / most_demos
    print (norm_demos)

    total_time_supersonic_pp = players['movement_percent_supersonic_speed'].sum()
    avg_time_supersonic = total_time_supersonic_pp / matches
    most_time_supersonic = total_time_supersonic_pp.max()
    norm_time_supersonic = avg_time_supersonic / most_time_supersonic
    print (norm_time_supersonic)