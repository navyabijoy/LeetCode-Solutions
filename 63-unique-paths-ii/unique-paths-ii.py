class Solution:
    def helper(self, mat, r, c,dp):
        if r < 0 or c < 0 or mat[r][c] == 1:
            return 0
        if r == 0 and c == 0:
            return 1
        
        if dp[r][c] != -1:
            return dp[r][c]
        up = self.helper(mat,r-1, c,dp)
        left = self.helper(mat,r,c-1,dp)
        dp[r][c] = up + left
        return dp[r][c]
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1]*n for _ in range(m)]
        return self.helper(obstacleGrid,m-1,n-1,dp)