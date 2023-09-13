// https://leetcode.com/problems/meeting-rooms-iii

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        queue = []
        rooms = [(-1, i, 0) for i in range(n)]
        for start, end in meetings:
            if start >= rooms[0][0]:
                room_end, room_id, room_cnt = heappop(rooms)
                heappush(rooms, (end, room_id, room_cnt + 1))
            else:
                heappush(queue, (start, end - start))
                _, interval = heappop(queue)
                room_end, room_id, room_cnt = heappop(rooms)
                heappush(rooms, (room_end + interval, room_id, room_cnt + 1))
        return sorted(rooms, key=lambda x: (-x[2], x[1]))[0][1]