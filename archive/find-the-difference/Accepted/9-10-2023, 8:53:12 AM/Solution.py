// https://leetcode.com/problems/find-the-difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        n, m = map(len, (s, t))
        difference = 0
        for i in range(m):
            if i < n: difference -= ord(s[i])
            difference += ord(t[i])
        return chr(difference)