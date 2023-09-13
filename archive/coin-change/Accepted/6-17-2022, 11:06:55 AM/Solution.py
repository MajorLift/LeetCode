// https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') if i > 0 else 0 for i in range(amount + 1)]
        for i in range(1, amount + 1):
            dp[i] = min([dp[i - coin] + 1 \
                         if i - coin >= 0 else float('inf') \
                         for coin in coins])
        return [dp[amount], -1][dp[amount] == float('inf')]