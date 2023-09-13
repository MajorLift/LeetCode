// https://leetcode.com/problems/insert-interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = sorted(intervals + [newInterval], key=lambda x: x[0])
        output = []
        for start, end in intervals:
            if not output or start > output[-1][1]:
                output.append([start, end])
            elif start <= output[-1][1] <= end:
                prev_start, prev_end = output.pop()
                output.append([prev_start, end])
        return output