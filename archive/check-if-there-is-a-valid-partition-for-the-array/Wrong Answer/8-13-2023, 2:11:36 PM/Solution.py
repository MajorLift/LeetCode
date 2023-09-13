// https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def dp(i):
            if i >= n:
                return True
            if i < n - 1 and nums[i] == nums[i + 1]:
                return dp(i + 2)
            elif i < n - 2 and nums[i] == nums[i + 1] == nums[i + 2]:
                return dp(i + 3)
            elif i < n - 2 and nums[i + 1] - nums[i] == nums[i + 2] - nums[i + 1] == 1:
                return dp(i + 3)
            return False
        return dp(0)