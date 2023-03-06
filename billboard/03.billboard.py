# What artist had the most songs chart in 2000, and what were those songs?

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

        # print(songs)

lookup = {}

to_beat = 0
result = ""

for song in songs:
    if song["artist"] not in lookup:
        lookup[song["artist"]] = [song["song"]]
    elif song["artist"] in lookup and song["song"] not in lookup[song["artist"]]:
        lookup[song["artist"]].append(song["song"])
        if len(lookup[song["artist"]]) > to_beat:
            to_beat = len(lookup[song["artist"]])
            result = song["artist"]

print(f"{result} - {lookup[result]} ")
