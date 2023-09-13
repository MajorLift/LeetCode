// https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = l = r = 0
        while (r < len(nums) - 1):
            reach = 0
            for i in range(l, r + 1):
                reach = max(reach, i + nums[i])
            l, r = r + 1, reach
            ans += 1
        return ans