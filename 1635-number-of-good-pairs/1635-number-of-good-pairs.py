class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(math.comb(k, 2) for k in Counter(nums).values())
