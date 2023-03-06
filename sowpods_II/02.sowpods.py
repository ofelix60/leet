# What are all of the words that have only “U”s for vowels?

import re

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]


result = []

for word in words:
    vowels = set(re.sub("[^AEIOU]", "", word))
    if len(list(vowels)) == 1 and list(vowels)[0] == "U":
        result.append(word)

print(result)
