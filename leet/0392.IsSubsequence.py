import re

# pattern = r"[aeiouAEIOU]"
# vowelsLength = len(re.findall(pattern, country))


class Solution(object):
    def isSubsequence(self, s, t):
        pattern = rf"{s}"
        # print(pattern)
        targetString = re.findall(pattern, t)
        print(pattern, t)


solution = Solution()

solution.isSubsequence("abc", "ahbgdc")
