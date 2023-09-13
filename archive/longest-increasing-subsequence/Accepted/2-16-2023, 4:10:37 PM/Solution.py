// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(i):
            local_max = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    local_max = max(local_max, dp(j) + 1)
            return local_max if local_max > 0 else 1
        return max(dp(i) for i in range(n - 1, -1, -1))