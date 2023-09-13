// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @cache
        def dp(i):
            if i == len(nums) - 1: return True
            return any(dp(j) for j in range(i + 1, min(i + nums[i] + 1, len(nums))))
        return dp(0)