// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {e: i for i,e in enumerate(nums)}
        complements = [target - num for num in nums]
        for i, comp in enumerate(complements):
            if nums_dict[comp]:
                return [i, nums_dict[comp]]
        