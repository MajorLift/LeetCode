// https://leetcode.com/problems/largest-perimeter-triangle

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        max_perimeter = 0
        for a, b, c in combinations(nums, 3):
            if a + b > c:
                max_perimeter = max(max_perimeter, a + b + c)
        return max_perimeter