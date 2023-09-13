// https://leetcode.com/problems/non-overlapping-intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])
        memo = [1] + [0] * (n - 1)
        global_max = 1
        for i in range(1, n):
            local_max = 0
            for j in range(i - 1, -1, -1):
                if intervals[j][1] <= intervals[i][0]:
                    local_max = max(local_max, memo[j])
                    break
            memo[i] = max(local_max + 1, memo[i - 1])
            global_max = max(global_max, memo[i])
        return n - global_max