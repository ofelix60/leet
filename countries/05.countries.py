# What countries use only one vowel in their name (the vowel can be used multiple times)
#   - For example, if the word “BEEKEEPER” were a country, it would be an answer, because it only uses “E”.

import re

with open("countries.txt", "r") as f:
    countries = [line.rstrip() for line in f]

pattern = r"[aeiouAEIOU]"
result = []

for country in countries:
    vowelsSet = set(re.findall(pattern, country.lower()))
    if len(vowelsSet) == 1:
        result.append(country)

print(result)
