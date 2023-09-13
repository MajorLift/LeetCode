// https://leetcode.com/problems/insert-interval

class Solution:    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = [], None
        start_new, end_new = newInterval
        for i, (start, end) in enumerate(intervals):
            if start > end_new:
                r = intervals[i:]
                break
            elif end < start_new:
                l.append(intervals[i])
            else:
                start_new, end_new = min(start, start_new), max(end, end_new)
        return l + [[start_new, end_new]] + r