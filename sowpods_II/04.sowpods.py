# What are all of the words that start with “PRO”, end in “ING”, and are exactly 11 letters long?

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

result = []

for word in words:
    if len(word) == 11 and word.startswith("PRO") and word.endswith("ING"):
        result.append(word)

print(result)
