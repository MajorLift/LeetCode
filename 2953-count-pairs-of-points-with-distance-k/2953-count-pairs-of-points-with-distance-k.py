class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        ans, cnt = 0, Counter()
        for x, y in coordinates:
            for t in range(k + 1):
                ans += cnt[(x ^ t, y ^ (k - t))]
            cnt[(x, y)] += 1
        return ans
    