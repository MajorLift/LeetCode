// https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = -math.inf
        while l < r:
            width = r - l
            if height[l] <= height[r]:
                maxArea = max(maxArea, height[l] * width)
                l += 1
            else:
                maxArea = max(maxArea, height[r] * width)
                r -= 1
        return maxArea