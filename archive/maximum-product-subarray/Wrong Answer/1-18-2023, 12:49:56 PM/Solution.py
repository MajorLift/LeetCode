// https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        global_max, local_max = nums[0], nums[0]
        for i in range(1, n):
            local_max = max(0, local_max * nums[i])
            global_max = max(global_max, local_max)
        return global_max