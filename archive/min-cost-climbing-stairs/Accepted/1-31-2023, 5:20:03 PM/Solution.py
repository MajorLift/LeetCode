// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost += [0]
        acc, prev = cost[1], cost[0]
        for i in range(2, n + 1):
            acc, prev = cost[i] + min(acc, prev), acc
        return acc