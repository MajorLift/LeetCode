// https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(i, x):
            if i < 0: 
                return 1 if x == 0 else 0
            return dp(i - 1, x + nums[i]) + dp(i - 1, x - nums[i])
        return dp(len(nums) - 1, target)