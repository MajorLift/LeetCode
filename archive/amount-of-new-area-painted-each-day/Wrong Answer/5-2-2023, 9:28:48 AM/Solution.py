// https://leetcode.com/problems/amount-of-new-area-painted-each-day

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        intervals = []
        maxEnd = -inf
        for day, (start, end) in enumerate(paint):
            heappush(intervals, (start, day, 'START'))
            heappush(intervals, (end, day, 'END'))
            maxEnd = max(maxEnd, end)
        
        worklog, pq = [0] * len(paint), []
        for pos in range(maxEnd + 1):
            while intervals and intervals[0][0] == pos:
                _, day, _type = heappop(intervals)
                if _type == 'START':
                    heappush(pq, day)
                if _type == 'END':
                    pq = list(filter(lambda x: x != day, pq))
            if pq:
                worklog[pq[0]] += 1

        return worklog