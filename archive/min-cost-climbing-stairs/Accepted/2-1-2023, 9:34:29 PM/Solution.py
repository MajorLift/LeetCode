// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
      return min(functools.reduce(
        lambda acc, curr: (min(acc[0], acc[1]) + curr, acc[0]), 
        cost[::-1], 
        (0, 0)))