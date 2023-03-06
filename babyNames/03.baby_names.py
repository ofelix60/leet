# There is at least one baby name from the top 40 baby names for 2020 that, when spelled backwards, is a valid Scrabble word. Find and print all such names.

# - Solve this two ways: first with an array to hold the Scrabble words, and then with a dictionary (or set) to hold the Scrabble words. Use timer functions to measure how long it takes to complete this work under each implementation. Why is the time different?

import time

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]
    words_dict = dict.fromkeys(words, None)

with open("baby_names_2020_short.txt", "r") as f:
    names = [line.rstrip() for line in f]

result = []
result2 = []

start_time = time.time()

for name in names:
    for word in words:
        if name[::-1].upper() == word:
            result.append(name)

end_time = time.time()
elapsed_time = end_time - start_time

print(result)
print(f"Elapsed time: {elapsed_time} seconds")


start_time_two = time.time()

for name in names:
    if name[::-1].upper() in words_dict:
        result2.append(name)

end_time_two = time.time()
elapsed_time_two = end_time_two - start_time_two

print(result2)
print(f"Elapsed time: {elapsed_time_two} seconds")

print("HERE:", min(elapsed_time, elapsed_time_two))
