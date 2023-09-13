// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def dp(i):
            if i == n - 1:
                return True
            return any(dp(j) for j in range(min(i + nums[i], n - 1), i, -1))
        return dp(0)