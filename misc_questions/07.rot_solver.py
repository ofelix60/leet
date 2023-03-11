# Part I

# (If you’ve heard of a rot13 letter substitution cipher, this question is a generalization of that cipher)

# Write a function `rot` that:

# - takes as arguments: an input string and an amount by which to shift the letters in the string
# - returns: the input string, shifted by the shift amount

# The function should preserve case — it should be able to handle both upper and lowercase letters — and it should not alter punctuation. The function should support negative numbers. The function should support large shift numbers.


# Sample inputs and outputs:

# rot("HELLO", 1) -> "IFMMP" # shift right by 1
# rot("HELLO", 2) -> "JGNNQ" # shift right by 2
# rot("HELLO", -1) -> "GDKKN" # shift left by 1
# rot("HELLO", 27) -> "IFMMP" # shift right by 27, wrapping back to the beginning
# rot("Hello, Rick", 1) -> "Ifmmp, Sjdl" # Preserve case and punctuation
# rot(rot("Hello, Rick", 1), -1) -> "Hello, Rick"


# Part II

# Using your `rot` function, write a function `decrypt` that takes a text encrypted using a shift substitution cipher of an unknown shift amount, and returns a tuple containing `(the shift used to encrypt the original string, the original string)`.

# You will need a dictionary or word list. An input string needs to be long enough to unambiguously determine the the shift used, or there could be multiple valid shifts.

# decrypt("Ju xbt uif cftu pg ujnft, ju xbt uif xpstu pg ujnft") -> ("It was the best of times, it was the worst of times", 1)


# upper 65 - 90
# lower 97 - 122

with open("sowpods.txt", "r") as f:
    words = [line.rstrip() for line in f]


def rot(str, shift):
    encoded = ""
    for char in str:
        if ord(char) >= 65 and ord(char) <= 90:
            encoded += chr(((ord(char) + shift - 65) % 26) + 65)
        elif ord(char) >= 97 and ord(char) <= 122:
            encoded += chr(((ord(char) + shift - 97) % 26) + 97)
        else:
            encoded += char

    return encoded


# print(rot("abc", 1))
# print(rot("ThIs, Is A tEsT!", 1))
# print(rot(rot("Hello, Rick", 1), -1))

# print("FORMAT" in words)
# print("theasdf" in words)

# for word in split_str:
#     for i in range(1, 26):
#         this_word = rot(word, i).upper()
#         print(this_word, i)
#         if this_word in words:


# return 26 - i

print(
    rot(
        "NyQuil tm. Severe cold & flu. Headache, fever, sore throat, minor aches & pains. Sneezing, Runny Nose, Cough.",
        7,
    )
)


def decrypt(str):
    result = []
    split_str = str.split()
    for i in range(1, 26):
        shifted_words = []
        for word in split_str:
            shifted_words.append(rot(word, i))
        valid_words = 0
        for s_word in shifted_words:
            if s_word.upper() in words:
                valid_words += 1
        if valid_words >= round((len(shifted_words) - 1) * 0.5):
            result = [" ".join(shifted_words), 26 - i]
    return tuple(result)


# print(decrypt("Ju xbt uif cftu pg ujnft, ju xbt uif xpstu pg ujnft"))
print(
    decrypt(
        rot(
            "Severe cold  flu Headache fever sore throat minor aches  pains Sneezing Runny Nose Cough",
            7,
        )
    )
)
