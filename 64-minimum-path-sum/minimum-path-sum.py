class Solution:
    def solve(self,grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]
                else:
                    up = float('inf')
                    left = float('inf')
                    if i > 0:
                        up = grid[i][j] + dp[i - 1][j]
                    if j > 0:
                        left = grid[i][j] + dp[i][j - 1]
                    
                    dp[i][j] = min(up,left)

        return dp[m-1][n-1]

    def minPathSum(self, grid: List[List[int]]) -> int:
        ans = self.solve(grid)
        return ans
