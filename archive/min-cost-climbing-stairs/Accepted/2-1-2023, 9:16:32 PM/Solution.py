// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        acc, prev = 0, 0
        for i in range(n):
            acc, prev = cost[i] + min(acc, prev), acc
        return min(acc, prev)