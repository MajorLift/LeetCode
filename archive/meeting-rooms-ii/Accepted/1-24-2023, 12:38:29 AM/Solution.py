// https://leetcode.com/problems/meeting-rooms-ii

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        rooms = [intervals[0][1]]
        ans = 1
        for start, end in intervals[1:]:
            print(rooms)
            if rooms[0] <= start:
                heappop(rooms)
            heappush(rooms, end)
            ans = max(ans, len(rooms))
        return ans