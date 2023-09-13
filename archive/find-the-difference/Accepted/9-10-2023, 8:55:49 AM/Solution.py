// https://leetcode.com/problems/find-the-difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(reduce(lambda acc, curr: acc ^ ord(curr), s + t, 0))