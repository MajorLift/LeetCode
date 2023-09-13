// https://leetcode.com/problems/paint-house

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        @cache
        def dp(idx, color):
            if idx == n:
                return 0
            red, blue, green = costs[idx]
            return min(dp(idx + 1, 0) + min(blue, green), \
                dp(idx + 1, 1) + min(red, green), \
                dp(idx + 1, 2) + min(red, blue))
        return min(dp(0, 0), dp(0, 1), dp(0, 2))