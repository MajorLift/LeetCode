// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort(key=lambda x: x[0])
        dp = [[0 for _ in range(k + 1)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(1, k + 1):
                start, end, val = events[i]
                next_idx = bisect_right(events, end, lo=i, key=lambda x: x[0])
                dp[i][j] = max(dp[i + 1][j], val + dp[next_idx][j - 1])
        return dp[0][k]