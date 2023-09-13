// https://leetcode.com/problems/find-the-difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(ord(e) for e in t) - sum(ord(e) for e in s))