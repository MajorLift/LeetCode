// https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        self.DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        (xs, ys), (xb, yb), (xt, yt) = map(self.findCellType, ('S', 'B', 'T'))

        dist = [[+inf] * self.n for _ in range(self.m)]
        dist[xb][yb] = 0
        pq = [(self.manhattanDist((xb, yb), (xt, yt)), 0, (xb, yb), (xs, ys))]
        while pq:
            heuristic, moves, (rb, cb), (rs, cs) = heappop(pq)
            if (rb, cb) == (xt, yt):
                break
            for d in self.DIRECTIONS:
                ib, jb = map(sum, zip((rb, cb), d))
                is_, js = map(sum, zip((rb, cb), map(operator.neg, d)))
                if not self.valid(ib, jb) \
                    or not self.valid(is_, js) \
                    or not self.traversable((rs, cs), (is_, js), (rb, cb)):
                    continue
                if moves + 1 < dist[ib][jb]:
                    dist[ib][jb] = moves + 1
                heappush(
                    pq, 
                    (
                        self.manhattanDist((ib, jb), (xt, yt)), 
                        moves + 1, 
                        (ib, jb), 
                        (rb, cb)
                    )
                )
        return dist[xt][yt] if dist[xt][yt] < +inf else -1
    
    def manhattanDist(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def valid(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n \
            and self.grid[x][y] != '#'

    def traversable(self, src, dst, box):
        queue, visited = deque([src]), set()
        while queue:
            curr = queue.popleft()
            if curr == dst:
                return True
            for i, j in (map(sum, zip(d, curr)) for d in self.DIRECTIONS):
                if self.valid(i, j) \
                    and (i, j) != box \
                    and (i, j) not in visited:
                    visited.add((i, j))
                    queue.append((i, j))
        return False
        
    def findCellType(self, cell_type):
        for i, j in product(range(self.m), range(self.n)):
            if self.grid[i][j] == cell_type:
                return (i, j)
