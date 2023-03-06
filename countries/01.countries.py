# What are all of the countries that have “United” in the name?

with open("countries.txt", "r") as f:
    countries = f.read().split("\n")

result = []

for country in countries:
    if "United" in country:
        result.append(country)

print(result)
