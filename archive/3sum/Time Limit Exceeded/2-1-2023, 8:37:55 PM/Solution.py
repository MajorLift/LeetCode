// https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()
        for k in range(len(nums) - 1, 1, -1):
            for i, j in self.twoSumSorted(nums[:k], -nums[k]):
                output.add((nums[i], nums[j], nums[k]))
        return output
        
    def twoSumSorted(self, nums, target):
        output = []
        for right in range(len(nums) - 1, 0, -1):
            left = bisect_left(nums[:right], target - nums[right])
            if left < right and nums[left] + nums[right] == target:
                output.append([left, right])
        return output