class Solution:
    def dfs(self,row,col,vis,grid):
        vis[row][col] = 1
        m = len(grid)
        n = len(grid[0])

        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for dr, dc in directions:
            nrow = dr + row
            ncol = dc + col
            if 0 <= nrow < m and 0 <= ncol < n and not vis[nrow][ncol] and grid[nrow][ncol] == 1:
                self.dfs(nrow,ncol,vis,grid)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        vis = [[0] * n for _ in range(m)]
        count = 0
        # traverse the first and last row
        for j in range(n):
            if not vis[0][j] and grid[0][j] == 1:
                self.dfs(0,j,vis,grid)
            if not vis[m-1][j] and grid[m-1][j] == 1:
                self.dfs(m-1,j,vis,grid)

        # traverse the first and last col
        for i in range(m):
            if not vis[i][0] and grid[i][0] == 1:
                self.dfs(i,0,vis,grid)
            if not vis[i][n-1] and grid[i][n-1] == 1:
                self.dfs(i,n-1,vis,grid)
        
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and grid[i][j] == 1:
                    count += 1
                    grid[i][j] = 0
        return count
            
        