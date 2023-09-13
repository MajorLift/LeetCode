// https://leetcode.com/problems/paint-house-ii

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        @cache
        def dp(i, color):
            if i == n:
                return 0
            return costs[i][color] + min(dp(i + 1, j % k) for j in range(color + 1, color + k))
        return min(dp(0, j) for j in range(k))