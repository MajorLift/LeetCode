// https://leetcode.com/problems/coin-change-ii

class Solution:
    def change(self, total: int, coins: List[int]) -> int:
        @cache
        def dp(coin_idx, amount):
            if coin_idx == 0: return 0
            if amount == 0: return 1
            return dp(coin_idx - 1, amount) \
                + (dp(coin_idx, amount - coins[coin_idx - 1]) 
                    if coins[coin_idx - 1] <= amount else 0)
        return dp(len(coins), total)