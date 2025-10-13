class Solution:
    def dfs(self, row,col,vis,grid):
        vis[row][col] = 1
        m = len(grid)
        n = len(grid[0])
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        for dr, dc in directions:
            nrow = dr + row
            ncol = dc + col
            if 0 <= nrow < m and 0 <= ncol < n and not vis[nrow][ncol] and grid[nrow][ncol] == "1":
                self.dfs(nrow,ncol,vis,grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        vis = [[0] * n for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not vis[i][j]:
                    count += 1
                    self.dfs(i,j,vis,grid)
        
        return count
        