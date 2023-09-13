// https://leetcode.com/problems/non-overlapping-intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        ans = 0
        i = 1
        while True:
            if i == len(intervals):
                break
            (prev_x, prev_y), (curr_x, curr_y) = intervals[i - 1], intervals[i]
            if curr_x < prev_y:
                ans += 1
                intervals = intervals[:i] + intervals[i+1:]
            else:
                i += 1
        return ans
