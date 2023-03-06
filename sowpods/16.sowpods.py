# What is the longest palindrome?

import math

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]


result = ""

for word in words:
    x = word[0 : math.ceil(len(word) / 2)]
    y = word[math.floor(len(word) / 2) : len(word)][::-1]
    if x == y and len(result) < len(word):
        result = word


print(result)
