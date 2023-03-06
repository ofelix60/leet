# Finding alphabet chains:
# - First, what are all of the words that have a least one “A”, one “B”, one “C”, one “D”, one “E”, and one “F” in them, in any order?
# - For example, “FEEDBACK” is an answer to this question
# - Next, is “ABCDEF” the longest alphabet chain that can be found in a word, or is there a longer chain starting somewhere else in the alphabet? Find the longest chain and the words that can be made from that chain.

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

pattern = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


result = []

# for word in words:
#     pattern = ["A", "B", "C", "D", "E", "F"]
#     if len(word) >= 6:
#         for letter in word:
#             if len(pattern) > 0 and letter in pattern:
#                 pattern.remove(letter)
#         if len(pattern) == 0:
#             result.append(word)

# print(result)


result2 = []
pattern2 = pattern

# print("letter:", pattern[(len(pattern) - 1) - i])
# print("number:", len(pattern) - i)
# print()

for i in range(len(pattern) - 1):
    # print(pattern[i])
    for word in words:
        x = False
        if len(word) >= len(pattern):
            for letter in word:
                if letter not in pattern:
                    break
        print(len(pattern))
        x = True
        if x == True:
            # result = pattern
            print("here:", pattern)
        else:
            pattern.pop(len(pattern) - 1)

# loop through alphabet
# loop through words
#   if no: word contains all letters remove last letter from pattern
#   if yes: result IS pattern and return pattern

# for i in range(len(pattern) - 1):
#     print(pattern)
#     pattern.pop(len(pattern) - 1)
#     print(pattern)
#     print()

# print(result2)
