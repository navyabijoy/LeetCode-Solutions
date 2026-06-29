class Solution:
    def countTrees(self, n, dp):
        if n <= 1:
            return 1
        if dp[n] != -1:
            return dp[n]
        ans = 0
        for i in range(1,n+1):
            ans +=  self.countTrees(i - 1, dp) * self.countTrees(n - i, dp)
        dp[n] = ans
        return dp[n]

    def numTrees(self, n: int) -> int:
        dp = [-1] * (n+1)
        return self.countTrees(n,dp)
