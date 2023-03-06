# What country names are > 50% vowels?

import re

with open("countries.txt", "r") as f:
    countries = [line.rstrip() for line in f]

pattern = r"[aeiouAEIOU]"
result = []

for country in countries:
    vowelsLength = len(re.findall(pattern, country))
    if vowelsLength > len(country.replace(" ", "")) // 2:
        print(country)


print(countries)
