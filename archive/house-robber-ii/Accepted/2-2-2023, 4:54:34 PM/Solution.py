// https://leetcode.com/problems/house-robber-ii

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        candidates = nums[:-1], nums[1:]
        @cache
        def dp(c, i = len(nums) - 2):
            arr = candidates[c]
            if i < 0:
                return 0
            return max(arr[i] + dp(c, i - 2), dp(c, i - 1))
        return max(dp(0), dp(1))