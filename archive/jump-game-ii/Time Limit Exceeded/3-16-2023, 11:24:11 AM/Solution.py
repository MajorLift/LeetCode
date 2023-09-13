// https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        best = +math.inf
        @cache
        def backtrack(candidate, target):
            nonlocal best
            if candidate >= best:
                return
            if target <= 0:
                best = candidate
            for i in range(target - 1, -1, -1):
                if i + nums[i] >= target:
                    backtrack(candidate + 1, i)
        backtrack(0, len(nums) - 1)
        return best