// https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()
        for k in range(len(nums) - 1, bisect_right(nums, 0) - 1, -1):
            for i, j in self.twoSumSorted(nums[:k], -nums[k]):
                output.add((nums[i], nums[j], nums[k]))
        for k in range(bisect_left(nums, 0)):
            for i, j in self.twoSumSorted(nums[bisect_left(nums, 0) + 1:], -nums[k]):
                output.add((nums[k], nums[i], nums[j]))
        if bisect_right(nums, 0) - bisect_left(nums, 0) + 1 >= 3:
            output.add((0, 0, 0))
        return output
        
    def twoSumSorted(self, nums, target):
        left, right = 0, len(nums) - 1
        output = []
        while left < right:
            if nums[left] + nums[right] == target:
                output.append((left, right))
                left, right = left + 1, right - 1
            while left < len(nums) - 1 and nums[left] + nums[right] < target:
                left = max(left + 1, 
                    bisect_left(nums, target - nums[right], 
                        lo=left + 1, hi=right - 1))
            while right > 0 and nums[left] + nums[right] > target:
                right = min(right - 1, 
                    bisect_right(nums, target - nums[left], 
                        lo=left + 1, hi=right - 1))
        return output