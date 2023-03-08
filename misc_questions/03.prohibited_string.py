# Write a function that takes two arguments, a list of prohibited strings and a username, and returns a boolean of whether or not the username contains any of the prohibited strings.

# Some important details:

# - The list of prohibited words will provide words in some casing, and we want to be case-insensitive in our checks. For example, if “darn” is a prohibited word, “darn”, “DARN” and “DaRn” are all prohibited.
# - Sometimes people like to make usernames that substitute numbers for letters, to try to get around a prohibited word list. We also want to make those substitutions prohibited. The specific letter substitutions we need to check are:
#     - A becomes 4
#     - E becomes 3
#     - I becomes 1
#     - O becomes 0
#     - For example, if “darn” is a prohibited word, “d4rn” is also a prohibited word. If “darn” and “heck” are prohibited words, the username “D4RN_y0u_T0_h3ck” contains prohibited words.


def prohibited_string(prohibited, username):
    substitutions = {
        "4": "a",
        "3": "e",
        "1": "i",
        "0": "o",
    }
    decoded = ""

    for char in username.lower():
        if char in substitutions:
            decoded += substitutions[char]
        else:
            decoded += char

    for word in prohibited:
        if word in decoded:
            return True
    return False


print(prohibited_string(["darn", "heck"], "D4RN_y0u_T0_h3ck"))
