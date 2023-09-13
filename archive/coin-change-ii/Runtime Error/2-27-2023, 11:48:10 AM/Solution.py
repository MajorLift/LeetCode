// https://leetcode.com/problems/coin-change-ii

class Solution:
    def change(self, total: int, coins: List[int]) -> int:
        memo = [([1] + [0] * total) for idx in range(len(coins))]
        for idx in range(len(coins)):
            for amount in range(1, total + 1):
                memo[idx][amount] = memo[idx - 1][amount] \
                    + (memo[idx][amount - coins[idx - 1]] or 0)
        return memo[-1][-1]