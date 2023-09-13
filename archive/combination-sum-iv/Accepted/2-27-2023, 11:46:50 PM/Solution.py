// https://leetcode.com/problems/combination-sum-iv

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dp(remainder):
            if remainder == 0: return 1
            if remainder < 0: return 0
            return sum(dp(remainder - num) for num in nums)
        return dp(target)