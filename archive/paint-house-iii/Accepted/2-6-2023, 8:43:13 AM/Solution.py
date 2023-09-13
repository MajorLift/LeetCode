// https://leetcode.com/problems/paint-house-iii

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @cache
        def dp(idx = 0, cnt = 0, prev_color = 0):
            if idx == m and cnt == target:
                return 0
            if (idx == m and cnt < target) or cnt > target:
                return +math.inf
            if houses[idx] != 0:
                return dp(idx + 1, cnt + 1 if houses[idx] != prev_color else cnt, houses[idx])
            return min(cost[idx][color - 1] + dp(idx + 1, cnt + 1 if color != prev_color else cnt, color) for color in range(1, n + 1))
        
        min_cost = dp()
        return min_cost if min_cost < +math.inf else -1