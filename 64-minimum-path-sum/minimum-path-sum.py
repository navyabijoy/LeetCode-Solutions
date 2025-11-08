class Solution:
    def solve(self, r, c, grid, dp):
        if r == 0 and c == 0:
            return grid[0][0]
        if r < 0 or c < 0:
            return float('inf')
        if dp[r][c] != -1:
            return dp[r][c]
        up = grid[r][c] + self.solve(r - 1, c, grid, dp)
        left = grid[r][c] + self.solve(r, c - 1, grid, dp)
        
        dp[r][c] = min(up,left)
        return dp[r][c]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        ans = self.solve(m - 1, n - 1, grid, dp)
        return ans
