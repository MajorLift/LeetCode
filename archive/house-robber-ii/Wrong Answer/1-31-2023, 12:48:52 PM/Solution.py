// https://leetcode.com/problems/house-robber-ii

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        candidates = [nums[:-1], nums[1:]]
        @cache
        def dp(i, x):
            if i < 2:
                 return candidates[x][i]
            return max(candidates[x][i] + dp(i - 2, x), dp(i - 1, x))
        return max(dp(n - 2, 0), dp(n - 2, 1))