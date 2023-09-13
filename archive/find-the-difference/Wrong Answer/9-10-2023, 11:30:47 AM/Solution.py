// https://leetcode.com/problems/find-the-difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = map(lambda x: ''.join(sorted(x)), (s, t))
        i = j = -1
        while i < len(s) - 1 and s[i := i + 1] == t[j := j + 1]: pass
        return t[j + 1]