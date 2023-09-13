// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        return any(l == r for l, r in zip(nums, islice(nums, 1, None)))