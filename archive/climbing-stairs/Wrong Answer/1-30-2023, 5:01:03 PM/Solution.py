// https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(i):
            if i == 1:
                return 0
            if i == 2:
                return 2
            if i == 3:
                return 3
            return dp(i - 1) + 2 * dp(i - 2)
        return dp(n)
