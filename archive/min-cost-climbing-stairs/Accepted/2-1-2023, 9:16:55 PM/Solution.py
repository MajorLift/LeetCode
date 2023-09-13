// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        acc = prev = 0
        for i in range(len(cost)):
            acc, prev = cost[i] + min(acc, prev), acc
        return min(acc, prev)