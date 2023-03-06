# What distributor has the most films on this list?

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

distributor_count = {}

for movie in movies:
    # print(movie["Distributor"])
    if movie["Distributor"] not in distributor_count:
        distributor_count[movie["Distributor"]] = 1
    else:
        distributor_count[movie["Distributor"]] += 1

x = distributor_count.items()

to_beat = 0
result = ""

for y in x:
    if y[1] > to_beat:
        to_beat = y[1]
        result = y[0]


print(result)
print(to_beat)
print(distributor_count)
