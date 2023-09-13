// https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda curr, acc: acc ^ curr, nums, 0)