class Solution(object):
    def climbStairs(self, n):
        b = 1
        a = b
        while n:
            n -= 1
            b += a
            a = b - a
        return a


solution = Solution()

print(solution.climbStairs(3))
