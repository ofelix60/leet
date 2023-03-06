# What are all of the words containing an X and a Y and a Z

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

result = []

for word in words:
    if "X" in word and "Y" in word and "Z" in word:
        result.append(word)

print(result)
