class Solution:
    def helper(self,r,c):
        # step 1: define the dp array
        dp = [[0] *c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                if i == 0 and j == 0:
                    dp[i][j] = 1 #base case
                else:
                    up = dp[i-1][j]
                    left = dp[i][j-1]
                    dp[i][j] = up + left
        return dp[r-1][c-1]

    def uniquePaths(self, m: int, n: int) -> int:
        return self.helper(m,n)