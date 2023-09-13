// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(i):
            curr_max = -math.inf
            for j in range(i):
                if nums[i] > nums[j]:
                    curr_max = max(curr_max, dp(j) + 1)
            return curr_max if curr_max > -math.inf else 1
        return dp(n - 1)