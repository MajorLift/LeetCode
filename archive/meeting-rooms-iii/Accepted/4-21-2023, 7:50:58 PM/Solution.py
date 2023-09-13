// https://leetcode.com/problems/meeting-rooms-iii

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        avail = list(range(n))
        used = []
        cnt = [0] * n
        for start, end in sorted(meetings, key=lambda x: x[0]):
            while used and used[0][0] <= start:
                heappush(avail, heappop(used)[1])
            if avail:
                room = heappop(avail)
                heappush(used, (end, room))
            else:
                next_end, room = heappop(used)
                heappush(used, (next_end + (end - start), room))
            cnt[room] += 1
        return cnt.index(max(cnt))