// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort(key=lambda x: x[0])
        @cache
        def dp(idx = 0, remaining = k):
            if remaining == 0 or idx >= n:
                return 0
            start, end, val = events[idx]
            next_idx = bisect_right([i for i in range(n)], end, lo=idx, key=lambda i: events[i][0])
            return max(dp(idx + 1, remaining), val + dp(next_idx, remaining - 1))
        return dp()