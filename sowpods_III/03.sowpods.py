# What are all of the words that have at least 3 different double letters? For example, “BOOKKEEPER” is an answer to this question because it has a double-O, a double-K, and a double-E.

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

result = []


for word in words:
    doubles = []
    for i in range(len(word) - 1):
        if word[i] == word[i + 1] and word[i] + word[i + 1] not in doubles:
            doubles.append(word[i] + word[i + 1])

        if len(doubles) >= 3:
            result.append(word)
            break

print(result)
