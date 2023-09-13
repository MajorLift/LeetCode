// https://leetcode.com/problems/coin-change-ii

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [([1] + [0] * amount) for _ in range(len(coins))]
        for i, coin in enumerate(coins):
            for x in range(1, amount + 1):
                memo[i][x] += memo[i - 1][x] + (memo[i][x - coin] if x >= coin else 0)
        return memo[-1][-1]