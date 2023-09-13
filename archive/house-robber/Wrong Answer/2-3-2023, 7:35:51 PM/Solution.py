// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            if i >= len(nums) - 1:
                return 0
            return min(nums[i] + dp(i + 2), dp(i + 1))
        return dp(0)