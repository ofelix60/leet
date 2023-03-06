# What is the highest grossing movie from Universal Pictures, domestically?

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

gross = 0
result = ""
for movie in movies:
    if movie["Distributor"] == "Universal Pictures" and int(movie["US_Sales"]) > gross:
        gross = int(movie["US_Sales"])
        result = movie["Title"]


print(result)
