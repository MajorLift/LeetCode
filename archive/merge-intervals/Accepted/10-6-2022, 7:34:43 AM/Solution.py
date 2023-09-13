// https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals_sorted = sorted(intervals, key=lambda x: (x[0], x[1]))
        merged = [intervals_sorted[0]]
        for i in range(1, n):
            start_curr, end_curr = intervals_sorted[i]
            start_merged, end_merged = merged[-1]
            if end_merged < start_curr:
                merged.append([start_curr, end_curr])
            else:
                merged[-1][1] = max(end_merged, end_curr)
        return merged