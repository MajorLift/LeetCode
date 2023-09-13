// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [0] * (len(nums) - 2) + nums[-2:]
        for i in range(len(nums) - 3, -1, -1):
            memo[i] = max(nums[i] + memo[i + 2], memo[i + 1])
        return memo[0]