// https://leetcode.com/problems/reaching-points

from collections import deque

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        queue = deque([(sx, sy)])
        while queue:
            curr_x, curr_y = queue.popleft()
            if (curr_x, curr_y) == (tx, ty):
                return True
            elif curr_x > tx or curr_y > ty:
                continue
            else:
                queue.append((curr_x, curr_x + curr_y))
                queue.append((curr_x + curr_y, curr_y))
        return False