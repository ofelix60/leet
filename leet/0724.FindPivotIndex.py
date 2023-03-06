from functools import reduce


class Solution(object):
    def pivotIndex(self, nums):
        leftSum = 0
        rightSum = reduce(lambda x, y: x + y, nums)

        for i in range(len(nums)):
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1


solution = Solution()

print(solution.pivotIndex([1, 7, 3, 6, 5, 6]))
