// https://leetcode.com/problems/maximum-profit-in-job-scheduling

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key=lambda x: x[0])
        pq = []
        max_prev = 0
        for start, end, val in jobs:
            while pq and start >= pq[0][0]:
                _, max_curr = heappop(pq)
                max_prev = max(max_prev, max_curr)
            heappush(pq, (end, max_prev + val))
        return max(x[1] for x in pq)