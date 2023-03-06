# class Solution(object):
#     def runningSum(self, nums):
#         result = []

#         for i in range(len(nums)):
#             temp = 0
#             for j in range(i, -1, -1):
#                 temp += nums[j]
#             result.append(temp)
#         return result


# solution = Solution()

# print(solution.runningSum([3, 1, 2, 10, 1]))


class Solution(object):
    def runningSum(self, nums):
        result = 0

        for i in range(len(nums)):
            result = result + nums[i]
            nums[i] = result
        return nums


solution = Solution()

print(solution.runningSum([3, 1, 2, 10, 1]))
