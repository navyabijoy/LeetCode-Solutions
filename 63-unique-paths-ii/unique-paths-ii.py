class Solution:
    def solve(self,mat):
        m = len(mat)
        n = len(mat[0])
        dp = [[0] * n for _ in range(m)]
        
        if mat[0][0] == 1:
            return 0

        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if mat[i][j] == 1:
                    dp[i][j] = 0
                else:
                    up = 0
                    left = 0
                    if i > 0:
                        up = dp[i-1][j]
                    if j > 0:
                        left = dp[i][j-1]
                    dp[i][j] = up + left

        return dp[m-1][n-1]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        ans = self.solve(obstacleGrid)
        return ans