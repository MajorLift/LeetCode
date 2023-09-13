// https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        widths = [1] * n
        for i in range(n):
            l = r = i
            while l >= 0 and heights[l] >= heights[i]:
                l -= 1
            while r < n and heights[r] >= heights[i]:
                r += 1
            l += 1
            r -= 1
            widths[i] = r - l + 1
        return max([widths[i] * heights[i] for i in range(n)])