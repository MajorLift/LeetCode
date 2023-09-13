// https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        cum_sums = [nums[0]] + [0] * (n - 1) 
        for i in range(1, n):
            cum_sums[i] = cum_sums[i - 1] + nums[i]
        return 1 - min(min(cum_sums), 0)