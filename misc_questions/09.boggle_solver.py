# Part 1
# Implement a recursive depth-first search that you fully understand and could reproduce in front of someone from scratch if you needed to.

# Then, run your DFS implementation on some example graphs. This means being comfortable with how to represent a graph with nodes and edges in your preferred interview language.

# This will become the foundation for the Boggle solver.


# Part 2
# Review how to play Boggle. Here is an example online version.

# The goal of the game when played with humans is to find as many words as you can in a grid of 16 letters, in a limited amount of time. Words can only be made from connected letters — i.e. from a given letter you can only use the letters directly adjacent, including diagonally. You can’t reuse letters, and words must be at least 3 letters long.


# Part 3

# Implement a Boggle solver. This is the part that you can treat like a time-boxed interview if you’d like. You will likely want to break this into the follow steps:


# 1. Stub out a function that takes as input a grid (e.g. a 2 x 2 or 4 x 4 matrix of letters) and returns all of the words that can be made from that grid.
# 2. Write a function to create a graph from the grid. [Goal: complete this sub-part in 30 minutes]
#     1. Refer back to your graph representations from Part I.
#     2. Test that you get the correct graph back from a grid.
# 3. Set up a data structure containing all words in the dictionary, with efficient lookup. [Goal: complete this sub-part in < 10 minutes (you probably already have this implemented if you’ve completed the prior problems in this problem set)]
# 4. Use depth-first search to find all of the words in the grid. [Goal: complete this sub-part in 60 minutes]
#     1. You’ll need to run DFS starting from every letter.
#     2. You don’t need any fancy data structures to solve a 4x4 grid quickly.
#     3. You’ll need a way of confirming if a path through the grid makes a valid word.
#     4. You might find it helpful (both as a light efficiency optimization and for easier debugging) to stop pursuing paths in the grid that cannot possibly lead to a valid word, i.e. that path is not a valid prefix for any word in the dictionary.


# Example inputs and outputs

# Example 1
# Grid:

#     BE
#     TQ

# Valid words: {'BET'}

# Example 2
# Grid:

#     ZQQZ
#     ZAEZ
#     ZUDZ
#     ZQQZ

# Valid words: {'ZUZ', 'ZED', 'ADZ', 'QUAD', 'EAU', 'DAE', 'DUE', 'ZEA', 'QUA', 'ADZE', 'AUE', 'ZZZ'}

# Example 3
# Grid:

#     MSEF
#     RATD
#     LONE
#     KAFB

# Valid words: {'FONDEST', 'TOR', 'RANTED', 'OAF', 'FETES’ … 486 words in all}

# x = [["B", "E"], ["T", "Q"]]

x = [
    ["Z", "Q", "Q", "Z"],
    ["Z", "A", "E", "Z"],
    ["Z", "U", "D", "Z"],
    ["Z", "Q", "Q", "Z"],
]


# Create an empty dictionary to represent the graph
graph = {}

# Loop through the rows and columns in x and add the nodes and edges to the graph dictionary
for i in range(len(x)):
    for j in range(len(x[0])):
        node = x[i][j]
        if node not in graph:
            graph[node] = []
        if i > 0:
            graph[node].append(x[i - 1][j])
        if j > 0:
            graph[node].append(x[i][j - 1])
        if i < len(x) - 1:
            graph[node].append(x[i + 1][j])
        if j < len(x[0]) - 1:
            graph[node].append(x[i][j + 1])

# Remove duplicate adjacent nodes from each node's adjacency list
for node in graph:
    graph[node] = list(set(graph[node]))

# Print the graph
print(graph)

valid_words = []
result = []


def dfs(start, visited=set()):
    print(start)
    visited.add(start)
    print(visited)

    words = graph[start]
    print(words)

    for word in words:
        if word in valid_words:
            print("found a word")
            result.append(word)
            return

        if word not in valid_words:
            dfs(word, visited)


{
    "Z": ["Q", "E", "Z", "A", "D", "U"],
    "Q": ["Q", "E", "Z", "A", "D", "U"],
    "A": ["Z", "Q", "U", "E"],
    "E": ["Z", "Q", "A", "D"],
    "U": ["Z", "Q", "A", "D"],
    "D": ["Z", "U", "E", "Q"],
}
