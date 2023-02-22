class Solution(object):
    def lengthOfLastWord(self, s):
        x = s.split()
        return len(x[len(x) - 1])


solution = Solution()

print(solution.lengthOfLastWord("Hello World"))
