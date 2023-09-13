// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[:2])
            return max(nums[i] + dp(i - 2), dp(i - 1))
        return dp(n - 1)