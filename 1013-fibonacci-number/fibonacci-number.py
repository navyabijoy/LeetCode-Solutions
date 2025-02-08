class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        # remove the base case, add the inital values after analyzing the base case
        prev1 = 1
        prev2 = 0
        
        # add a for loop to go through all of n+1
        for i in range(2,n+1):
            # remove recursion, store and access it from the database
            curr = prev1+prev2
            prev2 = prev1
            prev1 = curr

        # agar the value is -1 then store the value of dp[n]
        return prev1
            