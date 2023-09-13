// https://leetcode.com/problems/minimum-time-difference

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = list(map(self.toMinutes, timePoints))
        minutes += list(map(lambda x: 60 * 24 + x, minutes))
        minutes.sort()
        return min(r - l for l, r in zip(minutes, minutes[1:]))

    def toMinutes(self, s: str) -> int:
        h, m = map(int, s.split(":"))
        return h * 60 + m