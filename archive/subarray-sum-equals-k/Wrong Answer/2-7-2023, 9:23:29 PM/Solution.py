// https://leetcode.com/problems/subarray-sum-equals-k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = list(accumulate(nums, lambda x, y: x + y))
        ans = 1
        l = r = 0
        while l <= r < len(nums):
            diff = prefix_sum[r] - prefix_sum[l]
            if diff == k:
                ans += 1
            if diff >= k:
                l += 1
            if diff < k:
                r += 1
        return ans