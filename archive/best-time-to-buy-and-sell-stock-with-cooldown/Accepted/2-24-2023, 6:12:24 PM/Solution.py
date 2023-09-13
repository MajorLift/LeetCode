// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold, sold, rest = -math.inf, 0, 0
        for i in range(n):
            hold, sold, rest = max(hold, rest - prices[i]), hold + prices[i], max(rest, sold)
        return max(sold, rest)