class Solution:
    def fib(self, n: int) -> int:
        dp = [-1] * (n+1) # create an n+1 size 1D Array

        if n <= 1:
            return n
        # AFTER the base case, check if the value is occupied
        if dp[n] != -1:
            return dp[n]

        # agar the value is -1 then store the value of dp[n]
        dp[n] = self.fib(n-1) + self.fib(n-2)
        return dp[n]
            