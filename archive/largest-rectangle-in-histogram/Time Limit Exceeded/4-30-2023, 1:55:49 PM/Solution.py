// https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        @cache
        def dp(l, r):
            if l > r:
                return 0
            min_idx = l
            for i in range(l, r + 1):
                if heights[i] < heights[min_idx]:
                    min_idx = i
            return max(
                heights[min_idx] * (r - l + 1),
                dp(l, min_idx - 1),
                dp(min_idx + 1, r))
        return dp(0, len(heights) - 1)