# What are all of the compound words? These are words made up of 2 smaller words. For example, “SNOWMAN” is a compound word made from “SNOW” and “MAN”, and “BEACHBALL” is a compound word made from “BEACH” and “BALL”.

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]


yo = {*words}
result = []

for word in words:
    i = 0
    acc = ""
    while i <= len(word) - 1:
        acc += word[i]
        if len(acc) >= 3 and acc in yo and word[i + 1 : len(word)] in yo:
            print(acc, "+", word[i + 1 : len(word)])
            print("!!!!:", word)
            result.append(word)
        i += 1


print(result)
print(len(result))
