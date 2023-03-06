# What is the shortest country name? Make sure your solution can handle ties.

with open("countries.txt", "r") as f:
    countries = [line.rstrip() for line in f]

lookup = {}

for country in countries:
    if len(country) not in lookup:
        lookup[len(country)] = []
    lookup[len(country)].append(country)

print(lookup[min(lookup)])
