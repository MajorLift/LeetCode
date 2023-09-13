// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost += [0]
        @cache
        def dp(idx):
            return cost[idx] + (min(dp(idx - 1), dp(idx - 2)) if idx > 1 else 0)
        return dp(n)