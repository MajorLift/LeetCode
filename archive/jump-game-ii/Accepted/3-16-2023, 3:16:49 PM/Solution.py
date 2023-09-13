// https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = reach = ans = 0
        while r < len(nums) - 1:
            reach = max(reach, *[i + nums[i] for i in range(l, r + 1)])
            l, r = r + 1, reach
            ans += 1
        return ans