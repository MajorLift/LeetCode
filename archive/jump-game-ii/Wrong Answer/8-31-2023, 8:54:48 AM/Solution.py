// https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        i = cnt = 0
        while True:
            cnt += 1
            if i + nums[i] >= n - 1: break
            _, i = max(((nums[i + j], j) for j in range(1, nums[i] + 1)), key=lambda x: x[0])
        return cnt
