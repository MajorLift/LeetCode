// https://leetcode.com/problems/shortest-path-to-get-all-keys

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        grid = [[*row] for row in grid]
        m, n = map(len, (grid, grid[0]))
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))

        start = (-1, -1)
        all_keys = 0
        for i, j in product(range(m), range(n)):
            if grid[i][j] == "@":
                start = (i, j)
            if grid[i][j].islower():
                all_keys |= (1 << (ord(grid[i][j]) - ord('a')))

        visited = defaultdict(set)
        visited[0].add(start)
        pq = [(0, 0, start)]
        while pq:
            moves, state, (r, c) = heappop(pq)
            visited[state].add((r, c))
            if state == all_keys:
                return moves
            for i, j in (map(sum, zip((r, c), d)) for d in DIRECTIONS):
                if not (0 <= i < m and 0 <= j < n) \
                    or grid[i][j] == "#" \
                    or grid[i][j].isupper() and state & (1 << (ord(grid[i][j]) - ord('A'))) == 0 \
                    or (i, j) in visited[state]:
                    continue
                if grid[i][j].islower():
                    state |= (1 << (ord(grid[i][j]) - ord('a')))
                    heappush(pq, ((moves + 1, state, (i, j))))
                else:
                    heappush(pq, ((moves + 1, state, (i, j))))
        return -1