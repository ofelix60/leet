# What is the shortest word that contains all 5 vowels?

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

shortest = 100
result = ""

for word in words:
    if len(word) < shortest and "A" in word and "E" in word and "I" in word and "O" in word and "U" in word:
        result = word
        shortest = len(result)

print(result)
