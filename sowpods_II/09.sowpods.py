# What is the longest word that can be made without the letters in “AEIOSHRTN” (in other words, without the most common letters)? Make sure your solution can handle ties.

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

bank = {"A": "A", "E": "E", "I": "I", "O": "O", "S": "S", "H": "H", "R": "R", "T": "T", "N": "N"}
result = [words[0]]

# for word in words:
#     all_letters_in_bank = True
#     for letter in word:
#         if letter not in bank:
#             all_letters_in_bank = False
#             break
#     if all_letters_in_bank and len(word) > len(result[0]):
#         result = []
#         result.append(word)
#     if all_letters_in_bank and len(word) == len(result[0]):
#         result.append(word)


for word in words:
    x = True
    for letter in word:
        if letter in bank:
            x = False
            break
    if x and len(word) > len(result[0]):
        result = []
        result.append(word)
    if x and len(word) == len(result[0]):
        result.append(word)

print(result)
