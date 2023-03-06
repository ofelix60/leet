class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


solution = Solution()

print(solution.searchInsert([1, 3, 5, 6], 5))
print(solution.searchInsert([1, 3, 5, 6], 2))
print(solution.searchInsert([1, 3, 5, 6], 7))
print(solution.searchInsert([1, 5, 6], 3))