class Solution:
    def solve(self, r, c, mat,dp):
        if r < 0 or c < 0:
            return 0

        if mat[r][c] == 1:
            return 0

        if r == 0 and c == 0:
            return 1
        if dp[r][c] != -1:
            return dp[r][c]
        up = self.solve(r-1,c,mat,dp)
        left = self.solve(r,c-1,mat,dp)
        
        dp[r][c] = up + left
        return dp[r][c]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1] * n for _ in range(m)]
        ans = self.solve(m-1,n-1, obstacleGrid,dp)
        return ans