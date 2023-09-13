// https://leetcode.com/problems/maximum-profit-in-job-scheduling

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key=lambda x: x[0])
        global_max = 0
        pq = []
        for start, end, val in jobs:
            while pq and start >= pq[0][0]:
                _, local_max = heappop(pq)
                global_max = max(global_max, local_max)
            heappush(pq, (end, global_max + val))
        return max(x[1] for x in pq)