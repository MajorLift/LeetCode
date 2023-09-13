// https://leetcode.com/problems/minimum-time-difference

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = list(map(self.toMinutes, timePoints))
        minutes += list(map(lambda x: 60 * 24 + x, minutes))
        n = len(minutes)
        return min(abs(minutes[i] - minutes[j]) for i in range(n - 1) for j in range(i + 1, n))

    def toMinutes(self, s: str) -> int:
        h, m = map(int, s.split(":"))
        return h * 60 + m