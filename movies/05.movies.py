# What is the distribution of ratings? (How many are PG, PG-13, R, etc.?)

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

count_by_rating = {}

for movie in movies:
    if movie["Rating"] not in count_by_rating:
        count_by_rating[movie["Rating"]] = 1
    else:
        count_by_rating[movie["Rating"]] += 1


print(count_by_rating)
