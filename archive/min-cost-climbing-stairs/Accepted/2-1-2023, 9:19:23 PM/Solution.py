// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost += [0]
        @cache
        def dp(i):
            if i <= 1:
                return cost[i]
            return cost[i] + min(dp(i - 1), dp(i - 2))
        return dp(len(cost) - 1)