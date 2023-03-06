# What is the longest word that contains no vowels?
# What is the longest word that contains no vowels?

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

length = 0
result = ""

for word in words:
    if (
        len(word) > length
        and "A" not in word
        and "E" not in word
        and "I" not in word
        and "O" not in word
        and "U" not in word
    ):
        result = word
        length = len(word)

print(result)
