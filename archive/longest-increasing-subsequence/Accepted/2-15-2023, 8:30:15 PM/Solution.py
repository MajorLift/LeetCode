// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [1] * n
        for r in range(1, n):
            for l in range(r):
                if nums[r] > nums[l]:
                    memo[r] = max(memo[r], memo[l] + 1)
        return max(memo)
