class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        return sum(1 
            for triplet in combinations(nums, 3) 
            if all(l != r for l, r in combinations(triplet, 2)))