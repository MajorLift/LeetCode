// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dp(idx):
            if idx <= 2:
                return cost[idx - 1]
            return cost[idx] + min(dp(idx - 1), dp(idx - 2))
        return dp(len(cost) - 1)