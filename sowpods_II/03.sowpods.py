# What are all of the words that have only “E”s for vowels and are at least 15 letters long?

import re

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

result = []

for word in words:
    vowels = set(re.sub("[^AEIOU]", "", word))
    if len(list(vowels)) == 1 and list(vowels)[0] == "E" and len(word) >= 15:
        result.append(word)

print(result)
