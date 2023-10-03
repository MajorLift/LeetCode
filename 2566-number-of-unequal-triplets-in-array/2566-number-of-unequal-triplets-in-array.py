class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        return sum(1 
            for x, y, z in combinations(nums, 3) 
            if x != y and y != z and z != x)