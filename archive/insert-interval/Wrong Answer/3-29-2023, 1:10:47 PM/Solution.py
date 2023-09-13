// https://leetcode.com/problems/insert-interval

class Solution:    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l = []
        start_new, end_new = newInterval
        for i, (start, end) in enumerate(intervals):
            if start > end_new:
                return l + [[start_new, end_new]] + intervals[i:]
            elif end < start_new:
                l.append(intervals[i])
            else:
                start_new, end_new = min(start, start_new), max(end, end_new)
        
        # return l + [[start_new, end_new]]