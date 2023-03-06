# Write a function that takes a string substring as an argument and returns an array of all of the words that contain that substring (the substring can appear anywhere in the word).

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]


def somefunction(substring):
    result = []
    for word in words:
        if substring in word:
            result.append(word)
    return result


print(somefunction("LESSNESSES"))
