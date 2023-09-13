// https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        output = []
        for start, end in intervals:
            if not output or start > output[-1][1]:
                output.append([start, end])
            elif start <= output[-1][1] and end > output[-1][1]:
                last_start, last_end = output.pop()
                output.append([last_start, end])
        return output