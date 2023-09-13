// https://leetcode.com/problems/minimum-interval-to-include-each-query

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        output = defaultdict(int)
        pq = []
        for query in sorted(queries):
            for l, r in intervals:
                if l <= query <= r:
                    heappush(pq, (r - l + 1, r))
            while pq and query > pq[0][1]:
                heappop(pq)
            output[query] = pq[0][0] if pq else -1
        return [output[query] for query in queries]