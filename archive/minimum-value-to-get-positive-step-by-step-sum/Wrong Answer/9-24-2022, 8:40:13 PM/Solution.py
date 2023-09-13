// https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sums = [0] * (len(nums))
        for i, num in enumerate(nums):
            sums[i] = sums[i - 1] + num
        return 1 - min(sums[1:])