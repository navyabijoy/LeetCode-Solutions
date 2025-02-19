class Solution:
    def helper(self,i,j,n,triangle,dp):
        if i == n-1:
            return triangle[i][j]
        if dp[i][j] != -1:
            return dp[i][j]
        down = triangle[i][j] + self.helper(i+1,j,n,triangle,dp)
        diag = triangle[i][j] + self.helper(i+1,j+1,n,triangle,dp)
        dp[i][j] = min(down,diag)
        return dp[i][j]
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1] * n for _ in range(len(triangle))]
        return self.helper(0,0,n,triangle,dp)