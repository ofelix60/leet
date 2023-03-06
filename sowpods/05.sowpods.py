# What are all of the words that have no E or A and are at least 15 letters long?

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

result = []

for word in words:
    if "E" not in word and "A" not in word and len(word) == 15:
        result.append(word)

print(result)
