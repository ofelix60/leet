# Which of the letters Q, X, and Z is the least common?

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

lookup = {"Q": 0, "X": 0, "Z": 0}

for word in words:
    for letter in word:
        if letter == "Q":
            lookup["Q"] += 1
        if letter == "X":
            lookup["X"] += 1
        if letter == "Z":
            lookup["Z"] += 1

print(min(lookup.values()))
