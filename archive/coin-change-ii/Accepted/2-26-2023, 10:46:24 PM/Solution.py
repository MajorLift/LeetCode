// https://leetcode.com/problems/coin-change-ii

class Solution:
    def change(self, total: int, coins: List[int]) -> int:
        memo = [[1 if amount == 0 else 0 for idx in range(len(coins))] \
            for amount in range(total + 1)]
        for amount in range(total + 1):
            for idx in range(len(coins)):
                memo[amount][idx] = memo[amount][idx - 1] \
                    + (memo[amount - coins[idx - 1]][idx] 
                        if coins[idx - 1] <= amount else 0)
        return memo[-1][-1]
