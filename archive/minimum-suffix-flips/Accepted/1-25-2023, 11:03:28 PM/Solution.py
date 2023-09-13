// https://leetcode.com/problems/minimum-suffix-flips

class Solution:
    def minFlips(self, target: str) -> int:
        n = len(target)
        suffix = 0
        ans = 0
        for i in range(n):
            if int(target[i]) != suffix:
                suffix = 1 - suffix
                ans += 1
        return ans