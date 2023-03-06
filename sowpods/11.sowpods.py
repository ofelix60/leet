# How many words contain the substring "TYPE”?

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

result = 0

for word in words:
    if "TYPE" in word:
        result += 1

print(result)
