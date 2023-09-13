// https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(i, x):
            if i >= len(nums): 
                return 1 if x == target else 0
            return dp(i + 1, x + nums[i]) + dp(i + 1, x - nums[i])
        return dp(0, 0)