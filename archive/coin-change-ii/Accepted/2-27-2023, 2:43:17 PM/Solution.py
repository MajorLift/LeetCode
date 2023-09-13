// https://leetcode.com/problems/coin-change-ii

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [1] + [0] * amount
        for coin in coins:
            for x in range(coin, amount + 1):
                memo[x] += memo[x - coin]
        return memo[-1]