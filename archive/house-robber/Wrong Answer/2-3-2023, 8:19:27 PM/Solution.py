// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        memo = [0] + nums[1:]
        for i in range(len(nums) - 1, -1, -1):
            memo[i] = max(nums[i] + memo[i - 2], memo[i - 1])
        return memo[0]