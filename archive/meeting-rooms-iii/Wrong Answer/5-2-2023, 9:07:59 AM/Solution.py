// https://leetcode.com/problems/meeting-rooms-iii

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        avail, busy, cnt = list(range(n)), [], [0] * n

        for start, end in sorted(meetings, key=lambda x:x[0]):
            while busy and busy[0][0] <= start:
                heappop(busy)

            if avail:
                room_id = heappop(avail)
                heappush(busy, (end, room_id))
                cnt[room_id] += 1
            
            elif busy:
                nxt_end, nxt_id = heappop(busy)
                heappush(busy, (nxt_end + (end - start), nxt_id))
                cnt[nxt_id] += 1

        return cnt.index(max(cnt))
