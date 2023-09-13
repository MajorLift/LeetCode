// https://leetcode.com/problems/minimum-suffix-flips

class Solution:
    def minFlips(self, target: str) -> int:
        n = len(target)
        suffix = "0"
        ans = 0
        for bit in target:
            if bit != suffix:
                suffix = bit
                ans += 1
        return ans