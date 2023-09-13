// https://leetcode.com/problems/reaching-points

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        queue = deque([(tx, ty)])
        while queue:
            x, y = queue.popleft()
            if (x, y) == (sx, sy):
                return True
            for a, b in ((x, y - x), (x - y, y)):
                if a < sx or b < sy:
                    break
                queue.append((a, b))
        return False
