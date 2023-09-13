// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        BUY, SELL = 0, 1
        memo = [[0] * (n + 2) for _ in range(2)]
        for i in range(n - 1, -1, -1):
            memo[BUY][i] = max(-prices[i] + memo[SELL][i + 1], memo[BUY][i + 1])
            memo[SELL][i] = max(+prices[i] + memo[BUY][i + 2], memo[SELL][i + 1])
        return memo[BUY][0]