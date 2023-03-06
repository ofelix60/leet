# What are all of the words containing UU

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

result = []

for word in words:
    if "UU" in word:
        result.append(word)

print(result)
