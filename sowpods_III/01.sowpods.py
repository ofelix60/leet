# What is the longest word where no letter is used more than once?

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]


result = ""


for word in words:
    lookup = {}
    repeat = False
    for letter in word:
        if letter not in lookup:
            lookup[letter] = 1
        elif letter in lookup:
            repeat = True
            break
    if not repeat and len(word) > len(result):
        result = word

print(result)
