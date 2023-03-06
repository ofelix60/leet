# There is at least one country name that contains another country name. Find all of these cases.

with open("countries.txt", "r") as f:
    countries = [line.rstrip() for line in f]

# countries = [
#     "Afghanistan",
#     "Albania",
#     "Algeria",
#     "Andorra",
#     "Angola",
# ]

results = []

for i in range(len(countries) - 1):
    for j in range(i + 1, len(countries)):
        if countries[i] in countries[j] or countries[j] in countries[i]:
            results.append([countries[i], countries[j]])

print(results)
