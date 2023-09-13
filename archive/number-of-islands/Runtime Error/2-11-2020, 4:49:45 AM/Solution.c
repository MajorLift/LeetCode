// https://leetcode.com/problems/number-of-islands


void DFSMarkIsland(char** grid, int x, int y){
    if(x < 0 || y < 0 || \
       y >= sizeof(grid) || x >= sizeof(grid[0]) || \
       grid[y][x] == '0') return;
    grid[y][x] = '0';
    DFSMarkIsland(grid, x + 1, y);
    DFSMarkIsland(grid, x, y + 1);
    DFSMarkIsland(grid, x - 1, y);
    DFSMarkIsland(grid, x, y - 1);
}


int numIslands(char** grid, int gridSize, int* gridColSize){
    // gridColSize = sizeof(grid);
    // int i = 0;
    // while(i < gridColSize){
    //     gridRowSize[i] = sizeof(grid[i]);
    //     i++;
    // }
    
    int count = 0;
    int y = 0;
    while(y < gridSize){
        int x = 0;
        while(x < *gridColSize){
            if(grid[y][x] == '1'){
                count++;
                DFSMarkIsland(grid, x, y);
            }
            x++;
        }
        y++;
    }
    return count;
}

