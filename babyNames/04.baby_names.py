# What are all of the names that were top 40 baby names in both 1880 and 2020?

with open("baby_names_1880_short.txt", "r") as f:
    names_1880 = [line.rstrip() for line in f]
    names_dict = dict.fromkeys(names_1880, None)

with open("baby_names_2020_short.txt", "r") as f:
    names = [line.rstrip() for line in f]

result = []

for name in names:
    if name in names_dict:
        result.append(name)

print(result)
