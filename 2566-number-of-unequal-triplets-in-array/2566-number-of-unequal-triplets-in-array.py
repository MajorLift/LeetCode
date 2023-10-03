class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        return sum(1 
            for i, j, k in combinations(nums, 3) 
            if i != j and j != k and k != i)