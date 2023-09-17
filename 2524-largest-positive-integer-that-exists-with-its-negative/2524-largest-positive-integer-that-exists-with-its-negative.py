class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums_set = set(nums)
        return max([num for num in nums_set
                    if num > 0 and -num in nums_set] 
                or [-1])