// https://leetcode.com/problems/minimum-time-to-complete-trips

class Solution:
    def minimumTime(self, times: List[int], totalTrips: int) -> int:
        for totalTime in range(max(times) + 1):
            if sum(totalTime // time for time in times) >= totalTrips:
                return totalTime
        return -1