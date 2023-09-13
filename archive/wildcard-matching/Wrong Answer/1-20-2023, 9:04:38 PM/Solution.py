// https://leetcode.com/problems/wildcard-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        while j < len(p):
            if i == len(s):
                return True
            if p[j] == "?":
                i += 1
                j += 1
            elif p[j] == "*":
                if j < len(p) - 1:
                    while s[i] != p[j + 1]:
                        i += 1
                    j += 1
                else:
                    return True
            else:
                if s[i] != p[j]:
                    break
                i += 1
                j += 1
        return False