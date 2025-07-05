def total_matches(n_teams):
    return n_teams * (n_teams - 1) // 2

def total_points(total_matches, draws):
    win_loss_matches = total_matches - draws
    return draws * 2 + win_loss_matches * 3

def average_points(total_points, total_matches):
    return total_points / total_matches

# Data Problem
n_teams = 14
draws = 23

matches = total_matches(n_teams)
points = total_points(matches, draws)
average = average_points(points, matches)

print("Total matches:", matches)
print("The total points of the whole tournament:", points)
print("The average points per game:", round(average, 3))