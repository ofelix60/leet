# What are the longest baby names in the top 40 baby names for 2020? Make sure you can handle if there’s a tie.

with open("baby_names_1880_short.txt", "r") as f:
    names_1880 = [line.rstrip() for line in f]

with open("baby_names_2020_short.txt", "r") as f:
    names = [line.rstrip() for line in f]

length = 0
result = []

for name in names:
    if len(name) > length:
        length = len(name)
        result = []
        result.append(name)
    elif len(name) == length:
        result.append(name)


print(result)
