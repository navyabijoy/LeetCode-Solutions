class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [-1] * (n+1) # create an n+1 size 1D Array

        # remove the base case, add the inital values after analyzing the base case
        dp[0] = 0
        dp[1] = 1
        
        # add a for loop to go through all of n+1
        for i in range(2,n+1):
            # remove recursion, store and access it from the database
            dp[i] =dp[i-1] + dp[i-2]

        # agar the value is -1 then store the value of dp[n]
        return dp[n]
            