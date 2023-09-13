// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i, min(i + nums[i] + 1, len(nums))):
                dp[i] = dp[j]
        return dp[0]