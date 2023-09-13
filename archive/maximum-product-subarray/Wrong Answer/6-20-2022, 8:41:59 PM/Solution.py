// https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return None
        dp = [nums[0]] + [None] * (len(nums) - 1)
        for i in range(1, len(nums)):
            dp[i] = max(1, dp[i - 1]) * nums[i]
        return max(dp)