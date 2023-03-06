# Write a function that takes as an argument a team name and returns an array of all of the years the team has won the NBA finals.

with open("nba_finals.csv", "r") as f:
    finals = [dict(zip(["year", "winner", "loser", "score", "mvp"], line.rstrip().split(","))) for line in f]


def somefunction(team):
    result = []
    for final in finals:
        if final["winner"] == team:
            result.append(final["year"])
    return result


print(somefunction("Chicago Bulls"))
