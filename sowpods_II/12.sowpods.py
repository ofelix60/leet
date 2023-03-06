# Write a function that takes a string prefix as the first argument, a string suffix as the second argument, and an integer length as the third argument. It should return an array of all of the words that start with that prefix, end with that suffix, and are that length.

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]


def somefunction(prefix, suffix, length):
    result = []

    for word in words:
        if word.startswith(prefix) and word.endswith(suffix) and len(word) == length:
            result.append(word)
    return result


print(somefunction("PLEURO", "SIS", 14))
