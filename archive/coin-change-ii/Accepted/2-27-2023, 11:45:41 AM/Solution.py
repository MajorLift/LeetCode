// https://leetcode.com/problems/coin-change-ii

class Solution:
    def change(self, total: int, coins: List[int]) -> int:
        memo = [1] + [0 for _ in range(total)]
        for coin in coins:
            for amount in range(coin, total + 1):
                memo[amount] += memo[amount - coin]
        return memo[-1]