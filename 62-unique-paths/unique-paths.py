class Solution:
    def solve(self, m,n,dp):
        if m == 0 and n == 0:
            return 1
        if m < 0 or n < 0:
            return 0
        if dp[m][n] != -1:
            return dp[m][n]
        up = self.solve(m-1, n, dp)
        left = self.solve(m, n-1, dp)
        dp[m][n] = up + left
        return dp[m][n]
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        ans = self.solve(m-1,n-1,dp)
        return ans