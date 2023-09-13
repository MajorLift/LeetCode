// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost += [0]
        @cache
        def dp(i):
            if i > n - 2:
                return cost[i]
            return min(dp(i + 1) + cost[i + 1], dp(i + 2) + cost[i + 2])
        return dp(0)