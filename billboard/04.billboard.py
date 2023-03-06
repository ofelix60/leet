# What song(s) were on the charts (anywhere on the charts) for the most weeks of 2000?

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

lookup = {}

to_beat = 0
result = ""

for song in songs:
    if song["song"] not in lookup:
        lookup[song["song"]] = 1
    else:
        lookup[song["song"]] += 1
        if lookup[song["song"]] > to_beat:
            to_beat = lookup[song["song"]]
            result = song["song"]


print(result)
print(to_beat)
