// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sup = min(bisect_right(nums, target - (nums[0] if nums[0] < 0 else 0)), len(nums) - 1)
        for right in range(sup, 0, -1):
            left = bisect_right(nums[:right], target - nums[right]) - 1
            if nums[left] + nums[right] == target:
                return [left + 1, right + 1]