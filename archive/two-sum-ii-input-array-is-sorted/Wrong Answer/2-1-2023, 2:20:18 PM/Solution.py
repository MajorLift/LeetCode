// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sup = min(bisect_right(nums, max(target, target - nums[0])), len(nums) - 1)
        left = -1
        for right in range(sup, 0, -1):
            left = bisect_left(nums[left:right], target - nums[right])
            if nums[left] + nums[right] == target:
                return [left + 1, right + 1]