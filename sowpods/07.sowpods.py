# What are all of the words that both start and end with a Y?

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

result = []

for word in words:
    if word.startswith("Y") and word.endswith("Y"):
        result.append(word)

print(result)
