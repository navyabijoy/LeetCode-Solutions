class Solution:
    def helper(self,mat,i,j,dp):
        if i < 0 or j < 0 or mat[i][j] == 1:
            return 0 # out of bounds

        if i == 0 and j == 0:
            return 1 # we have reached the top grid
        if dp[i][j] != -1:
            return dp[i][j]
        # we start from the right most corner and then proceed to subtract 
        up = self.helper(mat,i-1,j,dp)
        left = self.helper(mat,i,j-1,dp) 
        dp[i][j] = up + left
        return dp[i][j]
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        dp =[[-1] * c for _ in range(r)]
        ans = self.helper(obstacleGrid,r-1,c-1,dp)
        return ans