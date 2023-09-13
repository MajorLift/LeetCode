// https://leetcode.com/problems/two-best-non-overlapping-events

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        local_max, global_max = 0, 0
        pq = []
        for start, end, val in events:
            heappush(pq, (end, val))
            while pq and pq[0][0] < start:
                r, v = heappop(pq)
                local_max = max(local_max, v)
            global_max = max(global_max, local_max + val)
        return global_max