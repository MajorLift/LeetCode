// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            return max(nums[i] + dp(i - 2), dp(i - 1)) if i >= 0 else 0
        return dp(len(nums) - 1)