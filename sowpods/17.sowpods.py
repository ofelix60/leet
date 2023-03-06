# What are all of the letters that never appear consecutively in an English word? For example, we know that “U” isn’t an answer, because of the word VACUUM, and we know that “A” isn’t an answer, because of “AARDVARK”, but which letters never appear consecutively?

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

lookup = {
    "AA": 0,
    "BB": 0,
    "CC": 0,
    "DD": 0,
    "EE": 0,
    "FF": 0,
    "GG": 0,
    "HH": 0,
    "II": 0,
    "JJ": 0,
    "KK": 0,
    "LL": 0,
    "MM": 0,
    "NN": 0,
    "OO": 0,
    "PP": 0,
    "QQ": 0,
    "RR": 0,
    "SS": 0,
    "TT": 0,
    "UU": 0,
    "VV": 0,
    "WW": 0,
    "XX": 0,
    "YY": 0,
    "ZZ": 0,
}
result = []

for word in words:
    for i in range(len(word) - 1):
        if word[i] + word[i + 1] in lookup:
            lookup[word[i] + word[i + 1]] += 1

for key in lookup:
    if lookup[key] == 0:
        result.append(key)

print(result)
# print(lookup)


################################


# consecutive_pairs = set()
# for word in words:
#     for i in range(len(word) - 1):
#         if word[i] == word[i + 1]:  # only consider consecutive double letters
#             consecutive_pairs.add(word[i : i + 2])
#             print(consecutive_pairs)

# non_consecutive_pairs = sorted(set([chr(i) * 2 for i in range(ord("A"), ord("Z") + 1)]) - consecutive_pairs)

# print(non_consecutive_pairs)
