# Part 1

# Write code that:

# - Accepts a string (e.g. as an argument to a function, or as a command-line argument). This string represents your Scrabble “rack”.
# - Prints out the words that can be made from the characters in that input string, along with their Scrabble scores, one word per line, in descending score order

# Example input and output:

# `$ python scrabble_cheater.py SPCQEIU  # Use any language you like.`
# `17 piques`
# `17 equips`
# `16 quips`
# `16 pique`
# `16 equip`
# `15 quip`
# `…`

# Key points:

# - Letters cannot be reused. For example, if your Scrabble rack is “ABCD”, you can make the word “CAB” but not the word “DAD”, because you only have one “D”.
# -
# Part 2

# Extend the script to handle blank tiles. When reading the input, the character _ can be used as a wildcard — it can represent any letter.

# Wildcards do not count towards a word's score.

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]


scores = {
    "A": 1,
    "B": 3,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 2,
    "H": 4,
    "I": 1,
    "J": 8,
    "K": 5,
    "L": 1,
    "M": 3,
    "N": 1,
    "O": 1,
    "P": 3,
    "Q": 10,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "V": 4,
    "W": 4,
    "X": 8,
    "Y": 4,
    "Z": 10,
}


def scrabble_solver(str):
    result = []
    bank = [*str.upper()]

    for word in words:
        score = 0
        word_bank = [*word]
        for letter in bank:
            if letter in word_bank:
                word_bank.remove(letter)
                score += scores[letter]

        if not word_bank:
            result.append([score, word])
    print(sorted(result))


print(scrabble_solver("UULEZMJTV"))
