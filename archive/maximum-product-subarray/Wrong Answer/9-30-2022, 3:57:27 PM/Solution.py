// https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [nums[0]] + [0 for _ in range(n - 1)]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] * nums[i], 0)
        return max(dp)