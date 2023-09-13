// https://leetcode.com/problems/non-overlapping-intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        curr_end = -math.inf
        for start, end in intervals:
            if start < curr_end:
                count += 1
            else:
                curr_end = end
        return count