# Create and print an array containing all of the words that end in "GHTLY"

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

result = []

for word in words:
    if word.endswith("GHTLY"):
        result.append(word)

print(result)
