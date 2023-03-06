# What is the longest word that can be made from only the letters in “RSTLNE”? Not all of those letters need to be used, and letters can be repeated. Make sure your solution can handle ties.

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

bank = {"R": "R", "S": "S", "T": "T", "L": "L", "N": "N", "E": "E"}
result = [words[0]]

for word in words:
    all_letters_in_bank = True
    for letter in word:
        if letter not in bank:
            all_letters_in_bank = False
            break
    if all_letters_in_bank and len(word) > len(result[0]):
        result = []
        result.append(word)
    if all_letters_in_bank and len(word) == len(result[0]):
        result.append(word)

print(result)
