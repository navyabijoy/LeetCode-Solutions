class Solution:
    def solve(self,m,n,dp):
        if m == 0 and n == 0:
            return 1

        if m < 0 or n < 0:
            return 0

        if dp[m][n] != -1:
            return dp[m][n]
        
        direction = [[-1,0],[0,-1]] # the path can only be top, left
        path = 0
        for r,c in direction:
            path += self.solve(m+r,n+c,dp)
        dp[m][n] = path
        return dp[m][n] 

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        ans = self.solve(m-1,n-1,dp)
        return ans
        