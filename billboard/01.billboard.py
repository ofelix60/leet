# Print out all of the #1 songs and the artists who made them. If a song was #1 for more than one week, only print it once. Example output:
#     These were the number one songs of 2000:
#     "Try Again" - Aaliyah
#     "Say My Name" - Destiny's Child
#     "What A Girl Wants" - Christina Aguilera
#     "Maria Maria" - Santana Featuring The Product G&B
#     "Smooth" - Santana Featuring Rob Thomas
#     "Independent Women Part I" - Destiny's Child

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

number_ones = []

for song in songs:
    if int(song["rank"]) == 1 and f"{song['song']} - {song['artist']}" not in number_ones:
        number_ones.append(f"{song['song']} - {song['artist']}")

print(number_ones)
