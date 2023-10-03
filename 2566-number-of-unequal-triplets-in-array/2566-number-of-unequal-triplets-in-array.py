class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return sum(cnt[i] * cnt[j] * cnt[k] 
            for i, j, k in combinations(cnt.keys(), 3))