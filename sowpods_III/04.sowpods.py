# Write a function that takes a string availableLetters as an argument and returns an array of all of the words that can be made from only those letters. Letters can be re-used as many times as needed and can appear in any order. Not all of the letters in availableLetters have to be used.

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]


def somefunction(available_letters):
    result = []
    bank = [*available_letters]

    for word in words:
        condition = True
        for letter in word:
            if letter not in bank:
                condition = False
                break
        if condition == True:
            result.append(word)

    return result


print(somefunction("QWERTY"))
