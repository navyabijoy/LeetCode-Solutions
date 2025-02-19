class Solution:
    def helper(self,i,j):
        dp =[[0] * j for _ in range(i)]

        for a in range(i):
            for b in range(j):
                if a == 0 and b == 0:
                    dp[a][b] = 1
                else:
                    up =  dp[a-1][b]
                    left = dp[a][b-1]
                    dp[a][b] = up + left

        return dp[i-1][j-1]
    def uniquePaths(self, m: int, n: int) -> int:
        return self.helper(m,n)
        