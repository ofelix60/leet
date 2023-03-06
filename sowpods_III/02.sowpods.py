# What are all of the words that are at least 8 letters long and use 3 or fewer different letters? For example, “REFERRER” is an answer to this question, because it uses only 3 different letters: R, E, and F.

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

result = []


for word in words:
    if len(word) >= 8:
        lookup = {}
        under_three = True

        for letter in word:
            if len(lookup) <= 3 and letter in lookup:
                lookup[letter] += 1
            elif len(lookup) <= 3 and letter not in lookup:
                lookup[letter] = 1
            else:
                under_three = False
                break

        if under_three == True:
            result.append(word)

print(result)
