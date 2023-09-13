// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        return reduce(lambda acc, curr: (max(curr + acc[1], acc[0]), acc[0]), nums[::-1], (0, 0))[0]