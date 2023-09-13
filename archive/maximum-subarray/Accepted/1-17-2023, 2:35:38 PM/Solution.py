// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        global_max = nums[0]
        last_max = nums[0]
        for i in range(1, n):
            last_max = max(last_max, 0) + nums[i]
            global_max = max(global_max, last_max)
        return global_max