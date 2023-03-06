# Which teams have made it to the NBA finals but have never won?

with open("nba_finals.csv", "r") as f:
    finals = [dict(zip(["year", "winner", "loser", "score", "mvp"], line.rstrip().split(","))) for line in f]

winners = []
result = []

for final in finals:
    winners.append(final["winner"])


for final in finals:
    if final["loser"] not in winners and final["loser"] not in result:
        result.append(final["loser"])


print(result)
