// https://leetcode.com/problems/cinema-seat-allocation

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        LEFT, MID, RIGHT = range(2, 6), range(4, 8), range(6, 10)
        availability = [[]] + [[True, True, True] for _ in range(n)]
        print(availability)
        for [row, seat] in reservedSeats:
            print([row, seat])
            if seat in LEFT:
                availability[row][0] = False
                print('LEFT', row, availability[row])
            if seat in MID:
                availability[row][1] = False
                print('MID', row, availability[row])
            if seat in RIGHT:
                availability[row][2] = False
                print('RIGHT', row, availability[row])
            print(row, availability)
        print(availability)
        
        return reduce(lambda acc, curr: acc + (2 if curr[0] and curr[2] else 1 if any(curr) else 0), availability[1:], 0)
            