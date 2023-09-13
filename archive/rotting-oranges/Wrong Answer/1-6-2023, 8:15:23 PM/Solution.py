// https://leetcode.com/problems/rotting-oranges

from multiprocessing import Pool

class Solution:
    def init_worker(self, grid_init):
        global grid
        grid = grid_init

    def orangesRotting(self, init: List[List[int]]):
        self.m, self.n = len(init), len(init[0])
        self.init = init
        fresh = [(i, j) for i in range(self.m) for j in range(self.n) if init[i][j] == 1]
        if not fresh: 
            return 0
        rotten = [(i, j) for i in range(self.m) for j in range(self.n) if init[i][j] == 2]
        if not rotten:
            return -1

        with Pool(initializer=self.init_worker, initargs=(self.init,)) as pool:
            times = pool.map(self.dfs_wrapper, [(r, c, thread) for thread, (r, c) in enumerate(rotten)])
            fresh = [(i, j) for i in range(self.m) for j in range(self.n) if init[i][j] == 1]
            return max(times) if len(fresh) == 0 else -1
    
    def dfs(self, r, c, thread, clock = 0):
        global grid
        if clock > 0:
            grid[r][c] = 2
        print(thread, (r, c), clock), print(grid)
        neighbors = [(i, j) for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)) \
            if 0 <= i < self.m and 0 <= j < self.n and grid[i][j] == 1]
        times = [self.dfs(r, c, thread, clock + 1) for r, c in neighbors]
        return max(times or [clock])

    def dfs_wrapper(self, args):
        return self.dfs(*args)