# What countries both begin and end with a vowel?

with open("countries.txt", "r") as f:
    countries = [line.rstrip() for line in f]

vowels = [
    "A",
    "E",
    "I",
    "O",
    "U",
]
result = []

for country in countries:
    if country[0] in vowels and country[len(country) - 1].upper() in vowels:
        result.append(country)

print(result)
