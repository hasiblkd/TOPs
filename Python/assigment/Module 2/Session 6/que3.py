teams = ["CSK", "MI", "GT", "RCB", "KKR"]
points = [12, 8, 14, 10, 16]
team_points = dict(zip(teams, points))
for team in team_points:
    if team_points[team] > 10:
        print(team, "-", team_points[team])