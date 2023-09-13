// https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(i):
            return dp(i - 1) + dp(i - 2) if i > 1 else 1
        return dp(n)
