#  What movies on this list were distributed by DreamWorks?

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

for movie in movies:
    if movie["Distributor"] == "DreamWorks":
        print(movie)
