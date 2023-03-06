# Write a function that takes a string prefix as an argument and returns an array of all of the words that start with that prefix (the prefix has to be at the beginning of the word).

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]


def somefuntion(substring):
    result = []
    for word in words:
        if word.startswith(substring):
            result.append(word)
    return result


print(somefuntion("PLEURO"))
