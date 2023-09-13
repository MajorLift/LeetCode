// https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        cnt = defaultdict(int)
        busy = dict()
        available = set([i for i in range(k)])
        for i, (start, duration) in enumerate(zip(arrival, load)):
            for server_id, server_end in list(busy.items()):
                if start >= server_end:
                    del busy[server_id]
                    available.add(server_id)
            if not available:
                continue
            j = 0
            while (i + j) % k not in available:
                j += 1
            assigned = (i + j) % k
            cnt[assigned] += 1
            available.remove(assigned)
            busy[assigned] = start + duration
        return [k for k, v in cnt.items() if v == max(cnt.values())]