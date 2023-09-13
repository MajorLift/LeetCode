// https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[1])
        output = deque([intervals[-1]])
        for i in range(len(intervals) - 2, -1, -1):
            (start, end), (start_next, end_next) = intervals[i], output[0]
            if start_next <= end:
                output[0] = min(start, start_next), end_next
            else:
                output.appendleft((start, end))
        return output