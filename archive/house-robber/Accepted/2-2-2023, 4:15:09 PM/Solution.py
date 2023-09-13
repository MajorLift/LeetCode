// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        acc = prev = 0
        for i in range(len(nums)):
            acc, prev = max(nums[i] + prev, acc), acc
        return acc