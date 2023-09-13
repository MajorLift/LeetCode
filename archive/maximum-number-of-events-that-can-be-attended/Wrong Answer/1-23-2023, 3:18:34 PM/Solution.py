// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        pq = [(-end, start) for start, end in events]
        heapify(pq)
        d = -1
        while pq:
            while pq and pq[0][1] < d:
                heappop(pq)
            if pq:
                curr = heappop(pq)
                start, end = curr[0], -curr[1]
            d += 1
        return d + 1