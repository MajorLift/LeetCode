// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        r = bisect_right(nums, target if target > 0 else 0)
        for j in range(r - 1, 0, -1):
            for i in range(j - 1, -1, -1):
                if nums[i] + nums[j] == target:
                    return [i + 1, j + 1]