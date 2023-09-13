// https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = -math.inf
        local_max = local_min = nums[0]
        for num in nums[1:]:
            local_max, local_min = max(num, local_max * num, local_min * num), \
                min(num, local_max * num, local_min * num)
            global_max = max(global_max, local_max)
        return int(global_max)