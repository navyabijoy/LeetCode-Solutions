class Solution:
    def helper(self,mat,i,j,dp):
        if i == 0 and j == 0:
            return mat[i][j]
        if i < 0 or j < 0:
            return float('inf')
        if dp[i][j] != -1:
            return dp[i][j]
        up = mat[i][j] + self.helper(mat,i-1,j,dp)
        left = mat[i][j] + self.helper(mat,i,j-1,dp)
        dp[i][j] = min(up,left)
        return dp[i][j]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        return self.helper(grid,m-1,n-1,dp)