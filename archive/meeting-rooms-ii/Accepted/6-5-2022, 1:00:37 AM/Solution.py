// https://leetcode.com/problems/meeting-rooms-ii

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([e[0] for e in intervals])
        ends = sorted([e[1] for e in intervals])
        
        result = 0
        e_ptr = 0
        for start in starts:
            if start < ends[e_ptr]:
                result += 1
            else:
                e_ptr += 1
        
        return result