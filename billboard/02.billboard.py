# What song was the #1 song for the most weeks of 2000, who was the artist, and how many weeks was it at #1?

import csv

with open("billboard100_2000.csv", "r", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)  # Read the header row

    songs = []
    for row in reader:
        song = {}
        for i, value in enumerate(row):
            song[header[i]] = value
        songs.append(song)

number_ones = {}

for song in songs:
    if int(song["rank"]) == 1 and f"{song['song']} - {song['artist']}" not in number_ones:
        number_ones[f"{song['song']} - {song['artist']}"] = 1
    elif int(song["rank"]) == 1 and f"{song['song']} - {song['artist']}" in number_ones:
        number_ones[f"{song['song']} - {song['artist']}"] += 1

to_beat = 0
result = ""

for ones in number_ones:
    if number_ones[ones] > to_beat:
        to_beat = number_ones[ones]
        result = f"{ones} - {number_ones[ones]} weeks"

print(result)
