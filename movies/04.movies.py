# What is the earliest year on this list, and what were the films from that year?

import csv

with open("top_movies.csv", "r", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)  # Read the header row

    movies = []
    for row in reader:
        movie = {}
        for i, value in enumerate(row):
            movie[header[i]] = value
        movies.append(movie)

earliest = 2023
result = ""

for movie in movies:
    if int(movie["Release_Date"]) < earliest:
        earliest = int(movie["Release_Date"])
        result = movie["Title"]

print(result)
