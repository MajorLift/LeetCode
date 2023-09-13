// https://leetcode.com/problems/paint-house

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        return sum(min(cost) for cost in costs)