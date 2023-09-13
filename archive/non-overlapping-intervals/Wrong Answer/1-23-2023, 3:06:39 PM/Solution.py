// https://leetcode.com/problems/non-overlapping-intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        ans = 0
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if end <= prev_end:
                ans += 1
            else:
                prev_end = end
        return ans