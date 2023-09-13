// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        memo = [0] * len(nums)
        for i in range(len(nums)):
            memo[i] = max(nums[i] + memo[i - 2], memo[i - 1])
        return memo[-1]