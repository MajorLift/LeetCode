// https://leetcode.com/problems/minimum-suffix-flips

class Solution:
    def minFlips(self, target: str) -> int:
        n = len(target)
        suffix = "0"
        ans = 0
        for i in range(n):
            if target[i] != suffix:
                suffix = str(1 - int(suffix))
                ans += 1
        return ans