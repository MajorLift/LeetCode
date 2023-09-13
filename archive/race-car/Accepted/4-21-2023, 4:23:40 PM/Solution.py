// https://leetcode.com/problems/race-car

class Solution:
    def racecar(self, target: int) -> int:
        moves, pos, speed = 0, 0, 1
        pq = [(moves, pos, speed)]
        while pq:
            moves, pos, speed = heappop(pq)
            if pos == target:
                break
            heappush(pq, (moves + 1, pos + speed, speed * 2))
            if (speed > 0 and pos + speed > target 
                or speed < 0 and pos + speed < target):
                heappush(pq, (moves + 1, pos, -1 if speed > 0 else 1))
        return moves