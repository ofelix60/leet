# Setup

# Most of us learn how to do math with operators in between numbers. For example:

# `(((4 * 3) + 1) - 2) = 11`

# You have an operator like `+ - * /`, and numbers (“operands”) on each side of the operator, and you apply the operator to those operands. If you have multiple expressions, you resolve them according to some order of operations (or forcing the order using parenthesis). This way of doing math uses infix notation — the operators are in between the operands.

# There’s another way of doing math that uses postfix notation — the operators come after the operands. This is a cool way of doing math — you don’t need parenthesis or rules to describe the order of operations, so it’s easier to parse a math expression, and you can use a stack to manage the calculation (using the stack data structure in the real world!).

# Let’s build a basic postfix notation calculator.

# What to implement

# Write a function that takes as an argument a string containing a mathematical expression in postfix notation, using as available operators `+ - * /`. The function should return the result of evaluating that expression.

# Example algorithm

# The postfix notation version of `(((4 * 3) + 1) - 2)` is:

# `1 3 4 * + 2 -`

# Here’s how the stack evolves while evaluating this expression:

# ** see dropbox tables


def postfix(operand):
    stack = []

    for i in range(len(operand)):
        # print(operand)

        if operand[i] in "1234567890":
            stack.append(operand[i])
        else:
            two = stack.pop()
            one = stack.pop()
            expr = one + operand[i] + two
            stack.append(str(int(eval(expr))))

    return stack[0]


print(postfix("134*+2-"))
print(postfix("321++2/"))
