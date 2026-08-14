team = {'CSK': {'captain': 'Dhoni', 'players': 18}, 
        'MI': {'captain': 'Rohit', 'players': 17}}
team2={'RCB': {'captain': 'Rajat', 'players': 16}}
team.update(team2)

for i in team:
    print(i,"-",team[i]["captain"])
