// https://leetcode.com/problems/coin-change-ii

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(x, i):
            if x == 0: return 1
            if x < 0 or i <= 0: return 0
            return dp(x, i - 1) + dp(x - coins[i - 1], i)
        return dp(amount, len(coins))