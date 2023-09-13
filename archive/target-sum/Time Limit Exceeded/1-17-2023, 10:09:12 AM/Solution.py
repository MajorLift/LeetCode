// https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dp(idx = len(nums) - 1, curr = 0):
            if idx < 0: 
                return 1 if curr == target else 0
            return dp(idx - 1, curr + nums[idx - 1]) + dp(idx - 1, curr - nums[idx - 1])
        return dp()