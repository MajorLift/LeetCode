// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        acc = prev = 0
        for i in range(len(nums) - 1, -1, -1):
            acc, prev = max(nums[i] + prev, acc), acc
        return acc