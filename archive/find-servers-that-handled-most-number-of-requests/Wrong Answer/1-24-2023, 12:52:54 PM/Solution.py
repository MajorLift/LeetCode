// https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        cnt = defaultdict(int)
        busy = []
        available = [_id for _id in range(k)]
        for i, (start, duration) in enumerate(zip(arrival, load)):
            while busy and start >= busy[0][0]:
                server_end, server_id = heappop(busy)
                available.append(server_id)
            if not available:
                continue
            idx = bisect_left(available, i % k)
            assigned_id = available[idx] if idx < len(available) else available[0]
            available.remove(assigned_id)            
            cnt[assigned_id] += 1
            heappush(busy, (start + duration, assigned_id))
        return [k for k, v in cnt.items() if v == max(cnt.values())]