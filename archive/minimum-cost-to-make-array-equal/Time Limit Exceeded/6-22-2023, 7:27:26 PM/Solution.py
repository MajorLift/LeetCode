// https://leetcode.com/problems/minimum-cost-to-make-array-equal

class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        pairs = [(num, cost) for num, cost in zip(nums, costs)]
        pairs.sort(key=lambda x: x[0])
        global_min = +inf
        for i, (base, _) in enumerate(pairs):
            total_cost = 0
            for num, cost in pairs[:i] + pairs[i+1:]:
                total_cost += abs(base - num) * cost
            global_min = min(global_min, total_cost)
        return global_min