// https://leetcode.com/problems/non-overlapping-intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        ans = 0
        prev_end = -math.inf
        for start, end in intervals:
            if start < prev_end:
                ans += 1
            else:
                prev_end = end
        return ans