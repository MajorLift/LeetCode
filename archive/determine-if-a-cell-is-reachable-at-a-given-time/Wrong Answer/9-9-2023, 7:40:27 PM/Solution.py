// https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        min_diag = min(abs(fx - sx), abs(fy - sy))
        return t <= min_diag + fy - min_diag + fx - min_diag