// https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [0.0] + [+math.inf for _ in range(amount)]
        for i in range(1, amount + 1):
            for coin in coins:
                memo[i] = min(memo[i], memo[i - coin] + 1)
        return -1 if memo[amount] == +math.inf else int(memo[amount])