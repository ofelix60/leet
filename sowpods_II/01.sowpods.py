# What are all of the words that both start with a “TH” and end with a “TH”?

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]

result = []

for word in words:
    if word.startswith("TH") and word.endswith("TH"):
        result.append(word)

print(result)
