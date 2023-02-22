class Solution:
    def isIsomorphic(self, s, t):
        # Corner case
        if len(s) != len(t):
            return False
        # Iteration to set the hashmap
        pair_s = {}
        pair_t = {}
        for c1, c2 in zip(s, t):
            # Havent appeared in both map
            if c1 not in pair_s and c2 not in pair_t:
                pair_s[c1] = c2
                pair_t[c2] = c1
            elif pair_s.get(c1) != c2 or pair_t.get(c2) != c1:
                return False
            else:
                pass
        return True


solution = Solution()
print(solution.isIsomorphic("egg", "add"))
