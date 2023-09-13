// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @cache
        def dp(i):
            if i == len(nums) - 1: return True
            return any(dp(j) for j in range(min(i + nums[i], len(nums) - 1), i, -1))
        return dp(0)