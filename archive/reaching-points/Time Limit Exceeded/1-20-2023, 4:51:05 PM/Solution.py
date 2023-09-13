// https://leetcode.com/problems/reaching-points

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        queue = deque([(sx, sy)])
        while queue:
            x, y = queue.popleft()
            if (x, y) == (tx, ty):
                return True
            for a, b in ((x, x + y), (x + y, y)):
                if sx <= a <= tx and sy <= b <= ty:
                    queue.append((a, b))
        return False