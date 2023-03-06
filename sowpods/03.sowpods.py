# What are all of the words containing a Q but not a U?

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

result = []

for word in words:
    if ("Q" in word) and ("U" not in word):
        result.append(word)


print(result)
