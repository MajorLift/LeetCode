// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        return any(not nums[i - 1] ^ nums[i] for i in range(1, len(nums)))