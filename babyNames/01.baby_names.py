# What is the shortest baby name in the top 40 baby names for 2020?

with open("baby_names_1880_short.txt", "r") as f:
    names_1880 = [line.rstrip() for line in f]

with open("baby_names_2020_short.txt", "r") as f:
    names = [line.rstrip() for line in f]

shortest = "abcdefghijklmnopqrstuvwxyz"

for name in names:
    if len(name) < len(shortest):
        shortest = name

print(shortest)
