// https://leetcode.com/problems/coin-change-ii

class Solution:
    def change(self, total: int, coins: List[int]) -> int:
        @cache
        def dp(amount, idx):
            if amount < 0 or idx <= 0: return 0
            if amount == 0: return 1
            return dp(amount, idx - 1) + dp(amount - coins[idx - 1], idx)
        return dp(total, len(coins))