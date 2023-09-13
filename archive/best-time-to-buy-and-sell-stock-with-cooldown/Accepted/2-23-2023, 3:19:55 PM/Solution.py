// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dp(i, doesBuy):
            if i >= n: return 0
            if doesBuy:
                return max(dp(i + 1, not doesBuy) - prices[i], dp(i + 1, doesBuy))
            else:
                return max(dp(i + 2, not doesBuy) + prices[i], dp(i + 1, doesBuy))
        return dp(0, True)