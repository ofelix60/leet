# What are all of the words that have all 5 vowels, in alphabetical order?

import re

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

vowels = ["A", "E", "I", "O", "U"]
wordsAllVowels = []
result = []

for word in words:
    vowelsInWord = re.sub("[^AEIOU]", "", word)
    if vowels == list(vowelsInWord):
        result.append(word)


print(result)
