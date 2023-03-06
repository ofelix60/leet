# What are all of the words with no vowel and not even a Y?

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

result = []

for word in words:
    if (
        "A" not in word
        and "E" not in word
        and "I" not in word
        and "O" not in word
        and "U" not in word
        and "Y" not in word
    ):
        result.append(word)

print(result)
