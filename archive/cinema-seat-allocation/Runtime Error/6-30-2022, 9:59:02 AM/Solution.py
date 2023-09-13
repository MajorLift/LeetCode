// https://leetcode.com/problems/cinema-seat-allocation

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        LEFT, MID, RIGHT = range(2, 6), range(4, 8), range(6, 10)
        availability = [[]] + [[True, True, True] for _ in range(n)]
        for [row, seat] in reservedSeats:
            if seat in LEFT:
                availability[row][0] = False
            if seat in MID:
                availability[row][1] = False
            if seat in RIGHT:
                availability[row][2] = False
        # return reduce(lambda acc, curr: acc + (2 if curr[0] and curr[2] else 1 if any(curr) else 0), availability[1:], 0)
        counter = 0
        for [l, m, r] in availability[1:]:
            if l and r:
                counter += 2
            elif any(l, m, r):
                counter += 1
        return counter