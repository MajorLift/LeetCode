class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n, cnt = len(nums), Counter(nums)
        return math.comb(n, 3) - sum(math.comb(v, 2) * (n - v) + math.comb(v, 3) for v in cnt.values())