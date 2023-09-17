class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r and nums[l] < 0 and nums[r] > 0:
            if -nums[l] < nums[r]:
                r -= 1
            elif -nums[l] > nums[r]:
                l += 1
            else:
                return nums[r]
        return -1