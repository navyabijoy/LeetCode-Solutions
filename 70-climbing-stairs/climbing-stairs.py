class Solution:
    def helper(self,n,dp):
        if n == 1:
            return 1
        if n == 2:
            return 2

        if dp[n] != -1:
            return dp[n]

        one_step = self.helper(n-1,dp)
        two_step = self.helper(n-2,dp)
        dp[n] = one_step + two_step
        return dp[n]
    def climbStairs(self, n: int) -> int:
        dp = [-1] *( n+1)
        ans  = self.helper(n,dp)
        return ans