# What are all of the words that have all 5 vowels, in any order?

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

result = []

for word in words:
    if "A" in word and "E" in word and "I" in word and "O" in word and "U" in word:
        result.append(word)

print(result)
