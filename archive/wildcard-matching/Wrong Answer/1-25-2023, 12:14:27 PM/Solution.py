// https://leetcode.com/problems/wildcard-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        star_idx = -1
        while i < len(s):
            if j < len(p) and p[j] in (s[i], "?"):
                i += 1
                j += 1
            elif j < len(p) and p[j] == "*":
                star_idx = j
                j += 1
            elif j == len(p) and star_idx == -1:
                return False
            elif j < len(p) and p[j] != s[i] or j == len(p) and star_idx >= 0:
                i += 1
                j = star_idx + 1
        return all(e == "*" for e in p[j:])
