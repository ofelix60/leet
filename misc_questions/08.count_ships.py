# Write a function that counts of the number of ships in a 2D grid.

# - Input: an array of arrays of strings, representing a 2D grid. The strings are either a `"."` for open water, or an `"S"` for part of a ship. Connected `"S"`es are part of the same ship.
# - Output: an integer that is the count of the number of ships in the grid.

# Facts about ships:

# - Ships are only horizontal or vertical, not diagonal.
# - Ships have a width of one or more and a height of one or more.
# - Ships never touch each other.

# The input will always be a well-formed grid (all rows are the same length).


ships2 = [
    ["S", "S", ".", "S", "S", "S", ".", "."],
    ["S", "S", ".", "S", "S", "S", ".", "."],
    ["S", "S", ".", ".", ".", ".", "S", "S"],
]
# countShips(ships) -> 3

ships = [[".", "S", ".", "S"], [".", ".", ".", "S"], ["S", "S", ".", "S"], [".", ".", ".", "S"]]


def countShips(ships):
    count = 0

    for i in range(len(ships)):
        for j in range(len(ships[i])):
            if ships[i][j] == "S":
                if ((i == 0 or ships[i - 1][j] != "S") and (j == 0 or ships[i][j - 1] != "S")) or (
                    (i == 0 or ships[i - 1][j] != "S") and (ships[i][j - 1] != "S")
                ):
                    count += 1

    return count


print(countShips(ships))
print(countShips(ships))

# print(ships[4][4])
