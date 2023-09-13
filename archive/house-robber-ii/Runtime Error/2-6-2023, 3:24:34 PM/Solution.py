// https://leetcode.com/problems/house-robber-ii

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[0 for _ in range(n - 1)] for _ in range(2)]
        for c in range(2):
            for i in range(n - 1):
                memo[c][i] = max(nums[(i + c) % n] + memo[c][i - 2], memo[c][i - 1])
        return max(memo[0][n - 2], memo[1][n - 2])