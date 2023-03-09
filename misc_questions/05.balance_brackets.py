# Given a string of different bracket types (parentheses, square brackets, and curly braces), write a function that returns whether or not the string is balanced.

# The string is balanced if each opening bracket is followed by a corresponding close bracket, and all brackets between those open and close brackets are also balanced.

# Examples of balanced strings

# - `{[()]}`
# - `{}[]()`
# - `[(){()}]`

# Examples of unbalanced strings

# - `{[(])}` // Has a `]` before the `(` was closed with a `)`
# - `{}][()` // Has a `]` without a preceding `[`
# - `[(){()}` // Missing a closing `]`

# Example function calls

# - `checkBrackets("{[()]}") → True`
# - `checkBrackets("{}][()") → False`


def checkBrackets(brackets):
    lookup = {"}": "{", "]": "[", ")": "("}
    stack = []

    for bracket in brackets:
        if not len(stack) or bracket not in lookup:
            stack.append(bracket)
        elif bracket in lookup and lookup[bracket] == stack[len(stack) - 1]:
            del stack[len(stack) - 1]

    if len(stack):
        return False
    return True


print(checkBrackets("{[()]}"))
print(checkBrackets("{}[]()"))
print(checkBrackets("[(){()}]"))

print(checkBrackets("{[(])}"))
print(checkBrackets("{}][()"))
print(checkBrackets("[(){()}"))
