class Solution:
    def solve(self, m,n):
        dp = [[0] * n for _ in range(m)]
        
        # dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = 1
                else:
                    up = 0
                    left = 0
                    if i > 0:
                        up = dp[i-1][j] # before dp[0-1][j] -> dp[-1][j] -> wrong
                    if j > 0:
                        left = dp[i][j-1] # before dp[i][0-1] -> dp[i][-1] -> wrong
                    dp[i][j] = up + left
        
        return dp[m-1][n-1]

    def uniquePaths(self, m: int, n: int) -> int:
        ans = self.solve(m,n)
        return ans