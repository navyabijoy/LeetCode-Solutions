class Solution:
    def helper(self,mat,i,j):
        dp = [[0] * j for _ in range(i)]

        # if i == 0 and j == 0:
        #     return mat[i][j]
        # if i < 0 or j < 0:
        #     return float('inf')
        # if dp[i][j] != -1:
        #     return dp[i;][j]
        for r in range(i):
            for c in range(j):
                if r == 0 and c == 0:
                    dp[r][c] = mat[0][0]
                else:
                    up = mat[r][c] + dp[r-1][c] if r > 0 else float('inf')
                    left = mat[r][c] + dp[r][c-1] if c > 0 else float('inf')
                    dp[r][c] = min(up,left)

        return dp[i-1][j-1]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        return self.helper(grid,m,n)