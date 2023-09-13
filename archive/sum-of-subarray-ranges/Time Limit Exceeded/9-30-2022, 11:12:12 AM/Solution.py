// https://leetcode.com/problems/sum-of-subarray-ranges

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            largest, smallest = nums[i], nums[i]
            for j in range(i, n):
                largest, smallest = max(largest, nums[j]), min(smallest, nums[j])
                ans += largest - smallest
        return ans