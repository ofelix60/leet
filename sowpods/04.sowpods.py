# What are all of the words that contain the word CAT and are exactly 5 letters long?

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

result = []

for word in words:
    if "CAT" in word and len(word) == 5:
        result.append(word)

print(result)
