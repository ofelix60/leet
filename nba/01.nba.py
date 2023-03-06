# Write a function that takes as an argument a year and returns the winner of the NBA finals that year.

with open("nba_finals.csv", "r") as f:
    finals = [dict(zip(["year", "winner", "loser", "score", "mvp"], line.rstrip().split(","))) for line in f]


def somefunction(year):
    for final in finals:
        if final["year"] == str(year):
            return final


# print(finals[1][{year}])

print(somefunction(1991))
