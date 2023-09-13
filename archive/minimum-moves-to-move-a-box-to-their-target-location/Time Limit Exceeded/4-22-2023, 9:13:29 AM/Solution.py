// https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        self.grid, self.m, self.n = grid, len(grid), len(grid[0])
        self.DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        (xs, ys), (xb, yb), (self.xt, self.yt) = map(self.findCellType, ('S', 'B', 'T'))

        visited = set([((xb, yb), (xs, ys))])
        pq = [(self.heuristic(xb, yb), 0, (xb, yb), (xs, ys))]
        while pq:
            _, moves, (rb, cb), (rs, cs) = heappop(pq)
            visited.add(((rb, cb), (rs, cs)))
            if (rb, cb) == (self.xt, self.yt):
                return moves
            for d in self.DIRECTIONS:
                ib, jb = map(sum, zip((rb, cb), d))
                is_, js = map(sum, zip((rb, cb), map(operator.neg, d)))
                if not self.valid(ib, jb) \
                    or not self.valid(is_, js) \
                    or not self.traversable((rs, cs), (is_, js), (rb, cb)) \
                    or ((ib, jb), (is_, js)) in visited:
                    continue
                heappush(pq, (self.heuristic(ib, jb) + moves + 1, moves + 1, (ib, jb), (is_, js)))
        return -1
    
    def heuristic(self, x, y):
        return abs(self.xt - x) + abs(self.yt - y)
    
    def valid(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n \
            and self.grid[x][y] != '#'

    def traversable(self, src, dst, box):
        queue, visited = deque([src]), set()
        while queue:
            curr = queue.popleft()
            visited.add(curr)
            if curr == dst:
                return True
            for i, j in (map(sum, zip(d, curr)) for d in self.DIRECTIONS):
                if self.valid(i, j) \
                    and (i, j) != box \
                    and (i, j) not in visited:
                    queue.append((i, j))
        return False
        
    def findCellType(self, cell_type):
        for i, j in product(range(self.m), range(self.n)):
            if self.grid[i][j] == cell_type:
                return (i, j)
