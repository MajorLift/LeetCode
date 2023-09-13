// https://leetcode.com/problems/meeting-rooms-iii

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        rooms = []
        empty = [(-1, i, 0) for i in range(n)]
        queue = []
        for start, end in meetings:
            if queue:
                _, interval = heappop(queue)
                if empty:
                    empty_end, empty_id, empty_cnt = heappop(empty)
                    heappush(rooms, (empty_end + interval, empty_id, empty_cnt + 1))
                else:
                    room_end, room_id, room_cnt = heappop(rooms)
                    heappush(rooms, (room_end + interval, room_id, room_cnt + 1))

            if rooms and start >= rooms[0][0]:
                room_end, room_id, room_cnt = heappop(rooms)
                heappush(rooms, (end, room_id, room_cnt + 1))
            if empty and (not rooms or start < rooms[0][0]):
                empty_end, empty_id, empty_cnt = heappop(empty)
                heappush(rooms, (end, empty_id, empty_cnt + 1))
            if not empty and start < rooms[0][0]:
                heappush(queue, (start, end - start))
                
        # print(sorted(rooms, key=lambda x: (-x[2], x[1])))
        return sorted(rooms + empty, key=lambda x: (-x[2], x[1]))[0][1] - 1