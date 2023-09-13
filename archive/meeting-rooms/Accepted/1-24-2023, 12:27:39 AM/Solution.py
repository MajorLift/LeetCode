// https://leetcode.com/problems/meeting-rooms

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals) - 1):
            curr_end, next_start = intervals[i][1], intervals[i + 1][0]
            if next_start < curr_end:
                return False
        return True
