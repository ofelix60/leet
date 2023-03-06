# Write a function that takes a string word as an argument and returns a count of all of the “A”s in that string.

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]


def somefunction(string):
    count = 0
    for letter in string:
        if letter == "A":
            count += 1
    return count


print(somefunction("TARAMASALATA"))
