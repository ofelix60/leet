# What are all of the words that can be made from only the letters in “RSTLNE”? Not all of those letters need to be used, and letters can be repeated.

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

bank = {"R": "R", "S": "S", "T": "T", "L": "L", "N": "N", "E": "E"}
result = []

for word in words:
    all_letters_in_bank = True
    for letter in word:
        if letter not in bank:
            all_letters_in_bank = False
            break
    if all_letters_in_bank:
        result.append(word)

print(result)
