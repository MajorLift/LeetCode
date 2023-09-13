// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def dp(i):
            return max(nums[i] + dp(i - 2), dp(i - 1)) if i > 1 else nums[i]
        return dp(n - 1)