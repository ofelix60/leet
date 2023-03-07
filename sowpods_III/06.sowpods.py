# Finding alphabet chains:
# - First, what are all of the words that have a least one “A”, one “B”, one “C”, one “D”, one “E”, and one “F” in them, in any order?
# - For example, “FEEDBACK” is an answer to this question
# - Next, is “ABCDEF” the longest alphabet chain that can be found in a word, or is there a longer chain starting somewhere else in the alphabet? Find the longest chain and the words that can be made from that chain.

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]


alphabet = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


result = []

# for word in words:
#     alphabet = ["A", "B", "C", "D", "E", "F"]
#     if len(word) >= 6:
#         for letter in word:
#             if len(alphabet) > 0 and letter in alphabet:
#                 alphabet.remove(letter)
#         if len(alphabet) == 0:
#             result.append(word)

# print(result)


def contains_all_letters(word, letters, cache):
    key = (word, "".join(sorted(letters)))
    if key in cache:
        return cache[key]
    if len(word) < len(letters):
        cache[key] = False
        return False
    for letter in letters:
        if letter not in word:
            cache[key] = False
            return False
    cache[key] = True
    return True


def has_word_using_all_letters(letters, words_array, cache):
    key = ("".join(sorted(letters)), tuple(words_array))
    if key in cache:
        return cache[key]
    for word in words_array:
        if contains_all_letters(word, letters, cache):
            cache[key] = True
            return True
    cache[key] = False
    return False


def get_subarray(array, start_index, length):
    return array[start_index : start_index + length]


def find_longest_letter_chain(alphabet, words):
    cache = {}
    start_index = 0
    length = 1
    longest_chain = None
    while start_index + length <= len(alphabet):
        if not has_word_using_all_letters(get_subarray(alphabet, start_index, length), words, cache):
            start_index += 1
        else:
            longest_chain = get_subarray(alphabet, start_index, length)
            start_index = 0
            length += 1
    return longest_chain


print(find_longest_letter_chain(alphabet, words))
