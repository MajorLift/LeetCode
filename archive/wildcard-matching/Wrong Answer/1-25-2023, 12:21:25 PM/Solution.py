// https://leetcode.com/problems/wildcard-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        star_idx = s_idx = -1
        while i < len(s):
            if j < len(p) and p[j] in (s[i], "?"):
                i += 1
                j += 1
            elif j < len(p) and p[j] == "*":
                s_idx, star_idx = i, j
                j += 1
            elif j < len(p) and p[j] != s[i] or j == len(p) and star_idx >= 0:
                i, j = s_idx + 1, star_idx + 1
                s_idx = i
            else:
                return False
        return all(e == "*" for e in p[j:])
