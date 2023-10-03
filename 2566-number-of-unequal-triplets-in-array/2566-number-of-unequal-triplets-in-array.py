class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        return sum(x != y and y != z and z != x
            for x, y, z in combinations(nums, 3)) 