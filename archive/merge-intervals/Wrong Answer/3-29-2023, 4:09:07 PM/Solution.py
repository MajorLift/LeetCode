// https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[1])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            start_prev, end_prev = output[-1]
            if start_prev <= start <= end_prev:
                output[-1] = min(start_prev, start), max(end_prev, end)
            else:
                output.append((start, end))
        return output