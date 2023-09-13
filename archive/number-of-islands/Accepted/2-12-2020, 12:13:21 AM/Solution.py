// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    cnt += 1
                    self.traverseIslandDFS(grid, x, y)
        return cnt       
        
    def traverseIslandDFS(self, grid, x, y):
        if x < 0 or y < 0 \
        or x >= len(grid[0]) or y >= len(grid) \
        or grid[y][x] == "0":
            return
        grid[y][x] = "0"
        self.traverseIslandDFS(grid, x+1, y)
        self.traverseIslandDFS(grid, x, y+1)
        self.traverseIslandDFS(grid, x-1, y)
        self.traverseIslandDFS(grid, x, y-1)