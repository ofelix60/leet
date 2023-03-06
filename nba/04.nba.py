# Print out a ranking of who has won the MVP more than once, by times won, e.g. this output:

# - 6 times: Michael Jordan
# - 3 times: Shaquille O'Neal, LeBron James
# - 2 times: <etc>


with open("nba_finals.csv", "r") as f:
    finals = [dict(zip(["year", "winner", "loser", "score", "mvp"], line.rstrip().split(","))) for line in f]

ranked = {}

for final in finals:
    if final["mvp"] not in ranked:
        ranked[final["mvp"]] = 1
    else:
        ranked[final["mvp"]] += 1

top_ranked = ranked.items()

ordered_ranked = {}


for player in top_ranked:
    if player[0] != "" and player[1] > 1 and player[1] not in ordered_ranked:
        ordered_ranked[player[1]] = player[0]
    elif player[0] != "" and player[1] > 1:
        ordered_ranked[player[1]] += ", " + player[0]

x = ordered_ranked.items()

for y in reversed(x):
    print(f"{y[0]} times: {y[1]}")
