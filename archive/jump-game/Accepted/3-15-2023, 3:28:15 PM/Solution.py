// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = -1
        for i in range(n):
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= n - 1:
                return True
            if i >= max_reach and nums[i] == 0:
                return False
        return False