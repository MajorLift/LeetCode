// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        BUY = True
        @cache
        def dp(i, transaction):
            if i >= n: return 0
            if transaction == BUY:
                return max(-prices[i] + dp(i + 1, not BUY), dp(i + 1, BUY))
            else:
                return max(+prices[i] + dp(i + 2, BUY), dp(i + 1, not BUY))
        return dp(0, BUY)