// https://leetcode.com/problems/reaching-points

from collections import deque

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        queue = deque([(sx, sy)])
        visited = set()
        while queue:
            curr_x, curr_y = queue.popleft()
            visited.add((curr_x, curr_y))
            if (curr_x, curr_y) == (tx, ty):
                return True
            elif curr_x > tx or curr_y > ty:
                continue
            else:
                if (curr_x, curr_x + curr_y) not in visited:
                    queue.append((curr_x, curr_x + curr_y))
                if (curr_x + curr_y, curr_y) not in visited:
                    queue.append((curr_x + curr_y, curr_y))
        return False