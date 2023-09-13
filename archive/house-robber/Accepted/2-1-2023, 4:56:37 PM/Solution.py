// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            if i < 0:
                return 0
            return max(nums[i] + dp(i - 2), dp(i - 1))
        return dp(len(nums) - 1)