// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        curr = n - 1
        for i in range(n - 1, -1, -1):
            if i + nums[i] >= curr:
                curr = i
        return curr == 0