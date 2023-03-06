# Write a function that takes a string word as the first argument, a string letter as the second argument, and returns a count of how many times letter occurs in word.

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]


def somefunction(word, letter):
    result = 0
    for current_letter in word:
        if current_letter.upper() == letter.upper():
            result += 1
    return result


print(somefunction("something", "o"))
