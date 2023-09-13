// https://leetcode.com/problems/find-the-difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = map(lambda x: sorted(list(x)), (s, t))
        i = j = 0
        while i < len(s) and j < len(t) and s[i] == t[j]:
            i += 1
            j += 1
        return t[j]