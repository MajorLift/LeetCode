// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = [0] * (n + 2)
        for buy in range(n - 2, -1, -1):
            memo[buy] = max(memo[buy + 1], 
                max(prices[sell] - prices[buy] + memo[sell + 2] 
                    for sell in range(buy + 1, n)))
        return memo[0]