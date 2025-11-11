class Solution:
    def dfs(self, vis, row, col, grid):
        vis[row][col] = True
        directions = [ (0,-1), (0,1), (1,0),(-1,0)]
        for dr, dc in directions:
            nrow = row + dr
            ncol = col + dc
            if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]) and not vis[nrow][ncol] and grid[nrow][ncol] == "1":
                self.dfs(vis, nrow, ncol, grid)
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        vis = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not vis[i][j]:
                    count += 1
                    self.dfs(vis, i, j, grid)
        return count
