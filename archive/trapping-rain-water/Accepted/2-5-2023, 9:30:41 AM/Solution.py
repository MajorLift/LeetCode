// https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        max_left, max_right = list(accumulate(height, max)), list(accumulate(height[::-1], max))[::-1]
        return sum([min(max_left[i], max_right[i]) - height[i] for i in range(len(height))])