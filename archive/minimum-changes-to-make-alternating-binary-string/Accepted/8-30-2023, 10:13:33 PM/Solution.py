// https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string

class Solution:
    def minOperations(self, s: str) -> int:
        diff = sum(e != "01"[i % 2] for i,e in enumerate(s))
        return min(diff, len(s) - diff)