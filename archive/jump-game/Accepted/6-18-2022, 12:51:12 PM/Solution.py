// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * (len(nums) - 1) + [True]
        for i in range(len(nums) - 2, -1, -1):
            dp[i] = any(dp[j] for j in range(i, min(i + nums[i] + 1, len(nums))))
        return dp[0]