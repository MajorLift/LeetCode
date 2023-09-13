// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        nums += [0]
        @cache
        def dp(i):
            if i < 2:
                return nums[i]
            return max(nums[i] + dp(i - 2), dp(i - 1))
        return dp(len(nums) - 1)