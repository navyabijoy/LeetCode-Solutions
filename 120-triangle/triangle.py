class Solution:
    def helper(self,i,j,n,triangle):
        dp = [[-1] * n for _ in range(len(triangle))]
    
        for j in range(n):
            dp[n-1][j] = triangle[n-1][j]
            
        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
    
                down = triangle[i][j] + dp[i+1][j]
                diag = triangle[i][j] + dp[i+1][j+1]
                dp[i][j] = min(down,diag)
        return dp[0][0]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        return self.helper(0,0,n,triangle)