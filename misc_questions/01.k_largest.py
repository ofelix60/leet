# Write a function that takes as input two arguments:

# 1. An array of numbers
# 2. An integer `k`

# and returns the `k` largest values from that array. The order of the elements in the returned array doesn’t matter.

# Example

# - Input array: `[5, 16, 7, 9, -1, 4, 3, 11, 2]`
# - `k`: 3
# - Result: `[16, 9, 11]`


def k_largest(k, arr):
    if k > len(arr):
        return "value of 'k' is too big. Please pick a different number."
    sorted_arr = sorted(arr)

    return sorted_arr[len(sorted_arr) - k :]


print(k_largest(4, [5, 16, 7, 9, -1, 4, 3, 11, 2]))
print(k_largest(7, [5, 16, 7, 9, -1, 4, 3, 11, 2]))
