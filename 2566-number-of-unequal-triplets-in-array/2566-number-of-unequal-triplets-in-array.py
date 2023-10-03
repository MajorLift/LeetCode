class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        return sum(1 
            for i, j, k in combinations(range(len(nums)), 3) 
            if nums[i] != nums[j] 
                and nums[j] != nums[k] 
                and nums[k] != nums[i])