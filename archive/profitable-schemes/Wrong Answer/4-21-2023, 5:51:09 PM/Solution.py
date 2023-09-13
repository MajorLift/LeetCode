// https://leetcode.com/problems/profitable-schemes

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        @cache
        def dp(i, spoils, idle):
            if idle <= 0 or i == len(profit):
                return int(spoils >= minProfit)
            take = dp(i + 1, spoils + profit[i], idle - group[i])
            leave = dp(i + 1, spoils, idle)
            return take + leave
        return dp(0, 0, n) % (10 ** 9 + 7)