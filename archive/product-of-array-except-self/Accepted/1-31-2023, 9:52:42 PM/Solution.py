// https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = list(accumulate(nums, operator.mul))
        suffix = list(accumulate(nums[::-1], operator.mul))[::-1]
        return [(prefix[i - 1] if i > 0 else 1) \
            * (suffix[i + 1] if i < n - 1 else 1) \
            for i in range(n)]