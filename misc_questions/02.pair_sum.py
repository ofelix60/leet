# Write a function that takes as input two arguments:

# 1. An array of numbers
# 2. An integer `k`

# and returns an array with all of the pairs of numbers from that array that sum to `k`. You can’t use the same number twice. You can assume that there are no duplicate numbers in the array.

# Example

# - Input array: `[1, 9, 6, 3, 5, 4]`
# - `k`: 10
# - Result: `[[1, 9], [6, 4]]` // Note that `[5, 5]` is not in the solution


def pair_sum(k, arr):
    result = []
    used_index = []

    for i in range(len(arr) - 1):
        for j in range(len(arr)):
            print(arr[i], arr[j])
            if arr[i] + arr[j] == k and i not in used_index and j not in used_index and i != j:
                result.append([arr[i], arr[j]])
                used_index.append(i)
                used_index.append(j)
                print(arr)

    return result


print(pair_sum(10, [1, 9, 6, 3, 5, 4]))
