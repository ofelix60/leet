# What are all of the words that can be made without the letters in “AEIOSHRTN” (in other words, without the most common letters)?

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

bank = {"A": "A", "E": "E", "I": "I", "O": "O", "S": "S", "H": "H", "R": "R", "T": "T", "N": "N"}
result = []

for word in words:
    x = True
    for letter in word:
        if letter in bank:
            x = False
            break
    if x:
        result.append(word)

print(result)
