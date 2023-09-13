// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def maxSubArray(l = 0, r = len(nums) - 1):
            if l > r: 
                return -math.inf
            mid = (l + r) // 2
            left_sum = right_sum = curr_sum = 0
            for i in range(mid - 1, l - 1, -1):
                left_sum = max(left_sum, curr_sum := curr_sum + nums[i])
            curr_sum = 0
            for i in range(mid + 1, r + 1):
                right_sum = max(right_sum, curr_sum := curr_sum + nums[i])
            
            return max(maxSubArray(l, mid - 1), 
                maxSubArray(mid + 1, r), 
                left_sum + nums[mid] + right_sum)
        
        return maxSubArray()