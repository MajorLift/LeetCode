// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        pq = [(end, start) for start, end in events]
        heapify(pq)
        ans = 0
        d = 1
        while pq:
            while pq and pq[0][0] < d:
                heappop(pq)
            if pq and pq[0][1] <= d:
                print(d, heappop(pq))
                ans += 1
            d += 1
        return ans