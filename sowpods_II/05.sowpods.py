# What are the shortest words that start with “PRO” and end in “ING”? Make sure your solution can handle ties.

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

result = ["abcdefghijklmnopqrstuvwxyz"]

for word in words:
    if word.startswith("PRO") and word.endswith("ING") and len(word) < len(result[0]):
        result = [word]
    if word.startswith("PRO") and word.endswith("ING") and len(word) == len(result[0]):
        result.append(word)

print(result)
